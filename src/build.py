#!/usr/bin/env python3
"""Build the portfolio site.

Run from the repository root:
    python3 src/build.py            -> index.html (media loaded from assets/)
    python3 src/build.py --single   -> also dist/portfolio.html, one self-contained file with media inlined

Pieces:
  src/base.html           page shell: <head>, About page, mobile menu and shared scripts
  src/styles.css          home deck, project pages, intro, cursor, stack page, footer
  src/tawaqaa.css         the code-drawn Tawaqaa phone and laptop screens, Masar laptop
  src/mizan.css           the code-drawn Mizan phone screens and floating cards
  src/mizan_scenes.py     markup for the Mizan screens
  src/main.js             deck, transitions, intro, cursor, project pages
  src/tawaqaa_scenes.py   markup for the Tawaqaa screens
  src/intro_curves.py     intro motion curves, sampled at 60 Hz
  src/icons.json          tool logos (SVG paths)
  assets/                 recorded app screens (animated WebP)
"""
import base64, os, re, shutil, html, sys, json
sys.path.insert(0, 'src')
import tawaqaa_scenes as TQ
import mizan_scenes as MZ
import intro_curves

OLD = open('src/base.html').read()
CSS_NEW = open('src/styles.css').read() + '\n' + open('src/tawaqaa.css').read() + '\n' + open('src/mizan.css').read()
JS_NEW = open('src/main.js').read()

def between(s, a, b, inc_a=True):
    i = s.index(a); j = s.index(b, i + len(a))
    return s[i if inc_a else i + len(a):j]

# ---------- head ----------
head = OLD[:OLD.index('<style>') + len('<style>')]
head = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/css2\?family=IBM\+Plex\+Sans\+Arabic[^"]*">', '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&amp;display=swap">', head)
head = head.replace('<meta name="theme-color" content="#7E6D54">', '<meta name="theme-color" content="#0F3442">')
# body face: Inter for platforms without Helvetica Neue (Windows, Android)
head = head.replace('family=Bebas+Neue&amp;family=League+Gothic&amp;display=swap', 'family=Bebas+Neue&amp;family=Inter:wght@400;500;600;700&amp;family=League+Gothic&amp;display=swap')
assert 'family=Inter' in head
head = head.replace('"sameAs":["https://github.com/your-username","https://www.linkedin.com/in/your-handle"]', '"sameAs":["https://www.linkedin.com/in/lujain-aloufi/","https://github.com/lujainaloufi0"]')
head = head.replace('"knowsAbout":["Python","Java","TypeScript","Next.js","NestJS","PostgreSQL","Firebase","AWS","SQL","Computer Vision","YOLOv10","IoT"]', '"knowsAbout":["Python","Java","JavaScript","TypeScript","SQL","React","Next.js","NestJS","Node.js","PostgreSQL","Firebase","Prisma","Socket.IO","Docker","YOLOv10","Android"]')
assert 'your-username' not in head and 'your-domain' not in head


# ---------- CSS ----------
style = between(OLD, '<style>', '</style>', inc_a=False)
css_base = style[:style.index('/* ═════════ HOME ═════════ */')]
css_base = css_base.replace('--home:#7E6D54;', '--home:#262626;').replace('--f-body:"Helvetica Neue",Helvetica,Arial,sans-serif;', '--f-body:"Helvetica Neue",Inter,Helvetica,Arial,sans-serif;').replace('--home:#25211B;', '--home:#1E1E1E;')
css_base = css_base.replace('Layout: two "pages" in one file. HOME is a fixed full-screen stage (3D card deck + rolling title belt, corner nav).',
                            'Layout: two "pages" in one file. HOME is a fixed full-screen stage: one flat card per project with its title above, and the page colour follows the project.')
css_about = style[style.index('/* ═════════ CURTAIN ═════════ */'):style.index('/* ── project media in the deck ── */')]
css_about = css_about.replace('.a-intro{grid-column:3/span 6;font:500 clamp(.95rem,1.25vw,1.15rem)/1.55 var(--f-body);text-transform:uppercase;letter-spacing:.02em;', '.a-intro{grid-column:3/span 6;font:400 clamp(1.0625rem,1.35vw,1.25rem)/1.5 var(--f-body);max-width:46ch;')
assert 'text-transform:uppercase;letter-spacing:.02em' not in css_about
css_rm = ''
css_about = re.sub(r'\.f-giant\{font:700[^}]*\}', '', css_about)
CSS = css_base + CSS_NEW + '\n' + css_about + css_rm
def gate_hover(css):
    out, i, depth, start = [], 0, 0, 0
    buf = ''
    # walk top-level rules; wrap any whose selector uses :hover (and no :focus) in a hover-capable media query
    while i < len(css):
        ch = css[i]
        if ch == '{':
            if depth == 0:
                sel_start = start
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                rule = css[start:i+1]
                sel = rule[:rule.index('{')]
                if ':hover' in sel and ':focus' not in sel and not sel.strip().startswith('@'):
                    rule = '@media (hover:hover) and (pointer:fine){' + rule.strip() + '}'
                out.append(rule)
                start = i + 1
        i += 1
    out.append(css[start:])
    return ''.join(out)
CSS = gate_hover(CSS)

# ---------- assets ----------
A = {}
def asset(name): A[name] = True; return '@@A:%s@@' % name

ICON_PATHS = json.load(open('src/icons.json'))
def icon(name):
    d = ICON_PATHS.get(name)
    return f'<svg class="ti" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="{d}"/></svg>' if d else ''
# one list, used by the home card, the Stack page and the About strip. p = projects that used it (t/m/z)
TOOLS = [
 ('Languages', [('Python','t','Tawaqaa'),('Java','t','Tawaqaa'),('JavaScript','t m','Tawaqaa, Masar'),('TypeScript','m z','Masar, Mizan'),('SQL','m','Masar'),('HTML','t m z','All three'),('CSS','t m z','All three')]),
 ('Frameworks', [('React','m z','Masar, Mizan'),('React Native','z','Mizan'),('Expo','z','Mizan'),('Next.js','m z','Masar, Mizan'),('NestJS','m','Masar'),('Node.js','m','Masar')]),
 ('Data', [('PostgreSQL','m','Masar'),('Firebase','t','Tawaqaa')]),
 ('AI, mobile &amp; design', [('YOLOv10','t','Tawaqaa'),('Android','t z','Tawaqaa, Mizan'),('Figma','t','Tawaqaa')]),
]
ALL_TOOLS = [n for _, items in TOOLS for n, _, _ in items]
ROWS = [ALL_TOOLS[0:5], ALL_TOOLS[5:10], ALL_TOOLS[10:14], ALL_TOOLS[14:18]]
stack_rows = ''; n = 0
for names in ROWS:
    stack_rows += '<div class="row">' + ''.join(f'<span style="--n:{(n+k*2)%8}">{icon(nm)}{nm}</span>' for _ in range(3) for k, nm in enumerate(names)) + '</div>'
    n += 3

PROJ = [
 dict(key='tawaqaa', title='Tawaqaa', ar='', attr='IOT &amp; ML   •   2024   •   GRADUATION PROJECT', card='@html:tq', bg=None,
      alt='Tawaqaa in motion: the Arabic app reporting a flooded street, the services screen and live flood alerts',
      meta_l=[('Type','Graduation project · IoT &amp; ML'),('Role','Project lead &amp; systems developer'),('Completed','2024 · University of Jeddah')],
      meta_r=[('Awards','Grand Special Award, SGiE 2024')],
      stack=['Java','Android','Firebase','Python','YOLOv10','JavaScript','Figma'],
      desc="Tawaqaa is a road-safety system for Jeddah's rainy season. Citizens report flooded streets from an Android app, by street name or with a pin on the map. Reports are counted and ranked by street, a water-level sensor measures the worst spot, and a YOLOv10 model trained on 1,532 images of flooded cars and 171 of people in floodwater flags danger in real time. Drivers get an alert and a safer route, while authorities review and close reports on a web console that syncs live with Firebase.",
      shots=TQ.SHOTS, phone=False, html=True),
 dict(key='masar', title='Masar', ar='', attr='WEB APP   •   2026   •   FULL-STACK', card='m-card.webp', bg=None,
      alt='Masar in use: signing in, the department overview, the task board, completing a task and switching to Arabic',
      meta_l=[('Type','Bilingual web app for government teams'),('Role','Backend &amp; full-stack developer'),('Completed','Jun – Sep 2026')],
      meta_r=[],
      stack=['TypeScript','React','Next.js','NestJS','Node.js','PostgreSQL'],
      desc='Masar is a task workspace for government departments. Each task has an owner and steps the whole team can see, and finished work stays on record. Members, department heads, HR and administrators each get their own view, showing progress by group and the average days to finish a task. The app works fully in Arabic and English, with right-to-left layout, Hijri and Gregorian dates, dark mode and live updates.',
      shots=[('01 · Sign in','m-signin.webp','Sign in with an employee ID. New staff set their password on first sign-in.'),
             ('02 · Overview','m-overview.webp',"The department head's overview: active tasks, progress by group and days to complete."),
             ('03 · Tasks','m-tasks.webp','The task board filters by group as you switch tabs.'),
             ('04 · Task','m-task.webp','Ticking the last step completes the task and the progress ring fills.'),
             ('05 · Groups','m-groups.webp','Groups, their members and the open work each one owns.'),
             ('06 · Arabic','m-arabic.webp','Arabic, right to left, then dark mode, one click each.')], phone=False, laptop=True),
 dict(key='mizan', title='Mizan', ar='مِيزان', attr='ANDROID APP   •   2026   •   EXPO &amp; REACT NATIVE', card='@html:mz', bg=None,
      alt='Mizan in Arabic: the weekly budget step with a balance scale, today\'s meals and the grocery list',
      meta_l=[('Type','Android app · meal planning &amp; grocery budget'),('Role','Design &amp; development'),('Year','2026')],
      meta_r=[('Links','<a href="https://lujainaloufi0.github.io/portfolio/mizan/" target="_blank" rel="noopener">Landing page</a> · <a href="https://github.com/lujainaloufi0/Mizan" target="_blank" rel="noopener">GitHub</a>')],
      stack=['TypeScript','React Native','Expo','React','Android'],
      desc="Mizan plans a Saudi household's week of meals and keeps the shopping inside a budget. You pick your cuisines, supermarkets, household size and a weekly budget in riyals, and Mizan plans the week from 163 halal recipes across 18 cuisines, filtered by your allergies, kitchen appliances and goal. It builds the grocery list sorted by aisle and store, and sends it to a delivery app. The app is Arabic first, right to left, with light and dark themes.",
      shots=MZ.SHOTS, phone=False, html=True),
 dict(key='stack', title='Stack', ar='', attr='LANGUAGES   •   FRAMEWORKS   •   TOOLS', card=None, bg=None, shots=[]),
]

def masar_sky():
    """Masar means "path": stars twinkle, and every so often a few of them join into a route."""
    import random
    r = random.Random(11)
    stars = []
    for _ in range(46):
        x, y = r.uniform(2, 98), r.uniform(2, 98)
        if 18 < x < 82 and 18 < y: continue  # leave the laptop clear
        stars.append(f'<i style="--x:{x:.1f}%;--y:{y:.1f}%;--s:{r.choice([1,1,1.4,1.8])};--d:{r.uniform(2.6,5.5):.1f}s;--w:-{r.uniform(0,5):.1f}s"></i>')
    path = [(6, 62), (11, 40), (8, 22), (16, 11), (27, 7), (34, 14)]
    path2 = [(66, 12), (76, 6), (86, 13), (93, 30), (89, 52), (95, 74)]
    def route(pts, cls):
        ln = ' '.join(f'{x*2.2:.1f},{y}' for x, y in pts)  # the stage is 2.2:1
        dots = ''.join(f'<i class="node" style="--x:{x}%;--y:{y}%;--k:{k}"></i>' for k, (x, y) in enumerate(pts))
        return (f'<svg class="m-route {cls}" viewBox="0 0 220 100" preserveAspectRatio="none"><polyline points="{ln}" pathLength="1"/></svg>'
                f'<span class="m-nodes {cls}">{dots}</span>')
    return '<div class="m-sky" aria-hidden="true">' + ''.join(stars) + route(path, 'r1') + route(path2, 'r2') + '</div>'

def card_html(i, p):
    lazy = ' loading="lazy"' if i else ''
    if p['card'] == '@html:tq':
        return f'<div class="card is-on" role="button" tabindex="0" data-k="{i}" aria-label="Open Tawaqaa: the app\'s report, home and alert screens">{TQ.CARD}</div>'
    if p['card'] == '@html:mz':
        return f'<div class="card" role="button" tabindex="0" data-k="{i}" aria-label="Open Mizan: {p["alt"]}">{MZ.CARD}</div>'
    if p.get('laptop'):
        still = p['card'].replace('.webp', '-still.webp')
        img = f'<img src="{asset(still)}" data-still="{asset(still)}" data-anim="{asset(p["card"])}" alt="" decoding="async">'
        return f'<div class="card" role="button" tabindex="0" data-k="{i}" aria-label="Open {html.unescape(p["title"])}: {p["alt"]}"><div class="mk" aria-hidden="true">{masar_sky()}{TQ.laptop(img)}</div></div>'
    inner = (f'<img src="{asset(p["card"])}" alt="{p["alt"]}" width="760" height="345"{lazy} decoding="async">'
             if p['card'] else f'<div class="c-stack" style="position:absolute;inset:0" aria-hidden="true">{stack_rows}</div><span class="sr-only">Stack: the languages, frameworks and tools I use</span>')
    return f'<div class="card" role="button" tabindex="0" data-k="{i}" aria-label="Open {html.unescape(p["title"])}">{inner}</div>'

TI = ' tabindex="-1"'
CUR = ' class="is-current"'
def letters(t):
    t = html.unescape(t)
    return ''.join(f'<span class="ch" style="--c:{k}">{"&nbsp;" if ch==" " else html.escape(ch)}</span>' for k, ch in enumerate(t))
ON = ' class="on"'
BELT = ''.join(f'        <li{ON if i==0 else ""}><button type="button" data-open="{i}"{TI if i else ""} aria-label="{html.unescape(p["title"])}"><span aria-hidden="true">{letters(p["title"])}</span></button></li>\n' for i,p in enumerate(PROJ))
CAT = ''.join(f'        <li style="--k:{i}"{CUR if i==0 else ""}><button type="button" data-open="{i}"><span class="t">{p["title"]}</span><span class="d lbl">{p["attr"]}</span></button></li>\n' for i,p in enumerate(PROJ))
HOME = f'''<!-- ═════════════ HOME ═════════════ -->
<div id="home" class="intro">
  <div class="corner c-tl">
    <a class="logo" href="#work" aria-label="Lujain Aloufi, home">
      <span class="ln en" aria-hidden="true"><span>LUJAIN ALOUFI</span><span>LUJAIN ALOUFI</span></span>
      <span class="ln ar" lang="ar" dir="rtl" aria-hidden="true"><span>لجين العوفي</span><span>لجين العوفي</span></span>
    </a>
  </div>
  <div class="corner c-tr">
    <button class="roll lbl theme" type="button" data-theme-toggle aria-pressed="false"><span>Dark mode</span><span aria-hidden="true">Dark mode</span></button>
    <button class="roll lbl" type="button" id="view-toggle" aria-pressed="false"><span>Catalog view</span><span aria-hidden="true">Catalog view</span></button>
    <button class="roll lbl menu-btn" type="button" id="menu-open" aria-expanded="false" aria-controls="menu"><span>Menu</span><span aria-hidden="true">Menu</span></button>
  </div>

  <main id="main-home" tabindex="-1">
    <h1 class="sr-only">Lujain Aloufi, Software Engineer and Full-Stack Systems. Selected work.</h1>
    <div class="hero">
      <div class="belt"><ol id="belt" style="--at:0">
{BELT}      </ol></div>
      <div class="attr lbl" aria-hidden="true"><ol id="attr" style="--at:0">
{''.join(f'        <li{ON if i==0 else ""}>{p["attr"]}</li>{chr(10)}' for i,p in enumerate(PROJ))}      </ol></div>
      <div class="stage" id="stage">
{''.join('        '+card_html(i,p)+chr(10) for i,p in enumerate(PROJ))}      </div>
      @@HOMEDOCK@@
    </div>
    <nav class="ticks" aria-label="Projects">
{''.join(f'      <button type="button" aria-label="{html.unescape(p["title"])}"></button>{chr(10)}' for p in PROJ)}    </nav>
    <section id="catalog" aria-label="Catalog view">
      <ol class="cat-list" id="cat-list">
{CAT}      </ol>
    </section>
  </main>

  <div class="corner c-bl">
    <a class="lbl" href="#about">About</a>
    <a class="lbl" href="#contact">Let's connect</a>
  </div>
  <div class="corner c-br">
    <span class="mouse" aria-hidden="true"></span>
    <p class="sr-only" id="live" aria-live="polite"></p>
  </div>
</div>
'''

CLOSE = '<button class="case-close lbl" type="button"><svg viewBox="0 0 12 12" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M1 1l10 10M11 1 1 11"/></svg>Close</button>'
LOGO = '<span class="case-logo logo" aria-hidden="true"><span class="ln en"><span>LUJAIN ALOUFI</span></span><span class="ln ar" lang="ar" dir="rtl"><span>لجين العوفي</span></span></span>'

def meta_col(items):
    return '<div>' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items) + '</div>'

def case_html(i, p):
    nxt = (i + 1) % len(PROJ)
    nxt_btn = f'<div class="case-next"><span class="lbl">Next project</span><button type="button" data-next="{nxt}"><span class="t">{PROJ[nxt]["title"]} →</span></button></div>'
    if p['key'] == 'stack':
        return STACK_CASE.replace('@@NEXT@@', nxt_btn)
    ar = f' <span lang="ar">{p["ar"]}</span>' if p['ar'] else ''
    stack = '<ul class="case-stack">' + ''.join(f'<li>{icon(t)}{t}</li>' for t in p['stack']) + '</ul>'
    shots = ''
    for j, (lbl, f, cap) in enumerate(p['shots']):
        if p.get('html'):
            shots += f'      <li class="shot" id="{p["key"]}-s{j}"><p class="cap"><span class="lbl">{lbl}</span><span>{cap}</span></p><div class="frame live" role="img" aria-label="{cap}">{f}</div></li>\n'
            continue
        if p.get('laptop'):
            lap = TQ.laptop('<img src="%s" alt="%s" loading="lazy" decoding="async">' % (asset(f), cap))
            shots += f'      <li class="shot" id="{p["key"]}-s{j}"><p class="cap"><span class="lbl">{lbl}</span><span>{cap}</span></p><div class="frame live"><div class="mk">{lap}</div></div></li>\n'
            continue
        frame_cls = 'frame phone' if p['phone'] else 'frame'
        shots += f'      <li class="shot" id="{p["key"]}-s{j}"><p class="cap"><span class="lbl">{lbl}</span><span>{cap}</span></p><div class="{frame_cls}"><img src="{asset(f)}" alt="{cap}" loading="lazy" decoding="async"></div></li>\n'
    if p.get('html'):
        rail = '<button class="txt" type="button" aria-label="Overview">INFO</button>' + ''.join(f'<button class="txt" type="button" aria-label="{lbl}">{lbl[:2]}</button>' for lbl, _, _ in p['shots'])
    else:
        rail = '<button class="txt" type="button" aria-label="Overview">INFO</button>' + ''.join(f'<button type="button" aria-label="{lbl}"><img src="@@R:{f}@@" alt="" loading="lazy" decoding="async"></button>' for lbl, f, _ in p['shots'])
    return f'''<dialog class="case" id="case-{i}" aria-labelledby="case-{i}-t">
  <div class="case-bg" aria-hidden="true"><div class="case-media"></div></div>
  {LOGO}{CLOSE}
  <div class="case-ui">
    <section class="case-intro">
      <h2 id="case-{i}-t">{p['title']}{ar}</h2>
      <dl class="case-meta">{meta_col(p['meta_l'])}{meta_col(p['meta_r'] + [('Stack', stack)])}</dl>
      <p class="case-desc">{p['desc']}</p>
      <p class="scroll-cue"><span class="mouse" aria-hidden="true"></span>Scroll to see it in motion</p>
    </section>
    <ol class="shots-col">
{shots}    </ol>
    {nxt_btn}
  </div>
  <nav class="rail case-ui" aria-label="Jump to a clip">{rail}</nav>
</dialog>
'''

# Stack page: reuse the grouped tool list from the previous version
groups = ''.join('        <div><h3 class="lbl">%s</h3><ul>%s</ul></div>\n' % (g, ''.join(f'<li data-p="{pp}"><b>{icon(nm)}{nm}</b><small>{u}</small></li>' for nm, pp, u in items)) for g, items in TOOLS)
STACK_CASE = f'''<dialog class="case" id="case-3" aria-labelledby="case-3-t">
  <div class="case-bg" aria-hidden="true"><div class="case-media"></div></div>
  {LOGO}{CLOSE}
  <div class="case-ui">
    <section class="case-intro" style="min-height:auto;padding-bottom:3rem">
      <h2 id="case-3-t">Stack</h2>
      <p class="case-desc">The tools I reach for and where I've shipped with them: Java and Python for Tawaqaa's app and detection model, a TypeScript stack for Masar, and React Native with Expo for Mizan.</p>
    </section>
    <div class="st-wrap">
      <div class="st-filter" role="group" aria-label="Show tools used in">
        <button type="button" data-f="" aria-pressed="true">All</button>
        <button type="button" data-f="t" aria-pressed="false">Tawaqaa</button>
        <button type="button" data-f="m" aria-pressed="false">Masar</button>
        <button type="button" data-f="z" aria-pressed="false">Mizan</button>
        <span class="st-count lbl" id="st-count" aria-live="polite">{len(ALL_TOOLS)} tools</span>
      </div>
      <div class="st-groups">{groups}
      </div>
    </div>
    @@NEXT@@
  </div>
</dialog>
'''
CASES = '<!-- project pages -->\n' + ''.join(case_html(i, p) for i, p in enumerate(PROJ))

# ---------- reuse menu, About page and curtain ----------
MENU = between(OLD, '<!-- mobile menu -->', '<!-- ═════════════ ABOUT')

ABOUT = between(OLD, '<!-- ═════════════ ABOUT ═════════════ -->', '<script>')
ABOUT = ABOUT.replace('data-open-from-about="2"', 'data-open-from-about="2"')
GH = 'https://github.com/lujainaloufi0'
ABOUT = ABOUT.replace('<a href="https://github.com/your-username" target="_blank" rel="noopener">github.com/your-username ↗</a>', f'<a href="{GH}" target="_blank" rel="noopener">github.com/lujainaloufi0 ↗</a>')
ABOUT = ABOUT.replace('<a href="https://github.com/your-username" target="_blank" rel="noopener">GitHub</a>', f'<a href="{GH}" target="_blank" rel="noopener">GitHub</a>')
ABOUT = ABOUT.replace('https://github.com/your-username', GH)
ABOUT = ABOUT.replace('Web components, React or Vue, and modern CSS,', 'React, Next.js and modern CSS,')
_strip = ''.join(f'<li>{icon(nm)}{nm}</li>' for nm in ALL_TOOLS)
ABOUT = re.sub(r'<div class="marquee-track">.*?</div>', '<div class="marquee-track">\n          <ul>' + _strip + '</ul>\n          <ul aria-hidden="true">' + _strip + '</ul>\n        </div>', ABOUT, count=1, flags=re.S)
assert 'your-username' not in ABOUT and ABOUT.count('github.com/lujainaloufi0') == 2 and 'Vue' not in ABOUT
for _n in re.findall(r'@@A:([^@]+)@@', ABOUT): asset(_n)  # About page photos
# ---------- contact: real LinkedIn, working email, English footer wordmark ----------
LI='https://www.linkedin.com/in/lujain-aloufi/'
MAIL='lujain.aloufi0@gmail.com'
ABOUT = ABOUT.replace('linkedin.com/in/your-handle ↗','linkedin.com/in/lujain-aloufi ↗').replace('https://www.linkedin.com/in/your-handle',LI)
ABOUT = ABOUT.replace('<code id="email-text">lujain.aloufi0@gmail.com</code>', f'<a id="email-text" class="mail-link" href="mailto:{MAIL}">{MAIL}</a>')
ABOUT = ABOUT.replace('<span class="lbl">Drop me a line</span><a href="#contact">lujain.aloufi0@gmail.com</a>', f'<span class="lbl">Drop me a line</span><a href="mailto:{MAIL}">{MAIL}</a>')
ABOUT = ABOUT.replace('<p class="f-giant" lang="ar" dir="rtl" aria-hidden="true">لجين العوفي</p>', '<p class="f-giant" aria-hidden="true"><span>Lujain Aloufi</span></p>')
ABOUT = ABOUT.replace('<span>© 2026 Lujain Aloufi</span></div>', '<a class="f-top" href="#about">Back to top ↑</a><span>© 2026 Lujain Aloufi</span></div>')
for need in ['class="f-top"', LI, f'href="mailto:{MAIL}">{MAIL}</a>', 'class="f-giant" aria-hidden="true"><span>']: assert need in ABOUT, need
assert 'your-handle' not in ABOUT and '#contact">lujain.aloufi0' not in ABOUT


# ---------- JS ----------
old_js = between(OLD, '<script>\n(()=>{', '\n})();\n</script>', inc_a=False)
js_prefix = old_js[:old_js.index('/* ── deck + title belt')]
js_prefix = re.sub(r'const N=4,titles=.*?;\n', '', js_prefix)
js_prefix = js_prefix.replace('const calm=matchMedia("(prefers-reduced-motion: reduce)").matches;', 'const calm=false;')
assert 'const calm=false;' in js_prefix
js_tail = old_js[old_js.index('/* ── mobile menu ── */'):]
js_tail = js_tail.replace('const show=async()=>{', 'const route=async()=>{')
js_tail = js_tail.replace('addEventListener("hashchange",show);show();', 'addEventListener("hashchange",route);route();')
js_tail = js_tail.replace('    syncDeckVideo();\n', '')
js_tail = js_tail.replace('curtain.style.setProperty("--c",toAbout?"var(--about)":colors[cur]);', 'curtain.style.setProperty("--c",toAbout?"var(--about)":P[cur].bg);')
js_tail = js_tail.replace('location.hash="#work";await wait(1700);openCase(k)', 'location.hash="#work";await wait(1700);openCase(k)')
js_tail = js_tail.replace('const ENDPOINT="";', 'const ENDPOINT="https://formsubmit.co/ajax/' + MAIL + '";')
js_tail = js_tail.replace('if(!ENDPOINT){await wait(700);throw new Error("demo")}\n    const r=await fetch(ENDPOINT,{method:"POST",body:new FormData(form),headers:{Accept:"application/json"}});if(!r.ok)throw new Error("fail");',
  'const fd=new FormData(form);fd.append("_subject",`Portfolio: ${fd.get("reason")} from ${fd.get("name")}`);fd.append("_replyto",fd.get("email"));fd.append("_template","box");fd.append("_captcha","false");\n    const r=await fetch(ENDPOINT,{method:"POST",body:fd,headers:{Accept:"application/json"}});const j=await r.json().catch(()=>({}));if(!r.ok||j.success==="false"||j.success===false)throw new Error("fail");')
# if the send fails, say so on the page and show the address; nothing opens in another app
js_tail = js_tail.replace('err.message==="demo"?"Demo mode: this form isn\'t connected yet, so nothing was sent. Email me at lujain.aloufi0@gmail.com.":"Your message didn\'t go through. Check your connection and try again, or email me directly."',
  '`Your message didn\'t go through. Check your connection and try again, or email me at ${"' + MAIL + '"}.`')
assert 'formsubmit.co' in js_tail and 'location.href=`mailto' not in js_tail and 'Demo mode' not in js_tail
js_tail = re.sub(r'\npaint\(\);\nconst boot=.*$', '\n', js_tail, flags=re.S)
JS = '<script>\n(()=>{' + js_prefix + intro_curves.JS + JS_NEW + '\n' + js_tail + '\n})();\n</script>\n'

# home: the contact dock again, with the availability note in front, where the status line used to be
_m = re.search(r'<nav class="dock" aria-label="Social links">(.*?)</nav>', ABOUT, re.S)
HOME = HOME.replace('@@HOMEDOCK@@', '<nav class="dock dock-home hero-status" aria-label="Availability and social links" data-base="36" data-max="62">'
    '<span class="dock-status"><i aria-hidden="true"></i><span class="ds-long">Open to software engineering roles</span><span class="ds-short">Open to roles</span></span>'
    '<span class="dock-sep" aria-hidden="true"></span>' + _m.group(1).strip() + '</nav>')
assert '@@HOMEDOCK@@' not in HOME and 'your-' not in HOME

PAGE = head + CSS + '</style>\n</head>\n<body class="on-home">\n<a class="skip" href="#main-home">Skip to content</a>\n\n' + HOME + '\n' + CASES + '\n' + MENU + ABOUT + JS + '</body>\n</html>\n'

def render(inline):
    out = PAGE
    for name in A:
        if inline:
            b = open('assets/' + name, 'rb').read()
            url = 'data:image/webp;base64,' + base64.b64encode(b).decode()
        else:
            url = 'assets/' + name
        out = out.replace('@@A:%s@@' % name, url)
    # rail thumbnails: real files in the hosted build; in the single file the script copies them from the clips
    out = re.sub(r'<img src="@@R:([^@]+)@@" ', (lambda m: '<img ') if inline else (lambda m: '<img src="assets/%s" ' % m.group(1)), out)
    assert '@@' not in out, re.findall(r'@@[^@]+@@', out)[:3]
    return out

import mizan_landing
mizan_landing.write('.')  # mizan/index.html, the Mizan landing page
SINGLE = '--single' in sys.argv
open('index.html', 'w').write(render(False))
missing = [n for n in A if not os.path.exists('assets/' + n)]
assert not missing, missing
if SINGLE:
    os.makedirs('dist', exist_ok=True)
    open('dist/portfolio.html', 'w').write(render(True))
print('index.html KB', round(os.path.getsize('index.html') / 1e3), '| assets', len(A), '| single file' if SINGLE else '')
