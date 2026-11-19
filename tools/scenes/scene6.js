function buildVis(){
 const G=[['Creative','Ads, images, 3D sites','<path d="M12 3l2.6 5.6L21 10l-4.5 4.4L17.6 21 12 18l-5.6 3 1.1-6.6L3 10l6.4-1.4z"/>'],['Build','Websites, chatbots, voice','<path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>'],['Automate','Workflows that run alone','<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'],['Shop','Ready-made templates','<path d="M6 7h12l-1 13H7zM9 7a3 3 0 0 1 6 0"/>']];
 $('vis').innerHTML=G.map((c,i)=>`<div id="g${i}" class="abs card" style="left:${60+(i%2)*490}px;top:${760+Math.floor(i/2)*440}px;width:470px;height:400px;border-radius:44px;opacity:1">
  <div style="position:absolute;left:36px;top:40px;width:120px;height:120px;border-radius:32px;background:rgba(136,2,246,.3);border:2px solid #A66BFF;display:flex;align-items:center;justify-content:center"><svg width="66" height="66" viewBox="0 0 24 24" fill="none" stroke="#EEE5FE" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">${c[2]}</svg></div>
  <div style="position:absolute;left:36px;top:190px;font-weight:700;font-size:70px">${c[0]}</div>
  <div class="lbl" style="position:absolute;left:38px;top:290px;width:400px;font-size:23px;line-height:1.5;color:#9a8fb8">${c[1]}</div></div>`).join('');
 endcard();
}
function scene(t){
 const S=CFG.segs;
 for(let i=0;i<4;i++){
  const st=S[i+1].s,on=t>=st&&t<(i<3?S[i+2].s:S[5].s),p=eb(P(t,st,.3)),past=t>=st;
  const c=$('g'+i);
  c.style.borderColor=past?'#A66BFF':'rgba(166,107,255,.35)';
  c.style.boxShadow=on?'0 0 110px rgba(136,2,246,.8),0 40px 90px #000':'0 40px 90px rgba(0,0,0,.7)';
  c.style.background=on?'linear-gradient(160deg,#3a1578,#120a22)':'linear-gradient(160deg,#1b1330,#0d0919)';
  tf(c,{y:Math.sin(t*2+i)*4,s:on?(1.05-.05*(1-p)):1,ry:(i%2?6:-6),rx:i<2?4:-2});
 }
}
