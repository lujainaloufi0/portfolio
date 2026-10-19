"""Builds mizan/index.html: a single-file landing page for Mizan.

The phone screens come from mizan_scenes.py, so the landing page and the portfolio show the same UI.
Layout uses Tailwind from its CDN; the phone frame and scene styles are inlined from tawaqaa.css and mizan.css.
Run through build.py, or on its own: python3 src/mizan_landing.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import mizan_scenes as MZ

GITHUB = 'https://github.com/lujainaloufi0/Mizan'
LINKEDIN = 'https://www.linkedin.com/in/lujain-aloufi/'


def phone_css():
    css = open(os.path.join(os.path.dirname(__file__), 'tawaqaa.css')).read()
    # whole rules whose selector starts with the phone frame classes (.iph, .scr, .sb)
    keep = re.findall(r'(?m)^\.(?:iph|scr|sb)\b[^{]*\{[^}]*\}', css)
    return '\n'.join(keep) + '\n' + open(os.path.join(os.path.dirname(__file__), 'mizan.css')).read()


def stage(inner, cls=''):
    return f'<div class="relative {cls}"><div class="mz">{inner}</div></div>'


FEATURES = [
    ('plan', 'Plan', 'A week that fits the budget',
     'Pick your cuisines, your supermarkets, the size of your household and a weekly budget in riyals. '
     'The scale weighs the expected basket against the budget while you move the slider.',
     ['18 cuisines, or a mix', 'Carrefour, Panda, Othaim, Danube, Tamimi and LuLu', 'Cooking days, meals per day and leftovers'],
     f'{MZ.FL_CUISINE}{MZ.wizard(lg=True)}{MZ.FL_BUDGET}'),
    ('swap', 'Swap', 'Change any meal in one tap',
     'Every meal can be swapped. The three quick options are ranked by what your basket already covers, '
     'and each one shows how the basket price changes.',
     ['Filtered by allergies and appliances', 'Ban a dish and it never comes back', 'Goals: balanced, high protein, cutting or bulking'],
     f'{MZ.swap()}{MZ.FL_SWAP}'),
    ('shop', 'Shop', 'A list sorted the way you walk the store',
     'The grocery list is grouped by aisle and can split by store. Ticked items move into "في مطبخي", '
     'the kitchen view, and cooked meals take their ingredients out of it.',
     ['Copy the list, sorted by aisle', 'Send it to HungerStation, Nana, Ninja, Keeta, ToYou, Jahez or Mrsool', 'Leftovers count toward next week'],
     f'{MZ.FL_AISLE}{MZ.grocery()}'),
]

GALLERY = [
    ('Today', "Today's meals and the week's basket", MZ.home()),
    ('Week', 'Every meal with time, calories and protein', MZ.week()),
    ('Deliver', 'Send the list to a delivery app', MZ.delivery()),
    ('Profile', 'Asked once, saved on the phone', MZ.profile()),
    ('Light', 'The same screens in the light theme', MZ.home(light=True, cook=False)),
]

BENTO = [
    ('lg:col-span-2', 'Arabic first', 'The whole app is written in Arabic and laid out right to left, with Thmanyah type on an 8pt grid.', 'مِيزان'),
    ('', 'No account', 'Your profile and plans are saved on the phone. Nothing is sent to a server.', None),
    ('', 'Works offline', 'Planning, swapping and the grocery list all run on the device.', None),
    ('', '163 halal recipes', 'Across 18 cuisines and about 128 ingredients, each with macros and a cost per serving in riyals.', None),
    ('lg:col-span-2', 'Stays on budget', 'When the week runs over, the planner swaps in cheaper meals in stages, keeping to your chosen cuisines first.', None),
    ('', 'Light and dark', 'Automatic, light or dark, set from the profile.', None),
    ('', 'Calm motion', 'Fades between 120 and 260 ms with an ease-out. Nothing slides or bounces.', None),
    ('', '21 tests', 'Jest tests cover the catalog, the planner rules and full flows on Android.', None),
]

STEPS = [
    ('01', 'Filter', 'Recipes that clash with your allergies, appliances, goal or banned dishes are removed first.'),
    ('02', 'Shuffle', 'A seeded shuffle picks the week, so two weeks rarely look the same.'),
    ('03', 'Balance', 'If the basket runs over budget, cheaper meals replace expensive ones in stages.'),
    ('04', 'Shop', 'Ingredients are priced per pack and grouped by aisle and store.'),
]


def page():
    tabs = ''.join(f'<button type="button" role="tab" data-tab="{k}" aria-selected="{"true" if i == 0 else "false"}" class="tab relative px-5 py-2.5 rounded-full text-sm font-semibold transition-colors">{lbl}<span class="tab-bar"></span></button>'
                   for i, (k, lbl, *_ ) in enumerate(FEATURES))
    panels = ''
    stages = ''
    for i, (k, lbl, h, p, pts, sc) in enumerate(FEATURES):
        li = ''.join(f'<li class="flex gap-3"><span class="mt-2 h-1.5 w-1.5 flex-none rounded-full bg-[#10B981]"></span><span>{x}</span></li>' for x in pts)
        panels += f'''<div class="panel{" on" if i == 0 else ""}" data-panel="{k}" role="tabpanel">
          <h3 class="text-3xl md:text-4xl font-semibold tracking-tight text-[#F4EFE8]">{h}</h3>
          <p class="mt-4 text-lg leading-relaxed text-[#B9B3AA]">{p}</p>
          <ul class="mt-6 space-y-3 text-[#D9D3CA]">{li}</ul></div>'''
        stages += f'<div class="tstage{" on" if i == 0 else ""}" data-stage="{k}"><div class="mz">{sc}</div></div>'
    gal = ''.join(f'''<figure class="gcard reveal snap-center flex-none w-[260px] md:w-[300px]">
        <div class="glow-border relative aspect-[9/16.5] rounded-[28px] overflow-hidden"><div class="mz solo">{s}</div></div>
        <figcaption class="mt-4"><span class="text-xs font-semibold tracking-[.18em] uppercase text-[#6EE7B7]">{t}</span><p class="mt-1 text-[#B9B3AA]">{c}</p></figcaption></figure>''' for t, c, s in GALLERY)
    bento = ''.join(f'''<div class="bento reveal {span} rounded-3xl p-7 md:p-8 flex flex-col justify-between min-h-[220px]">
        {f'<span class="ar text-6xl md:text-7xl font-bold text-[#E5D4C0] leading-none" lang="ar">{big}</span>' if big else '<span class="dot"></span>'}
        <div class="mt-8"><h3 class="text-xl font-semibold text-[#F4EFE8]">{t}</h3><p class="mt-2 text-[#B9B3AA] leading-relaxed">{d}</p></div></div>''' for span, t, d, big in BENTO)
    steps = ''.join(f'''<div class="step reveal rounded-3xl p-7"><span class="font-mono text-sm text-[#6EE7B7]">{n}</span>
        <h3 class="mt-6 text-2xl font-semibold text-[#F4EFE8]">{t}</h3><p class="mt-3 text-[#B9B3AA] leading-relaxed">{d}</p></div>''' for n, t, d in STEPS)
    mark = MZ.MARK.replace('class="z-mark"', 'class="h-8 w-8" style="--z-sand:#E5D4C0;--z-mint:#10B981"')
    facts = [('163', 'halal recipes'), ('18', 'cuisines'), ('6', 'supermarkets'), ('7', 'delivery apps')]
    fact_html = ''.join(f'<div><dt class="text-3xl md:text-4xl font-semibold text-[#F4EFE8] tabular-nums">{n}</dt><dd class="mt-1 text-sm text-[#8F8A82]">{l}</dd></div>' for n, l in facts)
    return f'''<!doctype html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mizan · Meal planning and grocery budget</title>
<meta name="description" content="Mizan plans a Saudi household's week of meals, builds the grocery list by aisle and store, and keeps the basket inside a weekly budget in riyals. An Android app by Lujain Aloufi.">
<meta name="theme-color" content="#0B0C0E">
<meta property="og:title" content="Mizan · Meal planning and grocery budget">
<meta property="og:description" content="An Arabic-first Android app that plans the week's meals and keeps the shopping inside a budget.">
<meta property="og:image" content="https://lujainaloufi0.github.io/portfolio/assets/og-image.png">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1024 1024'%3E%3Crect width='1024' height='1024' rx='226' fill='%23121417'/%3E%3Ccircle cx='512' cy='680' r='44' fill='%2310B981'/%3E%3Cpath d='M230 400C230 330 310 310 360 360C410 410 390 490 310 510C250 530 230 460 230 400Z' fill='%23E5D4C0'/%3E%3Cpath d='M320 460C420 640 680 640 794 400' fill='none' stroke='%23E5D4C0' stroke-width='52' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
<script src="https://cdn.tailwindcss.com/3.4.17"></script>
<style>
:root{{--f-ar:"IBM Plex Sans Arabic",Tahoma,sans-serif;--f-body:"Outfit",system-ui,sans-serif;--ease:cubic-bezier(.77,0,.18,1);--out:cubic-bezier(.16,1,.3,1)}}
html{{background:#0A0A0C}}
body{{font-family:var(--f-body);background:#0A0A0C;color:#F4EFE8;-webkit-font-smoothing:antialiased}}
.ar{{font-family:var(--f-ar)}}
h1,h2,h3{{text-wrap:balance}} p{{text-wrap:pretty}}
::selection{{background:#10B981;color:#0A0A0C}}
{phone_css()}
.mz.solo .z-ph{{height:96cqh}}
.mz .z-fl{{width:min(30cqw,40cqh)}}
#hero-stage .z-fl{{position:absolute;margin:0;width:min(44cqw,40cqh)}}
#hero-stage .z-fl:first-child{{left:3%;top:13%}}
#hero-stage .z-fl:last-child{{right:3%;bottom:8%;width:min(46cqw,44cqh)}}
.glass{{background:rgba(24,24,28,.6);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);border:1px solid rgba(229,212,192,.1)}}
.glow-border{{box-shadow:0 0 0 1px rgba(229,212,192,.1),0 30px 80px -30px rgba(0,0,0,.8),0 0 60px -20px rgba(16,185,129,.25)}}
.btn{{transition:transform .2s cubic-bezier(.23,1,.32,1),box-shadow .2s,background-color .2s}}
.btn:active{{transform:scale(.97)}}
.btn-mint{{background:#10B981;color:#0A0A0C;box-shadow:0 10px 30px -10px rgba(16,185,129,.6)}}
.btn-ghost{{border:1px solid rgba(229,212,192,.2);color:#F4EFE8}}
@media (hover:hover) and (pointer:fine){{
  .btn-mint:hover{{box-shadow:0 14px 40px -10px rgba(16,185,129,.8)}}
  .btn-ghost:hover{{background:rgba(229,212,192,.06)}}
  .bento:hover,.step:hover,.gcard:hover .glow-border{{transform:translateY(-4px);border-color:rgba(16,185,129,.35)}}
  .gcard:hover .glow-border{{box-shadow:0 0 0 1px rgba(16,185,129,.4),0 40px 90px -30px rgba(0,0,0,.85),0 0 70px -15px rgba(16,185,129,.4)}}
}}
.bento,.step{{background:linear-gradient(160deg,#18181C,#121216);border:1px solid rgba(229,212,192,.08);transition:transform .3s cubic-bezier(.23,1,.32,1),border-color .3s}}
.gcard .glow-border{{transition:transform .3s cubic-bezier(.23,1,.32,1),box-shadow .3s}}
.dot{{width:10px;height:10px;border-radius:50%;background:#10B981;box-shadow:0 0 0 6px rgba(16,185,129,.14)}}
.reveal{{opacity:0;transform:translateY(16px);transition:opacity .7s cubic-bezier(.23,1,.32,1),transform .7s cubic-bezier(.23,1,.32,1);transition-delay:var(--d,0s)}}
.reveal.in{{opacity:1;transform:none}}
.tab{{color:#B9B3AA}}
.tab[aria-selected="true"]{{background:#F4EFE8;color:#0A0A0C}}
.tab-bar{{position:absolute;left:18px;right:18px;bottom:5px;height:2px;border-radius:2px;background:#10B981;transform:scaleX(0);transform-origin:0 50%}}
.tab[aria-selected="true"] .tab-bar{{background:#0A0A0C;opacity:.25;animation:tabbar 7s linear forwards}}
@keyframes tabbar{{to{{transform:scaleX(1)}}}}
.panel{{display:none}} .panel.on{{display:block;animation:fadein .5s cubic-bezier(.23,1,.32,1)}}
.tstage{{position:absolute;inset:0;opacity:0;transition:opacity .5s cubic-bezier(.23,1,.32,1);pointer-events:none}}
.tstage.on{{opacity:1}}
@keyframes fadein{{from{{opacity:0}}}}
.hero-glow{{background:radial-gradient(50% 50% at 50% 50%,rgba(16,185,129,.35),transparent 70%)}}
.noise::after{{content:"";position:absolute;inset:0;pointer-events:none;opacity:.05;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.8' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
#gallery::-webkit-scrollbar{{display:none}}
</style>
</head>
<body class="overflow-x-hidden">

<header class="fixed inset-x-0 top-0 z-50">
  <nav class="glass mx-4 mt-4 md:mx-auto md:max-w-5xl rounded-full flex items-center justify-between pl-4 pr-2 py-2">
    <a href="#top" class="flex items-center gap-2.5" aria-label="Mizan, back to top">{mark}<span class="font-semibold tracking-tight">Mizan</span><span class="ar text-[#8F806E]" lang="ar">مِيزان</span></a>
    <div class="hidden md:flex items-center gap-7 text-sm text-[#B9B3AA]"><a class="hover:text-[#F4EFE8] transition-colors" href="#features">Features</a><a class="hover:text-[#F4EFE8] transition-colors" href="#screens">Screens</a><a class="hover:text-[#F4EFE8] transition-colors" href="#planner">How it plans</a></div>
    <a href="{GITHUB}" target="_blank" rel="noopener" class="btn btn-mint rounded-full px-4 py-2 text-sm font-semibold">GitHub</a>
  </nav>
</header>

<main id="top">
  <!-- hero -->
  <section class="noise relative overflow-hidden pt-36 md:pt-40 pb-20 md:pb-28">
    <div class="hero-glow absolute -right-40 top-20 h-[640px] w-[640px] blur-3xl opacity-60 pointer-events-none"></div>
    <div class="absolute -left-40 -top-20 h-[520px] w-[520px] rounded-full blur-3xl opacity-40 pointer-events-none" style="background:radial-gradient(closest-side,rgba(229,212,192,.25),transparent)"></div>
    <div class="relative mx-auto max-w-6xl px-4 md:px-6 grid lg:grid-cols-[1.05fr_1fr] gap-14 items-center">
      <div>
        <p class="reveal inline-flex items-center gap-2 rounded-full glass px-3.5 py-1.5 text-xs font-medium tracking-wide text-[#D9D3CA]"><span class="dot !w-2 !h-2"></span>Android app · Arabic first</p>
        <h1 class="reveal mt-6 text-5xl sm:text-6xl lg:text-7xl font-semibold tracking-[-0.035em] leading-[1.02]" style="--d:.08s">Smart nutrition,<br><span class="text-[#E5D4C0]">absolute balance.</span></h1>
        <p class="reveal mt-6 max-w-xl text-lg md:text-xl leading-relaxed text-[#B9B3AA] font-light" style="--d:.16s">Mizan plans your family's week of meals, builds the grocery list by aisle and store, and keeps the basket inside your weekly budget in riyals.</p>
        <div class="reveal mt-9 flex flex-wrap gap-3" style="--d:.24s">
          <a href="{GITHUB}" target="_blank" rel="noopener" class="btn btn-mint rounded-full px-6 py-3.5 font-semibold">View the code on GitHub</a>
          <a href="../" class="btn btn-ghost rounded-full px-6 py-3.5 font-semibold">More of my work</a>
        </div>
        <dl class="reveal mt-12 grid grid-cols-4 gap-4 max-w-lg border-t border-white/10 pt-6" style="--d:.32s">{fact_html}</dl>
      </div>
      <div class="reveal relative h-[560px] md:h-[640px]" id="hero-stage" style="--d:.1s">
        <div class="absolute inset-0 rounded-[40px] overflow-hidden glow-border" id="hero-tilt" style="transition:transform .6s cubic-bezier(.23,1,.32,1)"><div class="mz">{MZ.FL_COOKED}{MZ.home()}{MZ.FL_BASKET}</div></div>
      </div>
    </div>
  </section>

  <!-- features -->
  <section id="features" class="relative py-20 md:py-28">
    <div class="mx-auto max-w-6xl px-4 md:px-6">
      <p class="reveal text-xs font-semibold tracking-[.2em] uppercase text-[#6EE7B7]">What it does</p>
      <h2 class="reveal mt-3 text-4xl md:text-5xl font-semibold tracking-tight max-w-2xl">Plan the week, swap what you don't want, shop once.</h2>
      <div class="reveal mt-10 inline-flex gap-1 rounded-full glass p-1.5" role="tablist" aria-label="Features">{tabs}</div>
      <div class="mt-10 grid lg:grid-cols-[1fr_1.15fr] gap-10 lg:gap-16 items-center">
        <div class="reveal min-h-[300px]">{panels}</div>
        <div class="reveal relative aspect-[16/12] rounded-[36px] overflow-hidden glow-border">{stages}</div>
      </div>
    </div>
  </section>

  <!-- gallery -->
  <section id="screens" class="relative py-20 md:py-28 overflow-hidden">
    <div class="mx-auto max-w-6xl px-4 md:px-6 flex items-end justify-between gap-6">
      <div><p class="reveal text-xs font-semibold tracking-[.2em] uppercase text-[#6EE7B7]">Screens</p>
        <h2 class="reveal mt-3 text-4xl md:text-5xl font-semibold tracking-tight">Mizan in action</h2></div>
      <div class="hidden md:flex gap-2"><button type="button" class="btn btn-ghost h-11 w-11 rounded-full" data-scroll="-1" aria-label="Previous screens">←</button><button type="button" class="btn btn-ghost h-11 w-11 rounded-full" data-scroll="1" aria-label="Next screens">→</button></div>
    </div>
    <div id="gallery" class="mt-12 flex gap-6 overflow-x-auto snap-x snap-mandatory px-4 md:px-[max(1.5rem,calc((100vw-72rem)/2+1.5rem))] pb-6 cursor-grab" style="scrollbar-width:none">{gal}</div>
  </section>

  <!-- bento -->
  <section class="py-20 md:py-28">
    <div class="mx-auto max-w-6xl px-4 md:px-6">
      <p class="reveal text-xs font-semibold tracking-[.2em] uppercase text-[#6EE7B7]">Details</p>
      <h2 class="reveal mt-3 text-4xl md:text-5xl font-semibold tracking-tight max-w-2xl">Built for Saudi kitchens and Saudi prices.</h2>
      <div class="mt-12 grid sm:grid-cols-2 lg:grid-cols-4 gap-4">{bento}</div>
    </div>
  </section>

  <!-- planner -->
  <section id="planner" class="py-20 md:py-28">
    <div class="mx-auto max-w-6xl px-4 md:px-6">
      <p class="reveal text-xs font-semibold tracking-[.2em] uppercase text-[#6EE7B7]">How it plans</p>
      <h2 class="reveal mt-3 text-4xl md:text-5xl font-semibold tracking-tight max-w-2xl">Four steps, all on the phone.</h2>
      <div class="mt-12 grid sm:grid-cols-2 lg:grid-cols-4 gap-4">{steps}</div>
    </div>
  </section>

  <!-- closing -->
  <section class="py-20 md:py-28">
    <div class="reveal noise relative mx-4 md:mx-auto md:max-w-6xl overflow-hidden rounded-[40px] px-6 py-16 md:p-20 text-center glow-border" style="background:radial-gradient(70% 90% at 50% 120%,rgba(16,185,129,.35),transparent 70%),#121216">
      <p class="ar text-[#E5D4C0] text-2xl" lang="ar" dir="rtl">وش نطبخ اليوم؟</p>
      <h2 class="mt-4 text-4xl md:text-6xl font-semibold tracking-tight">The week, planned and priced.</h2>
      <p class="mt-5 text-lg text-[#B9B3AA] max-w-xl mx-auto">Mizan is an Android app built with Expo and React Native. The code is on GitHub.</p>
      <div class="mt-9 flex flex-wrap justify-center gap-3"><a href="{GITHUB}" target="_blank" rel="noopener" class="btn btn-mint rounded-full px-6 py-3.5 font-semibold">View on GitHub</a><a href="../" class="btn btn-ghost rounded-full px-6 py-3.5 font-semibold">Back to the portfolio</a></div>
    </div>
  </section>
</main>

<footer class="border-t border-white/10 py-12">
  <div class="mx-auto max-w-6xl px-4 md:px-6 grid md:grid-cols-[1.4fr_1fr_1fr] gap-10">
    <div><a href="#top" class="flex items-center gap-2.5">{mark}<span class="font-semibold">Mizan</span><span class="ar text-[#8F806E]" lang="ar">مِيزان</span></a>
      <p class="mt-4 max-w-sm text-[#8F8A82] leading-relaxed">A meal-planning, pantry and grocery-budget app for Saudi households. Designed and built by Lujain Aloufi.</p></div>
    <div><p class="text-xs font-semibold tracking-[.18em] uppercase text-[#6EE7B7]">On this page</p>
      <ul class="mt-4 space-y-2 text-[#B9B3AA]"><li><a class="hover:text-[#F4EFE8]" href="#features">Features</a></li><li><a class="hover:text-[#F4EFE8]" href="#screens">Screens</a></li><li><a class="hover:text-[#F4EFE8]" href="#planner">How it plans</a></li></ul></div>
    <div><p class="text-xs font-semibold tracking-[.18em] uppercase text-[#6EE7B7]">Elsewhere</p>
      <ul class="mt-4 space-y-2 text-[#B9B3AA]"><li><a class="hover:text-[#F4EFE8]" href="{GITHUB}" target="_blank" rel="noopener">GitHub ↗</a></li><li><a class="hover:text-[#F4EFE8]" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a></li><li><a class="hover:text-[#F4EFE8]" href="../">Portfolio</a></li></ul></div>
  </div>
  <p class="mx-auto max-w-6xl px-4 md:px-6 mt-12 text-sm text-[#6B675F]">© 2026 Lujain Aloufi. Prices in the screens are sample data.</p>
</footer>

<script>
(()=>{{
  const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add("in");io.unobserve(e.target)}}}}),{{threshold:.12}});
  document.querySelectorAll(".reveal").forEach(el=>io.observe(el));
  // feature tabs: click to switch, advance every 7s while visible
  const tabs=[...document.querySelectorAll("[data-tab]")];let at=0,timer=0;
  const show=k=>{{at=k;tabs.forEach((t,i)=>{{t.setAttribute("aria-selected",i===k);const b=t.querySelector(".tab-bar");b.style.animation="none";b.offsetWidth;b.style.animation=""}});
    const id=tabs[k].dataset.tab;document.querySelectorAll("[data-panel]").forEach(p=>p.classList.toggle("on",p.dataset.panel===id));
    document.querySelectorAll("[data-stage]").forEach(s=>s.classList.toggle("on",s.dataset.stage===id));
    clearTimeout(timer);timer=setTimeout(()=>show((at+1)%tabs.length),7000)}};
  tabs.forEach((t,i)=>t.addEventListener("click",()=>show(i)));
  new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting)show(at);else clearTimeout(timer)}}),{{threshold:.3}}).observe(document.getElementById("features"));
  // gallery: buttons and drag
  const g=document.getElementById("gallery");
  document.querySelectorAll("[data-scroll]").forEach(b=>b.addEventListener("click",()=>g.scrollBy({{left:+b.dataset.scroll*330,behavior:"smooth"}})));
  let down=false,sx=0,sl=0;
  g.addEventListener("pointerdown",e=>{{if(e.pointerType!=="mouse")return;down=true;sx=e.clientX;sl=g.scrollLeft;g.style.scrollSnapType="none";g.style.cursor="grabbing"}});
  addEventListener("pointerup",()=>{{if(!down)return;down=false;g.style.scrollSnapType="";g.style.cursor=""}});
  addEventListener("pointermove",e=>{{if(down)g.scrollLeft=sl-(e.clientX-sx)}});
  // hero: a slight tilt toward the pointer
  const st=document.getElementById("hero-stage"),tl=document.getElementById("hero-tilt");
  if(matchMedia("(hover:hover) and (pointer:fine)").matches){{
    st.addEventListener("pointermove",e=>{{const r=st.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;tl.style.transform=`perspective(1200px) rotateY(${{x*5}}deg) rotateX(${{-y*5}}deg)`}});
    st.addEventListener("pointerleave",()=>tl.style.transform="")}}
}})();
</script>
</body>
</html>
'''


def write(root='.'):
    os.makedirs(os.path.join(root, 'mizan'), exist_ok=True)
    out = os.path.join(root, 'mizan', 'index.html')
    open(out, 'w').write(page())
    return out


if __name__ == '__main__':
    print(write())
