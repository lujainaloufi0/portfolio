/* ── cursor: a small dot that follows the pointer; it grows into EXPLORE over project titles and cards ── */
const cursorEl=(()=>{
  if(!matchMedia("(hover:hover) and (pointer:fine)").matches)return null;
  const c=d.createElement("div");c.className="cursor";c.setAttribute("aria-hidden","true");c.textContent="EXPLORE";d.body.append(c);
  root.classList.add("has-cursor");
  let x=-100,y=-100,tx=-100,ty=-100,raf=0;
  const tick=()=>{x+=(tx-x)*.28;y+=(ty-y)*.28;c.style.setProperty("--x",x+"px");c.style.setProperty("--y",y+"px");raf=(Math.abs(tx-x)+Math.abs(ty-y)>.1)?requestAnimationFrame(tick):0};
  addEventListener("pointermove",e=>{tx=e.clientX;ty=e.clientY;if(calm){x=tx;y=ty;c.style.setProperty("--x",x+"px");c.style.setProperty("--y",y+"px")}else if(!raf)raf=requestAnimationFrame(tick);c.classList.add("on")},{passive:true});
  d.addEventListener("pointerleave",()=>c.classList.remove("on"));
  addEventListener("blur",()=>c.classList.remove("on"));
  addEventListener("pointerdown",()=>c.classList.add("down"));
  addEventListener("pointerup",()=>c.classList.remove("down"));
  d.addEventListener("pointerover",e=>{
    const t=e.target;
    const big=t.closest&&t.closest("#stage .card.is-on");
    const link=!big&&t.closest&&t.closest("a, button, label, [role=tab], summary, select");
    c.classList.toggle("big",!!big);c.classList.toggle("link",!!link);
  });
  return c;
})();

/* ── projects: colours per project ── */
const P=[
  {title:"Tawaqaa",night:"#071820",bg:"#0F3442",ink:"#E9F5F8",acc:"#1FA6BC",deep:"#082230"},
  {title:"Masar",night:"#071A12",bg:"#123A2B",ink:"#EAF3EE",acc:"#2E9E6E",deep:"#0A261B"},
  {title:"Fridge & Friends",night:"#240805",bg:"#5E140E",ink:"#F4E7C8",acc:"#D9A033",deep:"#3D0D09"},
  {title:"Stack",night:"#0C0C0C",bg:"#262626",ink:"#F2EFEA",acc:"#4A4A4A",deep:"#161616"}
];
const N=P.length;
const home=$("#home"),hero=$(".hero"),stage=$("#stage"),cards=$$("#stage .card"),belt=$("#belt"),attr=$("#attr"),beltBtns=$$("#belt button"),ticks=$$(".ticks button"),catItems=$$("#cat-list li");
const beltLis=[...belt.children],attrLis=[...attr.children];
let cur=0,busy=false;
/* split each title into letters so it can rise letter by letter */
const paint=()=>{
  const p=P[cur],bg=isDark()?p.night:p.bg;
  home.style.setProperty("--pbg",bg);home.style.setProperty("--pink",p.ink);home.style.setProperty("--pacc",p.acc);
  cursorEl&&cursorEl.style.setProperty("--acc",p.acc);
  beltBtns.forEach((b,k)=>b.tabIndex=k===cur?0:-1);
  ticks.forEach((b,k)=>b.setAttribute("aria-current",k===cur));
  catItems.forEach((li,k)=>li.classList.toggle("is-current",k===cur));
  cards.forEach((c,k)=>{c.tabIndex=k===cur?0:-1;c.setAttribute("aria-hidden",k!==cur)});
  $("#live").textContent=`Project ${cur+1} of ${N}: ${p.title}`;
  const tc=$('meta[name="theme-color"]');if(tc)tc.content=bg;
};
/* put a title, line and card straight into place with no motion */
const setInstant=k=>{
  [beltLis,attrLis].forEach(list=>list.forEach((li,j)=>{li.classList.add("prep");li.classList.remove("out");li.classList.toggle("on",j===k)}));
  cards.forEach((c,j)=>{c.classList.add("instant");c.classList.remove("leave","enter");c.classList.toggle("is-on",j===k)});
  stage.offsetWidth;
  [...beltLis,...attrLis].forEach(li=>li.classList.remove("prep"));cards.forEach(c=>c.classList.remove("instant"));
};
/* project change: the old card drops, grows and fades in front while the new one settles in
   from behind; the old title slides out of its slot letter by letter and the new one rises into it */
const show=async(to,dirHint)=>{
  if(busy||to===cur)return;busy=true;
  const from=cur,dir=dirHint||(((to-from+N)%N)<=N/2?1:-1);
  cur=to;paint();
  if(calm){setInstant(to);busy=false;return}
  hero.classList.remove("booting");
  [beltLis[to],attrLis[to]].forEach(el=>{el.classList.add("prep");el.classList.remove("out")});
  stage.offsetWidth;
  [beltLis[to],attrLis[to]].forEach(li=>li.classList.remove("prep"));
  beltLis[from].classList.replace("on","out");attrLis[from].classList.replace("on","out");
  beltLis[to].classList.add("on");attrLis[to].classList.add("on");
  cards[to].classList.remove("leave");
  cards[from].classList.remove("is-on","enter");cards[from].classList.add("leave");
  cards[to].classList.add("is-on","enter");
  await wait(1150);
  cards[from].classList.remove("leave");cards[to].classList.remove("enter");
  beltLis[from].classList.add("prep");beltLis[from].classList.remove("out");attrLis[from].classList.add("prep");attrLis[from].classList.remove("out");
  stage.offsetWidth;beltLis[from].classList.remove("prep");attrLis[from].classList.remove("prep");
  busy=false;
};
const go=dir=>show((cur+dir+N)%N,dir);
ticks.forEach((b,k)=>b.addEventListener("click",()=>show(k)));
cards.forEach((c,k)=>{c.addEventListener("click",()=>{if(k===cur)openCase(k)});c.addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&k===cur){e.preventDefault();openCase(k)}})});

const homeActive=()=>!d.body.classList.contains("on-about");
const blocked=()=>!homeActive()||home.classList.contains("is-catalog")||$("dialog[open]")||$("#menu").classList.contains("open");
let acc=0,last=0;
addEventListener("wheel",e=>{if(blocked())return;e.preventDefault();const now=Date.now();if(now-last>220)acc=0;last=now;acc+=e.deltaY;if(Math.abs(acc)>40){go(Math.sign(acc));acc=0}},{passive:false});
let ty=null;
home.addEventListener("touchstart",e=>{ty=e.touches[0].clientY},{passive:true});
home.addEventListener("touchend",e=>{if(ty===null||blocked())return;const dy=ty-e.changedTouches[0].clientY;if(Math.abs(dy)>50)go(dy>0?1:-1);ty=null},{passive:true});
d.addEventListener("keydown",e=>{if(blocked()||/INPUT|TEXTAREA/.test(e.target.tagName))return;
  if(["ArrowDown","PageDown"].includes(e.key)){e.preventDefault();go(1)}
  if(["ArrowUp","PageUp"].includes(e.key)){e.preventDefault();go(-1)}});

/* first load: the intro plays in CSS (see INTRO); scrolling and EXPLORE wait until it has finished */
paint();
cards.filter(c=>!c.classList.contains("is-on")).forEach((c,j)=>c.style.setProperty("--k",j+1));
busy=true;
/* INTRO: every pose below is sampled at 60 Hz from measured motion curves
   (see src/intro_curves.py). Each card gets one continuous WAAPI timeline of transform + opacity,
   which the compositor plays even while the page is still decoding media. */
{const st=$("#stage"),front=st&&st.querySelector(".card.is-on"),D=INTRO,N=D.s.length,dur=(N-1)/D.hz*1000;
 const done=()=>{home.classList.remove("intro","go","lit");anims.forEach(a=>a.cancel());clones.forEach(c=>c.remove());
   [front,...layers].forEach(el=>{if(el){el.style.zIndex="";el.style.willChange="";el.style.transformOrigin=""}})};
 let anims=[],clones=[],layers=[];
 if(front&&home.classList.contains("intro")&&"animate" in front){
  const r=st.getBoundingClientRect(),V=innerHeight,T=r.top,h=r.height,w=r.width,Pp=(w*.48).toFixed(1);
  /* curve units -> this page: its card's final top (154) lands on ours, the bottom edge on the viewport's */
  const mapTop=y=>y<=154?y/154*T:T+(y-154)/(472.5-154)*(V-T);
  const tf=(sc,top,th)=>{const dy=mapTop(top)+sc*h/2-(T+h/2);
    return `perspective(${Pp}px) translateY(${dy.toFixed(2)}px) scale(${sc.toFixed(4)}) translateY(${(h/2).toFixed(1)}px) rotateX(${th}deg) translateY(${(-h/2).toFixed(1)}px)`};
  /* the stack behind: five cards spread between where the small card started and where the front card is */
  const others=cards.filter(c=>c!==front),pool=[...others];
  while(pool.length<5){const k=others[pool.length%others.length].cloneNode(true);k.removeAttribute("id");k.setAttribute("aria-hidden","true");k.tabIndex=-1;st.prepend(k);clones.push(k);pool.push(k)}
  const FS=[0,.198,.433,.712,.877],FT=[0,.126,.382,.698,.887];
  layers=pool.slice(0,5);
  const kf=[],lk=layers.map(()=>[]);
  for(let i=0;i<N;i++){const o=i/(N-1),t=.12+i/D.hz,s=D.s[i],top=D.top[i],c=D.c[i];
    kf.push({offset:o,transform:tf(s,top,D.th[i]),opacity:D.op[i]});
    const as=.6+(s-.6)*c,at=205+(top-205)*c,lo=t<.79?0:t<2.72?1:0;
    layers.forEach((L,j)=>lk[j].push({offset:o,transform:tf(as+(s-as)*FS[j],at+(top-at)*FT[j],0),opacity:lo}))}
  const opt={duration:dur,fill:"both",easing:"linear"};
  [front,...layers].forEach((el,j)=>{el.style.transformOrigin="50% 50%";el.style.willChange="transform,opacity";el.style.zIndex=j?String(4+j):"10"});
  /* start once fonts are in and two frames have painted, so the first second is not spent fighting page load;
     the CSS parts (dim, title, page details) are held paused until the same moment */
  const go=()=>{home.classList.add("go");anims=[front.animate(kf,opt),...layers.map((L,j)=>L.animate(lk[j],opt))];
    setTimeout(()=>home.classList.add("lit"),5000);setTimeout(()=>{busy=false},5250);setTimeout(done,6100)};
  const ready=Promise.race([d.fonts?d.fonts.ready:Promise.resolve(),wait(1200)]);
  ready.then(()=>requestAnimationFrame(()=>requestAnimationFrame(go)));
 }else{setTimeout(()=>{busy=false},50);done()}
}
$$("[data-theme-toggle]").forEach(b=>b.addEventListener("click",()=>setTimeout(paint,0)));
dq.addEventListener("change",paint);

/* ── catalog / card view ── */
const vt=$("#view-toggle");
const setView=cat=>{home.classList.toggle("is-catalog",cat);vt.setAttribute("aria-pressed",cat);vt.querySelectorAll("span").forEach(s=>s.textContent=cat?"Card view":"Catalog view");store.set("view",cat?"catalog":"cards")};
vt.addEventListener("click",()=>setView(!home.classList.contains("is-catalog")));
if(store.get("view")==="catalog")setView(true);

/* ── project page: the title clears, the card lifts and grows, expands to fill the screen,
   holds, dims to dark, then the title rises in followed by the details and the thumbnail rail ── */
let opener=null,io=null;
$$(".case-intro h2").forEach(h=>{const s=d.createElement("span");s.className="rise";s.append(...h.childNodes);h.append(s)});
const openCase=async k=>{
  if(busy)return;busy=true;
  if(k!==cur){cur=k;paint();setInstant(k)}
  opener=d.activeElement;
  const dl=$("#case-"+k),card=cards[k],media=dl.querySelector(".case-media");
  dl.style.setProperty("--pbg",P[k].bg);dl.style.setProperty("--pink",P[k].ink);dl.style.setProperty("--pdeep",isDark()?P[k].night:P[k].deep);
  const fromHome=!calm&&!home.classList.contains("is-catalog");
  if(fromHome){hero.classList.remove("booting");home.classList.add("exploring");card.classList.add("lift");await wait(600)}
  /* the page background starts as a copy of the card, exactly where the card is */
  const clone=card.firstElementChild.cloneNode(true);clone.removeAttribute("aria-label");clone.setAttribute("aria-hidden","true");
  media.replaceChildren(clone);media.classList.remove("anim","full");
  if(fromHome){const r=card.getBoundingClientRect();Object.assign(media.style,{top:r.top+"px",left:r.left+"px",width:r.width+"px",height:r.height+"px",borderRadius:getComputedStyle(card).borderTopLeftRadius})}
  else media.removeAttribute("style");
  dl.classList.remove("shown","closing");dl.classList.toggle("calm",calm);
  dl.showModal();dl.scrollTop=0;if(cursorEl)dl.append(cursorEl);
  dl.querySelector(".case-close").focus({preventScroll:true});
  media.offsetWidth;media.classList.add("anim","full");
  requestAnimationFrame(()=>dl.classList.add("shown"));
  const shots=[...dl.querySelectorAll(".shot")];
  io&&io.disconnect();
  io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add("in")}),{root:dl,threshold:.15});
  shots.forEach(s=>calm?s.classList.add("in"):io.observe(s));
  await wait(1000);
  home.classList.remove("exploring");card.classList.remove("lift");
  busy=false;
};
const closeCase=async dl=>{dl.classList.add("closing");await wait(450);dl.close()};
$$("[data-open]").forEach(b=>b.addEventListener("click",()=>openCase(+b.dataset.open)));
$$("dialog.case").forEach(dl=>{
  dl.querySelector(".case-close").addEventListener("click",()=>closeCase(dl));
  dl.addEventListener("cancel",e=>{e.preventDefault();closeCase(dl)});
  dl.addEventListener("close",()=>{dl.classList.remove("shown","closing");dl.querySelector(".case-media").replaceChildren();if(cursorEl)d.body.append(cursorEl);if(opener&&opener.isConnected)opener.focus({preventScroll:true})});
  /* thumbnails copy their image from the clip they point to, so nothing is stored twice */
  const targets=[dl.querySelector(".case-intro"),...dl.querySelectorAll(".shot")],rb=[...dl.querySelectorAll(".rail button")];
  rb.forEach((b,i)=>{const img=b.querySelector("img"),src=targets[i]&&targets[i].querySelector(".frame img");if(img&&src)img.src=src.getAttribute("src");
    b.addEventListener("click",()=>targets[i].scrollIntoView({behavior:calm?"auto":"smooth",block:"center"}))});
  dl.addEventListener("scroll",()=>{const mid=dl.scrollTop+innerHeight/2;let a=0;targets.forEach((t,i)=>{if(t.offsetTop<=mid)a=i});rb.forEach((b,i)=>b.setAttribute("aria-current",i===a))},{passive:true});
  const nx=dl.querySelector("[data-next]");if(nx)nx.addEventListener("click",async()=>{await closeCase(dl);const k=+nx.dataset.next;await show(k,1);openCase(k)});
});

/* ── stack filter ── */
const fBtns=$$(".st-filter button"),fItems=$$(".st-groups li");
fBtns.forEach(b=>b.addEventListener("click",()=>{const f=b.dataset.f;let n=0;
  fBtns.forEach(o=>o.setAttribute("aria-pressed",o===b));
  fItems.forEach(li=>{const on=!f||li.dataset.p.split(" ").includes(f);li.classList.toggle("dim",!on);if(on)n++});
  $("#st-count").textContent=f?`${n} of ${fItems.length} tools`:`${fItems.length} tools`}));

/* ── logo: size the Arabic name so it runs exactly as wide as LUJAIN ALOUFI ── */
/* Arabic name: same type size as the English line, widened with kashida (tatweel) at the
   letters that join forward, round-robin across both words, until it runs as wide as the English */
const AR_S=[[0,1,2],[1,2,4]],AR_N=[["ل","ج","ي","ن"],["ا","ل","ع","و","ف","ي"]];
const kash=c=>AR_N.map((wd,i)=>wd.map((ch,j)=>{const k=AR_S[i].indexOf(j);return ch+(k<0?"":"\u0640".repeat(c[i][k]))}).join("")).join(" ");
const fitOne=l=>{const en=l&&l.querySelector(".en span"),ar=l&&l.querySelector(".ar");if(!en||!ar)return;
  const w=en.getBoundingClientRect().width;if(!w)return;const sps=ar.querySelectorAll("span"),sp=sps[0];
  ar.style.transform="";ar.style.fontSize=(parseFloat(getComputedStyle(en.parentNode).fontSize)*1.1).toFixed(2)+"px";
  const c=[[0,0,0],[0,0,0]],order=[[0,1],[1,1],[0,0],[1,2],[0,2],[1,0]];
  const set=()=>{const t=kash(c);sps.forEach(x=>x.textContent=t)};set();
  for(let n=0;n<80;n++){const [i,k]=order[n%order.length];c[i][k]++;set();
    if(sp.getBoundingClientRect().width>w){c[i][k]--;set();break}}
  /* tatweel comes in whole glyphs, so close the last few pixels with a tiny horizontal stretch */
  const aw=sp.getBoundingClientRect().width;if(aw)ar.style.transform=`scaleX(${Math.min(w/aw,1.25).toFixed(4)})`};
const fitAll=()=>$$(".logo").forEach(fitOne);
if("ResizeObserver" in window){const ro=new ResizeObserver(es=>es.forEach(e=>fitOne(e.target.closest(".logo"))));$$(".logo .en span").forEach(sp=>ro.observe(sp))}
addEventListener("resize",fitAll);fitAll();
/* the Arabic face loads only when first used, so fit again once it arrives */
if(d.fonts){d.fonts.ready.then(fitAll);d.fonts.addEventListener("loadingdone",fitAll);d.fonts.load('500 16px "IBM Plex Sans Arabic"',"لجين العوفي").then(fitAll).catch(()=>{})}


/* footer wordmark: size the name so it spans the footer width exactly, then lift it in on view */
{const g=$(".f-giant"),gs=g&&g.querySelector("span");
 if(g&&gs){const fit=()=>{const w=g.clientWidth;if(!w)return;g.style.fontSize="100px";const n=gs.scrollWidth;if(n)g.style.fontSize=(100*w/n*.995).toFixed(2)+"px"};
  fit();addEventListener("resize",fit);if(d.fonts)d.fonts.ready.then(fit);
  if("IntersectionObserver" in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){fit();g.classList.add("in")}}),{threshold:.2});io.observe(g);
   /* the floating BACK TO TOP steps aside once the wordmark shows; the footer bar carries its own link */
   const tt=$("#to-top");if(tt){new IntersectionObserver(es=>es.forEach(e=>document.body.classList.toggle("at-foot",e.isIntersecting)),{threshold:.05}).observe(g)}
   $$(".f-top").forEach(a=>a.addEventListener("click",e=>{e.preventDefault();scrollTo({top:0,behavior:"smooth"})}))
  }else g.classList.add("in")}}
