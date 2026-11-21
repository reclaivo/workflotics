import json,sys
from playwright.sync_api import sync_playwright
bad=0
with sync_playwright() as p:
    b=p.chromium.launch()
    import glob
    for r in sorted([f[:-9] for f in glob.glob('r*_cfg.json')],key=lambda x:int(x[1:])):
        cfg=json.load(open(f'{r}_cfg.json'))
        pg=b.new_page(viewport=dict(width=1080,height=1920))
        pg.goto(f'file:///home/claude/reels/{r}.html'); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(500)
        pg.evaluate('init(%s)'%json.dumps(cfg))
        ts=[0.0]
        for s in cfg['segs'][:-1]:
            ts+= [s['s']+s['d']*.3, s['s']+s['d']*.85]
        ts+=[cfg['endAt']+1.2]
        for t in ts:
            res=pg.evaluate("""(t)=>{frame(t);
              const out={};
              const sp=[...document.querySelectorAll('#cap span')].filter(e=>getComputedStyle(e).opacity!=='0');
              if(document.getElementById('cap').style.display!=='none'&&sp.length){const L=Math.min(...sp.map(e=>e.getBoundingClientRect().left)),R=Math.max(...sp.map(e=>e.getBoundingClientRect().right));out.cap=[L,R,(L+R)/2]}
              const ch=document.getElementById('chips');if(ch&&t<%f){const rs=[...ch.children].map(e=>e.getBoundingClientRect());const L=Math.min(...rs.map(x=>x.left)),R=Math.max(...rs.map(x=>x.right));out.chips=[L,R,(L+R)/2];out.gaps=rs.slice(1).map((x,i)=>Math.round(x.left-rs[i].right))}
              const e=document.getElementById('e_cta');if(e&&t>=%f){const q=e.getBoundingClientRect();out.cta=[q.left,q.right,(q.left+q.right)/2]}
              return out}"""%(cfg['endAt'],cfg['endAt']),t)
            msg=[]
            for k in ('cap','chips','cta'):
                if k in res:
                    L,R,c=res[k]
                    if abs(c-540)>10 or (k=='cap' and (L<135 or R>945)): msg.append(f'{k} centre {c:.0f} L{L:.0f} R{R:.0f}')
            if 'gaps' in res and min(res['gaps'])<10: msg.append(f"gaps {res['gaps']}")
            if msg: bad+=1; print(r,round(t,2),msg)
        pg.close()
    b.close()
print('issues',bad)
