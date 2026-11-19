function buildVis(){
 const T=[['Copy the lead','Step 1'],['Send the email','Step 2'],['Remind the client','Step 3']];
 const ic=['<path d="M8 4h8v4H8zM6 8h12v12H6z"/>','<path d="M3 6h18v12H3zM3 7l9 7 9-7"/>','<circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 3h6"/>'];
 $('vis').innerHTML=T.map((c,i)=>`
  <div id="k${i}" class="abs card" style="left:130px;top:${740+i*235}px;width:820px;height:190px">
   <div style="position:absolute;left:36px;top:36px;width:118px;height:118px;border-radius:30px;background:rgba(136,2,246,.3);border:2px solid #A66BFF;display:flex;align-items:center;justify-content:center"><svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#EEE5FE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${ic[i]}</svg></div>
   <div id="kt${i}" style="position:absolute;left:186px;top:34px;font-weight:700;font-size:58px">${c[0]}</div>
   <div class="lbl" style="position:absolute;left:188px;top:116px;font-size:26px;color:#9a8fb8">${c[1]} by hand</div>
   <div id="kx${i}" style="position:absolute;left:24px;top:93px;height:8px;width:772px;background:#ff4d6d;border-radius:4px;box-shadow:0 0 24px #ff4d6d;transform-origin:0 50%;transform:scaleX(0)"></div>
  </div>`).join('')+`
  <svg id="lines" class="abs" width="1080" height="1920" style="left:0;top:0;opacity:0"><defs><linearGradient id="lg" x1="0" x2="1"><stop offset="0" stop-color="#A66BFF"/><stop offset="1" stop-color="#8802F6"/></linearGradient></defs>
   <path id="ln" d="M190 980 L420 980 L660 980 L890 980" stroke="url(#lg)" stroke-width="10" fill="none" stroke-linecap="round" style="filter:drop-shadow(0 0 16px #8802F6)"/>
   <circle id="pulse" r="18" fill="#fff" style="filter:drop-shadow(0 0 22px #A66BFF) drop-shadow(0 0 44px #8802F6)"/></svg>
  ${[['Lead',190],['Email',420],['Remind',660],['Done',890]].map((n,i)=>`<div id="n${i}" class="abs" style="left:${n[1]-80}px;top:900px;width:160px;height:160px;opacity:0"><div style="width:160px;height:160px;border-radius:80px;background:${i==3?'#8802F6':'#1b1330'};border:3px solid #A66BFF;box-shadow:0 0 70px rgba(136,2,246,.7);display:flex;align-items:center;justify-content:center"><svg width="70" height="70" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="${i==3?3:1.8}" stroke-linecap="round" stroke-linejoin="round">${i==3?'<path d="M5 12l5 5L20 7"/>':ic[Math.min(i,2)]}</svg></div><div class="lbl" style="position:absolute;top:178px;width:160px;text-align:center;font-size:26px;color:#EEE5FE">${n[0]}</div></div>`).join('')}
  <div id="clk" class="abs card" style="left:150px;top:1230px;width:780px;height:270px;opacity:0;background:linear-gradient(160deg,#2a0f55,#0d0919);border-color:#A66BFF;box-shadow:0 0 120px rgba(136,2,246,.7),0 40px 90px #000">
   <div style="position:absolute;left:50px;top:48px;font-weight:700;font-size:130px;letter-spacing:-2px">2:00 AM</div>
   <div style="position:absolute;left:54px;top:196px;font-weight:500;font-size:44px;color:#CDB4FF;display:flex;align-items:center;gap:18px"><span id="dot" style="width:22px;height:22px;border-radius:11px;background:#A66BFF;box-shadow:0 0 22px #A66BFF"></span>Still working</div></div>`;
 endcard();
}
function scene(t){
 const S=CFG.segs,s5=S[5],s4=S[4];
 // strikes
 for(let i=0;i<3;i++){
  const st=S[i+1].s+.1, p=eo(P(t,st,.28));
  $('kx'+i).style.transform=`scaleX(${p})`;
  const hook=t<S[1].s;
  let o=1-.55*p, y=0, sc=1, r=0;
  const shake=(t>=s4.s&&t<s5.s)?Math.sin(t*60)*5:0;
  const morph=eo(P(t,s5.s,.4));
  tf($('k'+i),{x:shake,y:y-morph*60,s:(1-.3*morph)*(1+0*sc),ry:-8+i*2,r:r,o:(t<s5.s?o:o*(1-morph))*(1)});
  $('k'+i).style.display=(t>=s5.s+.45)?'none':'block';
 }
 // nodes
 const nodeT=s5.s+.15;
 for(let i=0;i<4;i++){const st=nodeT+i*.22,p=eb(P(t,st,.35));tf($('n'+i),{s:.4+.6*p,o:t>=st?P(t,st,.1):0})}
 const lineP=eo(P(t,nodeT+.7,.5));
 $('lines').style.opacity=lineP;
 const ln=$('ln');const len=ln.getTotalLength();ln.style.strokeDasharray=len;ln.style.strokeDashoffset=len*(1-lineP);
 // pulse travels, loops
 const pu=((t-(nodeT+1.0))*0.55)%1, pp=(t>nodeT+1.0)?pu:0;
 const pt=ln.getPointAtLength(len*pp);
 const pc=$('pulse');pc.setAttribute('cx',pt.x);pc.setAttribute('cy',pt.y);pc.style.opacity=(t>nodeT+1.0)?1:0;
 // clock
 const ct=s5.s+s5.d*.5, cp=eb(P(t,ct,.4));
 tf($('clk'),{y:(1-cp)*140,s:.65+.35*cp,rx:10*(1-cp)-2,o:t>=ct?P(t,ct,.1):0});
 $('dot').style.opacity=.5+.5*Math.abs(Math.sin(t*5));
}
