import json,sys,os,subprocess,numpy as np,soundfile as sf
from scipy.signal import butter,lfilter
reel=sys.argv[1]; mode=sys.argv[2]  # stills|full
SR=24000; FPS=30
raw=json.load(open(f'{reel}_segs.json'))
GAP=0.3; t=0.03; segs=[]
for r in raw:
    segs.append(dict(cap=r['cap'],s=round(t,3),d=round(r['d'],3))); t+=r['d']+GAP
last=segs[-1]
endAt=round(last['s']-0.05,3)
total=round(last['s']+last['d']+1.55,2)
assert total<=14.9,total
if reel=='r1':
    hook=[0,1]; 
    for i in (2,3): segs[i]['punch']=.06
    s3=segs[3]; bt=s3['s']+s3['d']*.64
    flashes=[s3['s'],bt,endAt]
elif reel=='r2':
    hook=[0]
    for i in (1,2,3): segs[i]['punch']=.03
    for i in (4,5): segs[i]['punch']=.07
    s5=segs[5]; ct=s5['s']+s5['d']*.5
    flashes=[segs[4]['s'],s5['s'],ct,endAt]
elif reel in('r3','r4','r5') or int(reel[1:])>=7:
    hook=[0]
    for i in (2,3,4): segs[i]['punch']=.04
    segs[5]['punch']=.06
    flashes=[segs[5]['s'],endAt]
else:
    hook=[0]
    for i in (1,2,3,4): segs[i]['punch']=.04
    flashes=[segs[1]['s'],segs[3]['s'],endAt]
cfg=dict(segs=segs,hook=hook,endAt=endAt,flashes=flashes,total=total,hookSize=86)
if int(reel[1:])>=7: cfg.update(hookSize=80,bodySize=88,capW=700)
json.dump(cfg,open(f'{reel}_cfg.json','w'))
GENJ=('const GEN='+open(f'{reel}_gen.json').read()+';') if int(reel[1:])>=7 else ''
html=open('reel.html').read().replace('<script id="scene"></script>','<script>'+GENJ+open(({'r1':'scene1.js','r2':'scene2.js','r3':'scene3.js','r4':'scene4.js','r5':'scene5.js','r6':'scene6.js'}).get(reel,'scene_gen.js')).read()+'</script>')
open(f'{reel}.html','w').write(html)
from playwright.sync_api import sync_playwright
def render(times,outdir,prefix):
    os.makedirs(outdir,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport=dict(width=1080,height=1920))
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file:///home/claude/reels/'+reel+'.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(600)
        pg.evaluate('init(%s)'%json.dumps(cfg))
        for i,tt in times:
            pg.evaluate('frame(%f)'%tt)
            pg.screenshot(path=f'{outdir}/{prefix}{i:04d}.jpg',type='jpeg',quality=92)
        b.close()
    if errs: print('ERRORS',errs[:3])
if mode=='stills':
    pts=[0,segs[2]['s']+.5,segs[4]['s']+.5,segs[5]['s']+1.0,endAt+1.2] if reel not in('r1','r2') else [0,segs[1]['s']+.5,segs[2]['s']+.6,segs[3]['s']+1.5,segs[3]['s']+3.9,endAt+1.2] if reel=='r1' else [0,segs[1]['s']+.6,segs[3]['s']+.6,segs[4]['s']+.3,segs[5]['s']+.9,segs[5]['s']+2.3,endAt+1.2]
    import shutil; shutil.rmtree(f'stills_{reel}',ignore_errors=True); render([(i,x) for i,x in enumerate(pts)],f'stills_{reel}','s'); print('stills',[round(x,2) for x in pts],'total',total); sys.exit()
# ---------- audio
rng=np.random.default_rng(3)
N=int(total*SR); mix=np.zeros(N)
def add(sig,at,g=1.0):
    i=int(at*SR); 
    if i>=N: return
    sig=sig[:N-i]; mix[i:i+len(sig)]+=sig*g
def tt(d): return np.arange(int(d*SR))/SR
def env(d,a=.01,r=None):
    x=tt(d); r=r or d-a
    return np.minimum(1,x/a)*np.exp(-(x-a).clip(0)/ (r/4))
def whoosh(d=.55):
    n=rng.standard_normal(int(d*SR)); b,a=butter(2,[500/(SR/2),5000/(SR/2)],'band'); n=lfilter(b,a,n)
    x=tt(d); e=np.sin(np.pi*np.clip(x/d,0,1))**2; return n*e*.6
def boom(d=1.0):
    x=tt(d); f=95*np.exp(-x*2.2)+38; ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-x*3.2)*1.0 + lfilter(*butter(2,300/(SR/2)),rng.standard_normal(len(x)))*np.exp(-x*9)*.5
def tick():
    x=tt(.07); return np.sin(2*np.pi*1900*x)*np.exp(-x*70)*.7+rng.standard_normal(len(x))*np.exp(-x*120)*.3
def pop(f=700):
    x=tt(.16); fr=f+300*np.exp(-x*25); return np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-x*22)*.6
def ding(f=1318,d=1.3):
    x=tt(d); return (np.sin(2*np.pi*f*x)+.35*np.sin(2*np.pi*2*f*x)+.15*np.sin(2*np.pi*3*f*x))*np.exp(-x*3.2)*.5
def ring():
    x=tt(.4); return (np.sin(2*np.pi*440*x)+np.sin(2*np.pi*480*x))*.5*np.minimum(1,x/.01)*np.minimum(1,(.4-x)/.02)*.35
def chime():
    out=np.zeros(int(1.6*SR))
    for k,f in enumerate([880,1108.7,1318.5]):
        s=ding(f,1.2)*.8; i=int(k*.11*SR); out[i:i+len(s)]+=s[:len(out)-i]
    return out
# voice
for i,s in enumerate(segs):
    a,sr=sf.read(f'{reel}_{i}.wav'); 
    assert sr==SR; add(a/ max(1e-6,np.abs(a).max())*.9,s['s'])
S=segs
if reel=='r1':
    k=0
    while k*0.9<S[1]['s']+S[1]['d']+.3 and k<4: add(ring(),.1+k*.9,.8); k+=1
    add(tick(),S[1]['s']+.2); add(boom(.8),S[2]['s'],.5); add(whoosh(),S[2]['s']-.2,.7)
    add(whoosh(.5),S[3]['s']-.15,.9); add(boom(.9),S[3]['s'],.55)
    for i in range(5): add(pop(600+i*70),S[3]['s']+.45+i*.38,.8)
    bt=S[3]['s']+S[3]['d']*.64; add(boom(1.1),bt,.6); add(ding(1318),bt+.05,.9)
elif reel in('r3','r4','r5') or int(reel[1:])>=7:
    add(whoosh(.45),S[1]['s']-.15,.6)
    for i in range(2,5): add(pop(620+i*60),S[i]['s']+.1,.9)
    if reel=='r3': add(ding(1318),S[2]['s']+.15,.5); add(ding(1568),S[3]['s']+.15,.5); add(ding(1760),S[4]['s']+.15,.5)
    add(whoosh(.5),S[5]['s']-.2,.9); add(boom(1.0),S[5]['s'],.55); add(ding(1318),S[5]['s']+.25,.8)
elif reel=='r6':
    for i in range(1,5): add(whoosh(.35),S[i]['s']-.12,.6); add(pop(560+i*80),S[i]['s']+.05,.9)
    add(boom(.8),S[1]['s'],.35)
else:
    for i in range(3): add(tick(),S[i+1]['s']+.1,.9)
    add(boom(.8),S[4]['s']-.02,.6); add(whoosh(.5),S[5]['s']-.2,.9)
    for i in range(4): add(pop(560+i*90),S[5]['s']+.15+i*.22,.8)
    ct=S[5]['s']+S[5]['d']*.5; add(boom(1.1),ct,.6); add(ding(1318),ct+.05,.9)
add(whoosh(.5),endAt-.2,.9); add(chime(),endAt+.1,.7)
# music: soft pad, no beat
x=tt(total); chords=[[220,261.6,329.6],[174.6,220,261.6],[261.6,329.6,392],[196,246.9,293.7]]
pad=np.zeros(N)
for ci in range(int(total/3.2)+2):
    for f in chords[ci%4]:
        seg=np.arange(int(3.6*SR))/SR; e=np.sin(np.pi*np.clip(seg/3.6,0,1))**1.5
        w=(np.sin(2*np.pi*f*seg)+.5*np.sin(2*np.pi*f*1.004*seg)+.2*np.sin(2*np.pi*2*f*seg))*e
        i=int(ci*3.2*SR); 
        if i<N: w=w[:N-i]; pad[i:i+len(w)]+=w
b,a=butter(2,1200/(SR/2)); pad=lfilter(b,a,pad); pad/=np.abs(pad).max()
pad*=np.minimum(1,x/0.05)*np.minimum(1,(total-x)/1.0)*.14
mix=mix+pad
mix=np.tanh(mix*1.05)*.95
sf.write(f'{reel}_audio.wav',mix,SR)
# ---------- frames
nf=int(total*FPS)
import shutil; shutil.rmtree(f'frames_{reel}',ignore_errors=True)
render([(i,i/FPS) for i in range(nf)],f'frames_{reel}','f')
out=f'/home/claude/reels/{reel}.mp4'
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'frames_{reel}/f%04d.jpg','-i',f'{reel}_audio.wav','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart',out],check=True)
print('done',out,total)
