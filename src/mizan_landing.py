"""Builds mizan/index.html: a single-file landing page for Mizan.

The phone screens come from mizan_scenes.py, so the landing page and the portfolio show the same UI.
Plain HTML, CSS and a little JavaScript; the phone frame and scene styles are inlined from tawaqaa.css
and mizan.css. Run through build.py, or on its own: python3 src/mizan_landing.py

Design: Apple product-page language in Mizan's own palette (obsidian #121417, sand, mint). One
authored load moment (the hero phones), one scroll story (a pinned phone that changes screen), one
user-driven toggle (light and dark). Everything else stays still.
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


def device(screen, cls=''):
    """A bare phone: the scene's iPhone frame with no stage behind it."""
    return f'<div class="device {cls}"><div class="mz bare">{screen}</div></div>'


CHEVRON = '<svg viewBox="0 0 8 14" aria-hidden="true"><path d="M1 1l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_UP = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 9l6-6M4 3h5v5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

STORY = [
    ('plan', 'Start with a budget.',
     'Pick your cuisines, your supermarkets and how many people you cook for. As you move the slider, '
     'the scale weighs the expected basket against what you want to spend.', MZ.wizard()),
    ('today', 'Today, at a glance.',
     "Home opens on what to cook today and where the week's basket stands. Mark a meal as cooked and its "
     'ingredients come out of the kitchen.', MZ.home()),
    ('swap', "Don't fancy it? Swap it.",
     "Any meal can be swapped. The quick options come from what's already in your basket, and each one "
     'shows how the price changes.', MZ.swap()),
    ('shop', 'One list, in aisle order.',
     'The grocery list follows the aisles and can split by supermarket. Copy it, or send it to '
     'HungerStation, Jahez, Nana or four other delivery apps.', MZ.grocery()),
]

DETAILS = [
    ('Arabic first', 'Written in Arabic and laid out right to left, on an 8pt grid.'),
    ('No account', 'Your profile and plans stay on your phone. Nothing goes to a server.'),
    ('Works offline', 'Planning, swaps and the grocery list all run on the device.'),
    ('Halal catalog', '163 recipes across 18 cuisines, each with macros and a price per serving.'),
    ('Saudi supermarkets', 'Carrefour, Panda, Othaim, Danube, Tamimi and LuLu.'),
    ('Tested', '21 Jest tests cover the catalog, the planner rules and full flows on Android.'),
]


def page():
    mark = MZ.MARK.replace('class="z-mark"', 'class="logo-mark" style="--z-sand:#E5D4C0;--z-mint:#10B981"')
    story_text = ''.join(
        f'<article class="step{" on" if i == 0 else ""}" data-step="{i}"><h3>{h}</h3><p>{p}</p>'
        f'<div class="step-device">{device(sc)}</div></article>'
        for i, (k, h, p, sc) in enumerate(STORY))
    story_phones = ''.join(f'<div class="layer{" on" if i == 0 else ""}" data-layer="{i}">{device(sc)}</div>' for i, (k, h, p, sc) in enumerate(STORY))
    details = ''.join(f'<div class="spec"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in DETAILS)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Mizan · Meal planning and grocery budget</title>
<meta name="description" content="Mizan plans a Saudi household's week of meals, builds the grocery list by aisle and store, and keeps the basket inside a weekly budget in riyals. An Android app by Lujain Aloufi.">
<meta name="theme-color" content="#121417">
<meta name="color-scheme" content="dark">
<meta property="og:title" content="Mizan · Meal planning and grocery budget">
<meta property="og:description" content="An Arabic-first Android app that plans the week's meals and keeps the shopping inside a budget.">
<meta property="og:image" content="https://lujainaloufi0.github.io/portfolio/assets/og-image.png">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1024 1024'%3E%3Crect width='1024' height='1024' rx='226' fill='%23121417'/%3E%3Ccircle cx='512' cy='680' r='44' fill='%2310B981'/%3E%3Cpath d='M230 400C230 330 310 310 360 360C410 410 390 490 310 510C250 530 230 460 230 400Z' fill='%23E5D4C0'/%3E%3Cpath d='M320 460C420 640 680 640 794 400' fill='none' stroke='%23E5D4C0' stroke-width='52' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
<style>
:root{{
  --bg:#121417;--raise:#1A1D22;--line:rgba(244,239,232,.09);
  --ink:#F4EFE8;--ink-2:#B9B3AA;--ink-3:#8E897F;--sand:#E5D4C0;--mint:#10B981;--mint-ink:#6EE7B7;
  --f-sans:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Segoe UI Variable Display","Segoe UI",system-ui,"Helvetica Neue",Arial,sans-serif;
  --f-ar:"IBM Plex Sans Arabic","SF Arabic","Geeza Pro",Tahoma,sans-serif;--f-body:var(--f-sans);
  --ease:cubic-bezier(.77,0,.175,1);--out:cubic-bezier(.23,1,.32,1);--spring:cubic-bezier(.32,1.18,.52,1);
  --gutter:clamp(20px,5vw,72px);--max:1180px}}
*{{box-sizing:border-box}}
html{{background:var(--bg);color-scheme:dark;-webkit-text-size-adjust:100%;scrollbar-color:#2C3038 var(--bg)}}
body{{margin:0;font:400 17px/1.47 var(--f-sans);color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased;caret-color:var(--mint);overflow-x:clip}}
::selection{{background:rgba(16,185,129,.35);color:var(--ink)}}
a{{color:inherit;text-decoration:none}}
:focus-visible{{outline:2px solid var(--mint-ink);outline-offset:3px;border-radius:6px}}
h1,h2,h3{{margin:0;text-wrap:balance;font-weight:600}}
p{{margin:0;text-wrap:pretty}}
.ar{{font-family:var(--f-ar)}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 var(--gutter)}}
.skip{{position:absolute;left:-999px;top:12px;z-index:100;background:var(--ink);color:var(--bg);padding:8px 14px;border-radius:8px}}
.skip:focus{{left:12px}}

/* scene styles from the app mockups */
{phone_css()}
.mz.bare{{background:none;position:absolute;inset:0;overflow:visible}}
.mz.bare::before,.mz.bare::after{{display:none}}
.mz.bare .z-ph{{height:97cqh;box-shadow:0 0 0 .3cqh #f3f4f6,0 0 0 .6cqh #b4b8be,0 0 0 .78cqh #70747a,0 0 0 .9cqh #2b2d30,0 3cqh 7cqh -1cqh rgba(0,0,0,.55)}}
.device{{position:relative;aspect-ratio:9/19.3;width:var(--w,300px);container-type:size}}

/* nav: the one translucent layer, content scrolls under it */
.nav{{position:fixed;inset:0 0 auto;z-index:50;height:56px;display:flex;align-items:center;
  background:rgba(18,20,23,.72);-webkit-backdrop-filter:saturate(180%) blur(20px);backdrop-filter:saturate(180%) blur(20px);
  border-bottom:1px solid transparent;transition:border-color .3s ease}}
.nav.scrolled{{border-bottom-color:var(--line)}}
.nav .wrap{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:24px}}
.brand{{display:flex;align-items:center;gap:10px;font-weight:600;letter-spacing:-.01em}}
.brand .ar{{color:var(--ink-3);font-weight:500}}
.logo-mark{{width:26px;height:26px}}
.nav-links{{display:flex;align-items:center;gap:28px;font-size:13px;color:var(--ink-2)}}
.nav-links a{{transition:color .2s ease}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:44px;padding:0 22px;border-radius:999px;font:500 17px/1 var(--f-sans);letter-spacing:-.01em;
  transition:transform .16s var(--out),background-color .2s ease,color .2s ease;-webkit-tap-highlight-color:transparent}}
.btn:active{{transform:scale(.97)}}
.btn-mint{{background:var(--mint);color:#0D1A14}}
.btn-sm{{height:30px;padding:0 14px;font-size:13px}}
.link{{display:inline-flex;align-items:center;gap:6px;color:var(--mint-ink);font-size:17px;letter-spacing:-.01em}}
.link svg{{width:7px;height:12px;transition:transform .2s var(--out)}}
.link-plain{{color:var(--ink-2)}}

/* hero */
.hero{{position:relative;padding:116px 0 0;text-align:center;overflow:hidden}}
.hero h1{{font-size:clamp(2.6rem,6vw,4.9rem);line-height:1.04;letter-spacing:-.038em}}
.hero .lede{{margin:22px auto 0;max-width:34ch;font-size:clamp(1.12rem,1.6vw,1.32rem);line-height:1.45;color:var(--ink-2);letter-spacing:-.012em}}
.hero .ctas{{margin-top:32px;display:flex;justify-content:center;align-items:center;gap:28px;flex-wrap:wrap}}
.fan{{position:relative;--w:clamp(200px,23vw,320px);height:calc(var(--w) * 1.42);margin-top:52px}}
.fan .device{{position:absolute;left:50%;top:0}}
.fan .d1{{transform:translateX(-50%);z-index:3}}
.fan .d0{{transform:translateX(calc(-50% - 78%)) translateY(9%) rotate(-7deg);z-index:2;opacity:.9}}
.fan .d2{{transform:translateX(calc(-50% + 78%)) translateY(9%) rotate(7deg);z-index:2;opacity:.9}}
.floor{{position:absolute;left:50%;bottom:-55%;width:min(1200px,140vw);aspect-ratio:2.4;transform:translateX(-50%);pointer-events:none;
  background:radial-gradient(closest-side,rgba(16,185,129,.30),rgba(16,185,129,.08) 55%,transparent)}}
/* the one authored load moment: headline, then the three phones settle in */
@media (prefers-reduced-motion:no-preference){{
  .hero h1,.hero .lede,.hero .ctas{{animation:rise .9s var(--out) both}}
  .hero .lede{{animation-delay:.08s}} .hero .ctas{{animation-delay:.16s}}
  .fan .device{{animation:settle 1.3s var(--out) both}}
  .fan .d1{{animation-delay:.28s}} .fan .d0,.fan .d2{{animation-delay:.42s}}
  .floor{{animation:glow 1.6s var(--out) .3s both}}
}}
@keyframes rise{{from{{opacity:0;transform:translateY(14px);filter:blur(6px)}}}}
@keyframes settle{{from{{opacity:0;translate:0 90px;scale:.96}}}}
@keyframes glow{{from{{opacity:0}}}}

/* scroll story: text on the left, one pinned phone on the right that changes screen */
.story{{position:relative;padding:clamp(120px,16vw,200px) 0 40px}}
.story-head{{text-align:center;margin-bottom:clamp(40px,8vw,96px)}}
.story-head h2{{font-size:clamp(2.2rem,5vw,4rem);line-height:1.06;letter-spacing:-.034em}}
.story-grid{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,6vw,96px)}}
.step{{min-height:88vh;display:flex;flex-direction:column;justify-content:center;max-width:30rem;opacity:.28;transition:opacity .5s var(--out)}}
.step.on{{opacity:1}}
.step h3{{font-size:clamp(1.9rem,3.6vw,3rem);line-height:1.08;letter-spacing:-.03em}}
.step>p{{margin-top:18px;font-size:clamp(1.06rem,1.4vw,1.24rem);line-height:1.5;color:var(--ink-2);letter-spacing:-.008em}}
.step-device{{display:none}}
.pin{{position:sticky;top:calc(50vh - min(42vh,330px));height:min(84vh,660px);display:grid;place-items:center}}
.pin .layer{{position:absolute;inset:0;display:grid;place-items:center;opacity:0;transform:scale(.985);filter:blur(6px);
  transition:opacity .55s var(--out),transform .55s var(--out),filter .55s var(--out)}}
.pin .layer.on{{opacity:1;transform:none;filter:none}}
.pin .device{{--w:auto;height:100%;width:auto}}
.pin::before{{content:"";position:absolute;inset:8% -10%;border-radius:50%;background:radial-gradient(closest-side,rgba(16,185,129,.16),transparent);pointer-events:none}}

/* light and dark */
.theme{{padding:clamp(120px,16vw,200px) 0;text-align:center}}
.theme h2{{font-size:clamp(2.2rem,5vw,4rem);line-height:1.06;letter-spacing:-.034em}}
.theme .wrap>p{{margin:18px auto 0;max-width:36ch;font-size:clamp(1.06rem,1.4vw,1.24rem);color:var(--ink-2)}}
.seg{{position:relative;display:inline-grid;grid-template-columns:1fr 1fr;margin-top:36px;padding:4px;border-radius:999px;background:var(--raise);border:1px solid var(--line)}}
.seg button{{position:relative;z-index:1;appearance:none;border:0;background:none;color:var(--ink-2);font:500 15px/1 var(--f-sans);height:36px;padding:0 26px;border-radius:999px;cursor:pointer;transition:color .25s ease}}
.seg button[aria-pressed="true"]{{color:#0D1A14}}
.seg .thumb{{position:absolute;top:4px;bottom:4px;left:4px;width:calc(50% - 4px);border-radius:999px;background:var(--ink);transition:transform .28s var(--spring)}}
.seg[data-mode="light"] .thumb{{transform:translateX(100%)}}
.seg button:active{{transform:scale(.97)}}
.theme-stage{{position:relative;margin:56px auto 0;width:min(320px,74vw);aspect-ratio:9/19.3}}
.theme-stage .layer{{position:absolute;inset:0;opacity:0;filter:blur(8px);transition:opacity .5s var(--out),filter .5s var(--out)}}
.theme-stage .layer.on{{opacity:1;filter:none}}
.theme-stage .device{{--w:100%}}

/* details: a quiet spec list */
.details{{padding:0 0 clamp(120px,16vw,200px)}}
.details h2{{font-size:clamp(2.2rem,5vw,4rem);line-height:1.06;letter-spacing:-.034em;max-width:14ch}}
.specs{{margin:clamp(40px,6vw,72px) 0 0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:clamp(24px,4vw,56px)}}
.spec{{padding:26px 0 30px;border-top:1px solid var(--line)}}
.spec dt{{font-size:19px;font-weight:600;letter-spacing:-.015em}}
.spec dd{{margin:8px 0 0;color:var(--ink-2);max-width:34ch}}

/* closing */
.close{{padding:0 0 clamp(120px,14vw,180px);text-align:center}}
.close .ar{{font-size:clamp(1.4rem,2.4vw,1.9rem);color:var(--sand);font-weight:500}}
.close h2{{margin-top:14px;font-size:clamp(2.4rem,6vw,4.6rem);line-height:1.04;letter-spacing:-.036em}}
.close .ctas{{margin-top:34px;display:flex;justify-content:center;align-items:center;gap:28px;flex-wrap:wrap}}
.close .mark-big{{width:72px;height:72px;margin:0 auto 26px;display:block}}

footer{{border-top:1px solid var(--line);padding:28px 0 40px;font-size:13px;color:var(--ink-3)}}
footer .wrap{{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}}
footer nav{{display:flex;gap:22px}}
footer a{{color:var(--ink-2);transition:color .2s ease}}
footer a svg{{width:9px;height:9px;margin-left:3px;vertical-align:1px}}

@media (hover:hover) and (pointer:fine){{
  .nav-links a:not(.btn):hover,footer a:hover{{color:var(--ink)}}
  .btn-mint:hover{{background:#13C68C}}
  .link:hover svg{{transform:translateX(3px)}}
  .seg button:hover{{color:var(--ink)}}
  .seg button[aria-pressed="true"]:hover{{color:#0D1A14}}
}}
@media (max-width:900px){{
  .nav-links .opt{{display:none}}
  .story-grid{{grid-template-columns:1fr}}
  .pin{{display:none}}
  .step{{min-height:0;opacity:1;max-width:none;padding:56px 0;text-align:center;align-items:center}}
  .step>p{{max-width:34ch}}
  .step-device{{display:block;margin-top:40px}}
  .step-device .device{{--w:min(280px,70vw)}}
  .specs{{grid-template-columns:1fr 1fr}}
}}
@media (max-width:560px){{
  .fan .d0,.fan .d2{{display:none}}
  .fan{{--w:min(270px,72vw)}}
  .specs{{grid-template-columns:1fr}}
  .hero .ctas,.close .ctas{{flex-direction:column;gap:18px}}
}}
@media (prefers-reduced-motion:reduce){{
  .pin .layer,.theme-stage .layer{{transform:none!important;filter:none!important}}
  .mz *,.mz *::before,.mz *::after{{animation:none!important}}
}}
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav" id="nav">
  <div class="wrap">
    <a href="#top" class="brand" aria-label="Mizan, back to top">{mark}<span>Mizan</span><span class="ar" lang="ar">مِيزان</span></a>
    <nav class="nav-links" aria-label="Page">
      <a class="opt" href="#story">How it works</a><a class="opt" href="#details">Details</a>
      <a class="btn btn-mint btn-sm" href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
    </nav>
  </div>
</header>

<main id="main">
  <section class="hero" id="top">
    <div class="wrap">
      <h1>Smart nutrition,<br>absolute balance.</h1>
      <p class="lede">Mizan plans your family's week of meals and keeps the grocery basket inside your budget.</p>
      <div class="ctas">
        <a class="btn btn-mint" href="{GITHUB}" target="_blank" rel="noopener">View on GitHub</a>
        <a class="link" href="#story">See how it works {CHEVRON}</a>
      </div>
    </div>
    <div class="fan" aria-hidden="true">
      <div class="floor"></div>
      {device(MZ.wizard(), 'd0')}{device(MZ.home(cook=False), 'd1')}{device(MZ.grocery(), 'd2')}
    </div>
  </section>

  <section class="story" id="story" aria-label="How Mizan works">
    <div class="wrap">
      <div class="story-head"><h2>A week of meals,<br>planned around your budget.</h2></div>
      <div class="story-grid">
        <div class="steps">{story_text}</div>
        <div class="pin" aria-hidden="true">{story_phones}</div>
      </div>
    </div>
  </section>

  <section class="theme" aria-label="Light and dark">
    <div class="wrap">
      <h2>Easy on the eyes,<br>day or night.</h2>
      <p>Choose automatic, light or dark from your profile.</p>
      <div class="seg" role="group" aria-label="Preview theme" data-mode="dark">
        <span class="thumb" aria-hidden="true"></span>
        <button type="button" data-mode="dark" aria-pressed="true">Dark</button>
        <button type="button" data-mode="light" aria-pressed="false">Light</button>
      </div>
      <div class="theme-stage" aria-hidden="true">
        <div class="layer on" data-theme="dark">{device(MZ.home(cook=False))}</div>
        <div class="layer" data-theme="light">{device(MZ.home(light=True, cook=False))}</div>
      </div>
    </div>
  </section>

  <section class="details" id="details">
    <div class="wrap">
      <h2>Made for Saudi kitchens.</h2>
      <dl class="specs">{details}</dl>
    </div>
  </section>

  <section class="close">
    <div class="wrap">
      {MZ.MARK.replace('class="z-mark"', 'class="mark-big" style="--z-sand:#E5D4C0;--z-mint:#10B981"')}
      <p class="ar" lang="ar" dir="rtl">وش نطبخ اليوم؟</p>
      <h2>The code is on GitHub.</h2>
      <div class="ctas">
        <a class="btn btn-mint" href="{GITHUB}" target="_blank" rel="noopener">View the code</a>
        <a class="link" href="../">More of my work {CHEVRON}</a>
      </div>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <span>Designed and built by Lujain Aloufi. Prices in the screens are sample data.</span>
    <nav aria-label="Elsewhere"><a href="{GITHUB}" target="_blank" rel="noopener">GitHub{ARROW_UP}</a><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn{ARROW_UP}</a><a href="../">Portfolio</a></nav>
  </div>
</footer>

<script>
(()=>{{
  // hairline under the nav once the page has scrolled
  const nav=document.getElementById("nav"),top=document.getElementById("top");
  new IntersectionObserver(([e])=>nav.classList.toggle("scrolled",!e.isIntersecting),{{rootMargin:"-56px 0px 0px 0px",threshold:.98}}).observe(top);
  // scroll story: the step crossing the middle of the screen picks the phone screen
  const steps=[...document.querySelectorAll(".step")],layers=[...document.querySelectorAll(".pin .layer")];
  const pick=i=>{{steps.forEach((s,k)=>s.classList.toggle("on",k===i));layers.forEach((l,k)=>l.classList.toggle("on",k===i))}};
  const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting)pick(+e.target.dataset.step)}}),{{rootMargin:"-45% 0px -45% 0px"}});
  steps.forEach(s=>io.observe(s));
  // light and dark preview
  const seg=document.querySelector(".seg"),btns=[...seg.querySelectorAll("button")],themes=[...document.querySelectorAll(".theme-stage .layer")];
  btns.forEach(b=>b.addEventListener("click",()=>{{const m=b.dataset.mode;seg.dataset.mode=m;
    btns.forEach(x=>x.setAttribute("aria-pressed",x===b));themes.forEach(t=>t.classList.toggle("on",t.dataset.theme===m))}}));
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
