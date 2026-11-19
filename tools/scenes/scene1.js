function buildVis(){
 const bars=Array.from({length:13},(_,i)=>`<div class="bar" id="b${i}" style="position:absolute;left:${34+i*26}px;bottom:0;width:14px;height:20px;border-radius:7px;background:linear-gradient(#EEE5FE,#A66BFF)"></div>`).join('');
 $('vis').innerHTML=`
 <div id="ph" class="abs phone" style="left:320px;top:700px"><div class="screen"><div class="notch"></div>
  <div id="ring" class="abs" style="left:0;top:0;width:100%;height:100%">
   <div class="lbl" style="position:absolute;top:120px;width:100%;text-align:center;font-size:26px;color:#9a8fb8">Incoming call</div>
   <div id="halo" class="abs" style="left:116px;top:200px;width:180px;height:180px;border-radius:90px;background:rgba(255,60,90,.35)"></div>
   <div class="abs" style="left:126px;top:210px;width:160px;height:160px;border-radius:80px;background:#3a0f1a;display:flex;align-items:center;justify-content:center">${phoneSvg('#ff4d6d')}</div>
   <div id="missTxt" style="position:absolute;top:430px;width:100%;text-align:center;font-weight:700;font-size:58px;color:#ff4d6d">Missed call</div>
   <div class="lbl" style="position:absolute;top:515px;width:100%;text-align:center;font-size:34px;color:#cfc3ee">8:00 PM</div>
   <div id="vm" style="position:absolute;left:66px;top:640px;width:280px;height:84px;border-radius:42px;background:#1a1428;border:2px solid #3b3350;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:36px;color:#cfc3ee">Voicemail
    <div id="vmx" style="position:absolute;left:14px;top:40px;height:6px;width:252px;background:#ff4d6d;border-radius:3px;box-shadow:0 0 20px #ff4d6d;transform-origin:0 50%;transform:scaleX(0)"></div></div>
  </div>
  <div id="ai" class="abs" style="left:0;top:0;width:100%;height:100%;opacity:0;background:linear-gradient(170deg,#6a0fc9,#1a0838 70%)">
   <img src="${LOGO}" style="position:absolute;left:146px;top:130px;width:120px;height:120px;border-radius:28px;box-shadow:0 0 60px rgba(166,107,255,.9)">
   <div style="position:absolute;top:290px;width:100%;text-align:center;font-weight:700;font-size:52px">AI voice agent</div>
   <div class="lbl" id="ailbl" style="position:absolute;top:372px;width:100%;text-align:center;font-size:24px;color:#EEE5FE">Answering</div>
   <div style="position:absolute;left:0;top:560px;width:100%;height:120px">${bars}</div>
  </div>
 </div></div>
 <div id="lost" class="abs card" style="left:120px;top:960px;width:840px;height:250px;opacity:0;border-color:#ff4d6d;display:flex;align-items:center;justify-content:center;gap:30px;font-weight:700;font-size:70px;color:#ff4d6d;box-shadow:0 0 90px rgba(255,77,109,.4),0 40px 90px #000">Customer gone</div>
 <div id="chips"></div>
 <div id="book" class="abs card" style="left:150px;top:1260px;width:780px;height:290px;opacity:0;background:linear-gradient(160deg,#2a0f55,#0d0919);border-color:#A66BFF;box-shadow:0 0 120px rgba(136,2,246,.8),0 40px 90px #000">
   <div style="position:absolute;left:46px;top:62px;width:120px;height:120px;border-radius:60px;background:#8802F6;display:flex;align-items:center;justify-content:center;box-shadow:0 0 50px #8802F6"><svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></div>
   <div style="position:absolute;left:206px;top:50px;font-weight:700;font-size:92px">Booked.</div>
   <div style="position:absolute;left:206px;top:170px;font-weight:500;font-size:58px;color:#CDB4FF">Friday 7 PM</div></div>`;
 const L=[['English',30,790,-4],['Français',30,930,3],['हिन्दी',30,1070,-3],['Español',800,860,4],['العربية',800,1000,-3]];
 $('chips').innerHTML=L.map((c,i)=>`<div id="c${i}" class="abs chip" style="left:${c[1]}px;top:${c[2]}px;font-size:${i>2?44:40}px;font-family:SG,'DejaVu Sans','Noto Sans Devanagari',sans-serif">${c[0]}</div>`).join('');
 endcard();
}
function scene(t){
 const S=CFG.segs,s2=S[2],s3=S[3];
 const T3=s3.s,D3=s3.d;
 // phone
 let ph={x:0,y:Math.sin(t*2)*6,s:1,r:0,o:1,ry:-8+Math.sin(t*1.2)*3};
 if(t<S[1].s+S[1].d+.2) ph.r=Math.sin(t*46)*1.4;
 const pOut=P(t,s2.s,.35), pIn=P(t,T3,.01);
 if(t>=s2.s&&t<T3){ph.s=1-.08*eo(pOut);ph.o=1-.78*eo(pOut);ph.y+=70*eo(pOut)}
 if(t>=T3){ph.s=1;ph.o=1;ph.ry=-6+Math.sin(t*1.5)*4}
 tf($('ph'),ph);
 // ring ui
 $('halo').style.transform=`scale(${1+.3*((Math.sin(t*9)+1)/2)})`;$('halo').style.opacity=t<T3?(0.9-.5*((Math.sin(t*9)+1)/2)):0;
 $('vmx').style.transform=`scaleX(${eo(P(t,S[1].s+.2,.3))})`;
 $('vm').style.opacity=.4+.6*(1-P(t,S[1].s+.5,.3)*0.3);
 $('ring').style.opacity=t<T3?1:0;
 $('ai').style.opacity=t>=T3?1:0;
 for(let i=0;i<13;i++){const a=t>=T3?(.25+.75*Math.abs(Math.sin(t*7+i*.7)*Math.sin(t*3.1+i*1.3))):0;$('b'+i).style.height=(18+a*100)+'px'}
 $('ailbl').textContent=t<T3+D3*.62?'Answering':'Booking';
 // lost card
 const lp=eb(P(t,s2.s+.15,.35));
 tf($('lost'),{x:0,y:(1-lp)*80,s:.7+.3*lp,ry:-10+4*Math.sin(t*3),o:(t>=s2.s+.15&&t<T3)?P(t,s2.s+.15,.15):0});
 // chips
 for(let i=0;i<5;i++){const st=T3+.45+i*.38,p=eb(P(t,st,.3));
  tf($('c'+i),{y:(1-p)*50+Math.sin(t*2+i)*7,s:.5+.5*p,o:t>=st?P(t,st,.12):0})}
 // booking
 const bt=T3+D3*.64,bp=eb(P(t,bt,.4));
 tf($('book'),{y:(1-bp)*160,s:.6+.4*bp,rx:12*(1-bp)-3,o:t>=bt?P(t,bt,.1):0});
}
