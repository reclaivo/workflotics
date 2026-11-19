function buildVis(){
 $('vis').innerHTML=`
 <div id="pic" class="abs card" style="left:120px;top:700px;width:840px;height:630px;overflow:hidden;border-radius:44px;padding:0">
  <img id="img" src="file:///home/claude/wf/v3/img/3d-property-walkthrough.webp" style="position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover">
  <div id="clutter" style="position:absolute;inset:0;background:radial-gradient(circle at 20% 30%,rgba(60,50,40,.7) 0,transparent 22%),radial-gradient(circle at 75% 65%,rgba(70,60,40,.7) 0,transparent 20%),radial-gradient(circle at 50% 85%,rgba(50,40,30,.7) 0,transparent 18%)"></div>
  <div id="after" style="position:absolute;left:0;top:0;width:100%;height:100%;overflow:hidden;opacity:0"><img src="file:///home/claude/wf/v3/img/3d-property-walkthrough.webp" style="position:absolute;left:0;top:0;width:840px;height:630px;object-fit:cover"></div>
  <div id="divl" style="position:absolute;top:0;width:6px;height:100%;background:#fff;box-shadow:0 0 30px #A66BFF;opacity:0"></div>
  <div id="tagB" class="lbl" style="position:absolute;left:24px;top:24px;padding:10px 20px;border-radius:20px;background:rgba(0,0,0,.65);font-size:26px;opacity:0">Before</div>
  <div id="tagA" class="lbl" style="position:absolute;right:24px;top:24px;padding:10px 20px;border-radius:20px;background:#8802F6;font-size:26px;opacity:0">After</div>
 </div>
 <div id="chips" class="abs" style="left:0;top:1400px;width:1080px;display:flex;justify-content:center;gap:24px">${['Light','Sharpness','Background'].map((c,i)=>`<div id="c${i}" class="chip" style="font-size:36px;min-width:230px;text-align:center;color:#a89ccf;border-color:#4a3d6e;background:rgba(20,12,40,.8);box-shadow:none"><span id="cc${i}" style="display:inline-block;width:30px"></span>${c}</div>`).join('')}</div>`;
 endcard();
}
function scene(t){
 const S=CFG.segs;
 const L=eo(P(t,S[2].s,.5)),Sh=eo(P(t,S[3].s,.5)),B=eo(P(t,S[4].s,.5));
 const img=$('img');
 img.style.filter=`brightness(${.5+.5*L}) contrast(${.75+.25*Sh}) saturate(${.55+.45*L}) blur(${4*(1-Sh)}px)`;
 $('clutter').style.opacity=1-B;
 tf($('pic'),{y:Math.sin(t*2)*5,ry:-4+Math.sin(t*1.1)*2});
 [L,Sh,B].forEach((v,i)=>{const on=v>0.5;const c=$('c'+i);c.style.color=on?'#fff':'#a89ccf';c.style.borderColor=on?'#A66BFF':'#4a3d6e';c.style.background=on?'rgba(136,2,246,.35)':'rgba(20,12,40,.8)';c.style.boxShadow=on?'0 0 40px rgba(136,2,246,.6)':'none';$('cc'+i).innerHTML=on?'&#10003;':'';c.style.transform=on?'scale(1.04)':'scale(1)'});
 // final before/after sweep
 const s5=S[5].s,d5=S[5].d;
 const sp=P(t,s5+.2,d5-.5);
 const inSweep=t>=s5;
 $('after').style.opacity=inSweep?1:0;$('divl').style.opacity=inSweep?1:0;$('tagB').style.opacity=inSweep?1:0;$('tagA').style.opacity=inSweep?1:0;
 const x=840*(0.12+0.76*(0.5-0.5*Math.cos(sp*Math.PI*1.0)));
 $('after').style.clipPath=`inset(0 0 0 ${x}px)`;$('divl').style.left=(x-3)+'px';
 if(inSweep){$('img').style.filter=`brightness(.5) contrast(.75) saturate(.55) blur(4px)`;$('clutter').style.opacity=1}
}
