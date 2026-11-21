function buildVis(){
 const G=GEN;
 $('vis').innerHTML=`
 <div id="win" class="abs card" style="left:150px;top:700px;width:780px;height:300px;overflow:hidden;border-radius:36px">
  <div style="position:absolute;left:0;top:0;width:100%;height:300px;background:radial-gradient(circle at 25% 50%,rgba(136,2,246,.45),transparent 60%)"></div>
  <div style="position:absolute;left:60px;top:70px;width:160px;height:160px;border-radius:44px;background:rgba(136,2,246,.3);border:3px solid #A66BFF;display:flex;align-items:center;justify-content:center;box-shadow:0 0 60px rgba(136,2,246,.6)"><svg width="96" height="96" viewBox="0 0 24 24" fill="none" stroke="#EEE5FE" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">${G.icon}</svg></div>
  <div style="position:absolute;left:260px;top:72px;width:490px;font-weight:700;font-size:54px;line-height:1.05">${G.title}</div>
  <div class="lbl" style="position:absolute;left:262px;top:204px;width:480px;font-size:22px;color:#9a8fb8">${G.sub}</div>
 </div>
 ${G.items.map((c,i)=>`<div id="k${i}" class="abs card" style="left:150px;top:${1040+i*190}px;width:780px;height:150px;border-radius:36px">
  <div style="position:absolute;left:30px;top:28px;width:94px;height:94px;border-radius:26px;background:rgba(136,2,246,.3);border:2px solid #A66BFF;display:flex;align-items:center;justify-content:center"><svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="#EEE5FE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${c[2]}</svg></div>
  <div style="position:absolute;left:150px;top:26px;font-weight:700;font-size:50px">${c[0]}</div>
  <div class="lbl" style="position:absolute;left:152px;top:96px;font-size:22px;color:#9a8fb8">${c[1]}</div>
  <div id="ck${i}" style="position:absolute;right:32px;top:32px;width:86px;height:86px;border-radius:43px;border:4px solid #4a3d6e;display:flex;align-items:center;justify-content:center"><svg id="cks${i}" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" style="opacity:0"><path d="M5 12l5 5L20 7"/></svg></div></div>`).join('')}
 <div id="chat" class="abs card" style="left:150px;top:1620px;width:780px;height:250px;opacity:0;background:linear-gradient(160deg,#2a0f55,#0d0919);border-color:#A66BFF;box-shadow:0 0 110px rgba(136,2,246,.7),0 40px 90px #000">
  <div style="position:absolute;left:0;top:0;width:780px;height:250px;display:flex;align-items:center;justify-content:center;text-align:center;padding:0 50px;font-weight:700;font-size:54px;line-height:1.12;text-shadow:0 0 30px #8802F6">${G.final}</div></div>`;
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
