function buildVis(){
 const T=[['Fast on a phone','Loads in a blink','<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'],['Clear in one line','Says what you do','<path d="M4 7h16M4 12h10M4 17h14"/>'],['Answers any hour','Day, night, weekends','<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>']];
 $('vis').innerHTML=`
 <div id="win" class="abs card" style="left:150px;top:700px;width:780px;height:300px;overflow:hidden;border-radius:36px">
  <div style="position:absolute;left:0;top:0;width:100%;height:64px;background:#120c20;border-bottom:2px solid rgba(166,107,255,.25)">
   <div style="position:absolute;left:26px;top:22px;width:20px;height:20px;border-radius:10px;background:#ff4d6d"></div><div style="position:absolute;left:58px;top:22px;width:20px;height:20px;border-radius:10px;background:#e8b84a"></div><div style="position:absolute;left:90px;top:22px;width:20px;height:20px;border-radius:10px;background:#A66BFF"></div>
   <div class="lbl" style="position:absolute;left:150px;top:16px;width:480px;height:34px;border-radius:17px;background:#0b0912;font-size:20px;color:#9a8fb8;padding:6px 18px;letter-spacing:3px">yourbusiness.com</div></div>
  <div style="position:absolute;left:46px;top:100px;width:420px;height:34px;border-radius:10px;background:#3a2a66"></div>
  <div style="position:absolute;left:46px;top:152px;width:300px;height:22px;border-radius:8px;background:#241a40"></div>
  <div style="position:absolute;left:46px;top:200px;width:200px;height:54px;border-radius:27px;background:#8802F6;box-shadow:0 0 30px rgba(136,2,246,.7)"></div>
  <div style="position:absolute;left:520px;top:100px;width:220px;height:160px;border-radius:20px;background:linear-gradient(150deg,#4a1a99,#1a0f33)"></div>
 </div>
 ${T.map((c,i)=>`<div id="k${i}" class="abs card" style="left:150px;top:${1040+i*190}px;width:780px;height:150px;border-radius:36px">
  <div style="position:absolute;left:30px;top:28px;width:94px;height:94px;border-radius:26px;background:rgba(136,2,246,.3);border:2px solid #A66BFF;display:flex;align-items:center;justify-content:center"><svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#EEE5FE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${c[2]}</svg></div>
  <div style="position:absolute;left:150px;top:26px;font-weight:700;font-size:52px">${c[0]}</div>
  <div class="lbl" style="position:absolute;left:152px;top:96px;font-size:22px;color:#9a8fb8">${c[1]}</div>
  <div id="ck${i}" style="position:absolute;right:32px;top:32px;width:86px;height:86px;border-radius:43px;border:4px solid #4a3d6e;display:flex;align-items:center;justify-content:center"><svg id="cks${i}" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"><path d="M5 12l5 5L20 7"/></svg></div></div>`).join('')}
 <div id="chat" class="abs card" style="left:150px;top:1620px;width:780px;height:250px;opacity:0;background:linear-gradient(160deg,#2a0f55,#0d0919);border-color:#A66BFF;box-shadow:0 0 110px rgba(136,2,246,.7),0 40px 90px #000">
  <div style="position:absolute;right:36px;top:28px;padding:16px 28px;border-radius:30px 30px 6px 30px;background:#2a1c4d;font-size:36px;font-weight:500">What time do you open?</div>
  <div style="position:absolute;left:36px;top:128px;padding:16px 28px;border-radius:30px 30px 30px 6px;background:#8802F6;font-size:36px;font-weight:700">Nine AM. Want to book?</div></div>`;
 endcard();
}
function scene(t){
 const S=CFG.segs;
 tf($('win'),{ry:-5+Math.sin(t*1.3)*2,y:Math.sin(t*2)*4});
 for(let i=0;i<3;i++){
  const st=S[i+2].s+.12,p=eb(P(t,st,.3)),on=t>=st;
  const ck=$('ck'+i);ck.style.background=on?'#8802F6':'transparent';ck.style.borderColor=on?'#A66BFF':'#4a3d6e';ck.style.boxShadow=on?'0 0 40px #8802F6':'none';
  $('cks'+i).style.opacity=on?1:0;ck.style.transform=`scale(${on?(.6+.4*p):1})`;
  tf($('k'+i),{y:Math.sin(t*2+i)*3,ry:-4,s:1+(on?.03*(1-P(t,st,.4)):0)});
 }
 const ct=S[5].s+.2,cp=eb(P(t,ct,.4));
 tf($('chat'),{y:(1-cp)*120,s:.7+.3*cp,rx:10*(1-cp),o:t>=ct?P(t,ct,.1):0});
}
