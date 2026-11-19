function buildVis(){
 const bars='';
 $('vis').innerHTML=`
 <div id="ph" class="abs phone" style="left:320px;top:700px"><div class="screen"><div class="notch"></div>
  <div id="adv" class="abs" style="left:0;top:0;width:100%;height:100%;background:linear-gradient(170deg,#241046,#0b0912 70%)">
   <div class="lbl" style="position:absolute;top:110px;width:100%;text-align:center;font-size:24px;color:#9a8fb8">Sponsored</div>
   <div style="position:absolute;left:66px;top:190px;width:280px;height:300px;border-radius:30px;background:linear-gradient(150deg,#6a0fc9,#1a0838);box-shadow:0 0 60px rgba(136,2,246,.5)"><svg style="position:absolute;left:100px;top:110px" width="80" height="80" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></div>
   <div id="cnt" style="position:absolute;top:540px;width:100%;text-align:center;font-weight:700;font-size:110px;letter-spacing:-2px">0.0s</div>
   <div style="position:absolute;left:66px;top:690px;width:280px;height:16px;border-radius:8px;background:#241a40"><div id="bar" style="height:16px;width:0%;border-radius:8px;background:linear-gradient(90deg,#A66BFF,#8802F6);box-shadow:0 0 20px #8802F6"></div></div>
   <div id="swipe" class="abs" style="left:156px;top:740px"><svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="#A66BFF" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M6 11l6-6 6 6"/></svg></div>
  </div></div></div>
 ${[['1','Problem',60,830],['2','One idea',770,980],['3','Next step',60,1130]].map((c,i)=>`<div id="st${i}" class="abs chip" style="left:${c[2]}px;top:${c[3]}px;font-size:40px"><span style="color:#A66BFF">${c[0]}</span>&nbsp; ${c[1]}</div>`).join('')}
 ${['A','B','C'].map((l,i)=>`<div id="m${i}" class="abs" style="left:${55+i*335}px;top:900px;width:300px;height:600px;opacity:0"><div class="phone" style="width:300px;height:600px;border-radius:50px;padding:10px"><div class="screen" style="border-radius:42px;background:linear-gradient(${150+i*30}deg,${['#6a0fc9','#3a1c8f','#8802F6'][i]},#120a22 80%)"><svg style="position:absolute;left:100px;top:230px" width="90" height="90" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></div></div><div style="position:absolute;left:0;top:640px;width:300px;text-align:center;font-weight:700;font-size:64px;color:#EEE5FE;text-shadow:0 0 30px #8802F6">${l}</div></div>`).join('')}
 `;
 endcard();
}
function scene(t){
 const S=CFG.segs,s5=S[5].s;
 const main=t<s5;
 const sw=Math.sin(t*5);
 tf($('ph'),{y:Math.sin(t*2)*6,ry:-8+Math.sin(t*1.2)*3,s:1,o:main?1:0});
 $('swipe').style.transform=`translateY(${-20*((t*1.5)%1)}px)`;$('swipe').style.opacity=1-((t*1.5)%1);
 const cp=P(t,S[1].s,S[1].d*.9);
 const cv=t<S[1].s?0:eo(cp)*1.0;
 $('cnt').textContent=cv.toFixed(1)+'s';$('bar').style.width=(cv*100)+'%';
 for(let i=0;i<3;i++){
  const st=S[i+2].s+.05,p=eb(P(t,st,.3));
  tf($('st'+i),{y:(1-p)*40,s:.6+.4*p,o:main&&t>=st?P(t,st,.1):0});
 }
 for(let i=0;i<3;i++){const st=s5+.1+i*.28,p=eb(P(t,st,.35));
  tf($('m'+i),{y:(1-p)*80+Math.sin(t*2+i)*8,s:.6+.4*p,ry:(i-1)*-10,o:t>=st?P(t,st,.12):0})}
}
