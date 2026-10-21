"""Tawaqaa scenes: HTML for the home card and the project-page shots.

Redrawn from the screens in the graduation report (chapter 5): the Arabic, right-to-left Android app
for citizens, the authorities' web page, and the YOLOv10 webcam test. Labels, flows and data fields
follow the report; nothing here is a feature the app did not have.
"""

SB = '<div class="sb"><span>9:41</span><i><svg class="sb-wifi" viewBox="0 0 17 12" aria-hidden="true"><g fill="currentColor"><path d="M8.5 11.2 6.38 9.08A3 3 0 0 1 10.62 9.08Z"/><path d="M3.41 6.11A7.2 7.2 0 0 1 13.59 6.11L11.75 7.95A4.6 4.6 0 0 0 5.25 7.95Z"/><path d="M.58 3.28A11.2 11.2 0 0 1 16.42 3.28L14.72 4.98A8.8 8.8 0 0 0 2.28 4.98Z"/></g></svg><svg class="sb-batt" viewBox="0 0 27 13" aria-hidden="true"><rect x=".6" y=".6" width="22.8" height="11.8" rx="3.6" fill="none" stroke="currentColor" stroke-width="1.1" opacity=".38"/><rect x="2.4" y="2.4" width="19.2" height="8.2" rx="2.1" fill="currentColor"/><path d="M25 4.4v4.2c.85-.3 1.4-1.15 1.4-2.1s-.55-1.8-1.4-2.1z" fill="currentColor" opacity=".45"/></svg></i></div>'

def svg(path, cls='ic'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

WAVE = 'c1.5-1.2 3-1.2 4.5 0s3 1.2 4.5 0 3-1.2 4.5 0 3 1.2 4.5 0'
I_REPORT = f'<path d="M8 3.5s-3 3.3-3 5.4a3 3 0 0 0 6 0C11 6.8 8 3.5 8 3.5zM16 3.5s-3 3.3-3 5.4a3 3 0 0 0 6 0c0-2.1-3-5.4-3-5.4z"/><path d="M3 16.5{WAVE}M3 20.5{WAVE}"/>'
I_DIR = '<path d="M12 21.5V3"/><path d="M12 5h6l2.4 2.5L18 10h-6zM12 12H6l-2.4 2.5L6 17h6z"/>'
I_SAFE = '<path d="M12 3 5 6v5.5c0 4.4 3 7.9 7 9.5 4-1.6 7-5.1 7-9.5V6z"/><path d="m9 12 2.2 2.2L15.5 10"/>'
I_FLOOD = f'<path d="M5.5 13.5 7 9.4A2 2 0 0 1 8.9 8h6.2a2 2 0 0 1 1.9 1.4l1.5 4.1"/><path d="M4.5 13.5h15V16h-15z"/><path d="M3 20.5{WAVE}"/>'
I_GEAR = '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>'
I_BACK = '<path d="m9.5 6 6 6-6 6"/>'          # RTL: "back" points right
I_DOWN = '<path d="m6.5 9.5 5.5 5.5 5.5-5.5"/>'
I_WARN = '<path d="M10.3 4.2 2.6 17.5A2 2 0 0 0 4.3 20.5h15.4a2 2 0 0 0 1.7-3L13.7 4.2a2 2 0 0 0-3.4 0z"/><path d="M12 9.5v4M12 17v.01"/>'
I_STOP = '<circle cx="12" cy="12" r="8.6"/><path d="m5.9 5.9 12.2 12.2"/>'
I_PIN = '<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/>'
CHECK_BADGE = ('<svg class="badge" viewBox="0 0 48 48" aria-hidden="true"><path fill="currentColor" d="M24 3l4.6 3.4 5.7-.2 1.8 5.4 4.7 3.3-1.6 5.5 1.6 5.5-4.7 3.3-1.8 5.4-5.7-.2L24 45l-4.6-3.4-5.7.2-1.8-5.4-4.7-3.3 1.6-5.5-1.6-5.5 4.7-3.3 1.8-5.4 5.7.2z"/>'
               '<path d="m16 24.5 5.5 5.5L32.5 19" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# the wordmark "توقّى" set in Thmanyah Sans Black and kept as outlines, so no font file is shipped
WORDMARK = 'M429 -126C553 -106 668 -58 668 -30C668 3 514 40 380 40C219 40 136 -14 136 -137C136 -195 142 -252 155 -305L39 -324C29 -284 7 -203 7 -112C7 133 168 220 366 220C572 220 789 126 789 -56C789 -198 657 -241 518 -266L447 -279ZM593 -1245 606 -1162C613 -1119 592 -1118 587 -1118C554 -1118 550 -1153 550 -1214H501C501 -1148 476 -1106 442 -1106C424 -1106 410 -1118 410 -1166V-1203H357V-1160C357 -1104 375 -1054 433 -1054C482 -1054 505 -1091 516 -1128C522 -1104 534 -1066 583 -1066C633 -1066 663 -1106 655 -1166L643 -1252ZM636 -384C636 -280 593 -279 447 -279L566 -145C685 -198 756 -285 756 -440C756 -630 649 -742 513 -742C386 -742 292 -644 292 -510C292 -416 339 -326 459 -326C519 -326 556 -348 583 -368L627 -457C633 -435 636 -411 636 -384ZM438 -822 513 -898 588 -822 679 -914 588 -1005 513 -930 438 -1005 347 -914ZM482 -576C544 -576 597 -544 622 -476C583 -471 528 -466 498 -466C432 -466 402 -487 402 -520C402 -552 429 -576 482 -576ZM931 287C1187 287 1286 145 1316 0H1350C1382 0 1399 -17 1399 -49V-189H1324C1304 -353 1213 -450 1085 -450C965 -450 866 -364 866 -206C866 -65 945 0 1031 0H1186C1152 69 1074 122 917 122H880V287ZM976 -233C976 -264 1019 -285 1061 -285C1111 -285 1166 -255 1193 -189H1070C1024 -189 976 -200 976 -233ZM1351 0C1536 0 1677 -104 1630 -354L1608 -468L1462 -440L1493 -268C1505 -200 1485 -189 1400 -189C1368 -189 1351 -172 1351 -140ZM1455 -548 1530 -624 1605 -548 1696 -640 1605 -731 1530 -656 1455 -731 1364 -640Z'

def logo(cls='tqlogo'):
    """The app's mark: the wordmark with the drop beside it, as on the welcome screen."""
    return (f'<span class="{cls}" role="img" aria-label="توقّى"><svg class="wm" viewBox="0 -1260 1700 1560" aria-hidden="true"><path d="{WORDMARK}" fill="currentColor"/></svg>'
            '<svg class="drop" viewBox="0 0 20 28" aria-hidden="true"><path d="M10 1.5S2 11 2 17.2A8 8 0 0 0 18 17.2C18 11 10 1.5 10 1.5z" fill="currentColor"/>'
            '<path d="M6.2 18.5a4.2 4.2 0 0 0 3.6 3.9" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".8"/></svg></span>')

def phone(body, lg=False):
    return f'<div class="iph{" lg" if lg else ""}"><div class="scr" dir="rtl" lang="ar">{SB}{body}</div></div>'

def top(title, extra=''):
    return f'<div class="tb">{svg(I_BACK)}{extra}</div><p class="t1">{title}</p>'


# ── citizen app ──────────────────────────────────────────────────────────────────────────────

def home():
    tiles = [('rep tap', I_REPORT, 'إنشاء بلاغ'), ('', I_DIR, 'الاتجاهات'),
             ('', I_SAFE, 'السلامة والإرشاد'), ('alr', I_FLOOD, 'الإنذارات')]
    t = ''.join(f'<div class="tile {c}" style="--k:{k}"><span class="bub">{svg(i)}</span><span class="t2">{a}</span>'
                f'{"<em>3</em>" if c == "alr" else ""}</div>' for k, (c, i, a) in enumerate(tiles))
    return phone(f'''<div class="hero">{svg(I_GEAR, 'ic gear')}{logo()}<p class="tag">حياتك تهمنا</p></div>
  <div class="sheet0"><p class="hi">مرحبًا بك، <span>لجين</span></p><p class="t1">الخدمات</p><div class="tiles">{t}</div></div>''', lg=True)

def report():
    opts = ['شارع قريش', 'شارع فلسطين', 'شارع أبو يزيد']
    li = ''.join(f'<span class="{"pick" if k == 0 else ""}">{o}</span>' for k, o in enumerate(opts))
    return phone(f'''{top('إنشاء بلاغ')}
  <label class="lab">اسم الشارع</label>
  <div class="sel"><span class="ph">اختر اسم الشارع</span><span class="val">شارع قريش</span>{svg(I_DOWN)}<div class="dd">{li}</div></div>
  <div class="btn go">إرسال</div>
  <p class="alt">{svg(I_PIN)}أو حدّد الموقع على الخريطة</p>
  <div class="mini"><svg viewBox="0 0 200 120" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="200" height="120" fill="#EEF1EC"/><g fill="#E3E7EA"><rect x="10" y="10" width="50" height="34" rx="2"/><rect x="80" y="10" width="54" height="34" rx="2"/><rect x="150" y="62" width="44" height="50" rx="2"/><rect x="10" y="66" width="50" height="44" rx="2"/></g><rect x="80" y="66" width="54" height="44" rx="2" fill="#DCE6D3"/><g stroke="#fff" stroke-width="9" fill="none"><path d="M-5 55H205M70 -5V125M142 -5V125"/></g></svg><span class="mpin r">{svg(I_PIN)}</span></div>
  <div class="done">{CHECK_BADGE}<p class="t1">تم إرسال البلاغ</p><p class="t3">وصل بلاغك للجهات المختصة</p><div class="btn">التالي</div></div>''')

ALERTS = [('r', I_STOP, 'خطير', 'شارع قريش', 80, '6:15 م'),
          ('r', I_STOP, 'خطير', 'شارع فلسطين', 55, '6:22 م'),
          ('a', I_WARN, 'متوسط', 'شارع أبو يزيد', 30, '6:25 م'),
          ('a', I_WARN, 'متوسط', 'طريق الملك عبدالعزيز', 25, '6:31 م')]

def alerts():
    cards = ''.join(f'''<div class="al {c}" style="--k:{k}"><span class="sq">{svg(i)}</span>
    <div class="al-b"><span class="lv">{lv}</span><b>{st}</b><span class="t3">ارتفاع الماء {h} سم</span><span class="mt"><i style="--h:{h}%"></i></span></div>
    <time>{tm}</time></div>''' for k, (c, i, lv, st, h, tm) in enumerate(ALERTS))
    return phone(f'''{top('الإنذارات', '<span class="live"><i></i>مباشر</span>')}
  <div class="chips"><span class="ind"></span><span class="c0">الكل</span><span class="c1">خطير</span><span class="c2">متوسط</span></div>
  <div class="als">{cards}</div>''')

def mapscr():
    return phone(f'''<div class="mapfull">
    <svg viewBox="0 0 200 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
      <rect width="200" height="400" fill="#EEF1EC"/>
      <g fill="#DCE6D3"><rect x="8" y="200" width="52" height="40" rx="3"/><rect x="150" y="18" width="40" height="46" rx="3"/></g>
      <g fill="#E4E7EA"><rect x="70" y="100" width="58" height="60" rx="2"/><rect x="70" y="190" width="58" height="80" rx="2"/><rect x="0" y="100" width="40" height="70" rx="2"/><rect x="160" y="200" width="40" height="60" rx="2"/><rect x="0" y="300" width="40" height="60" rx="2"/><rect x="70" y="300" width="58" height="60" rx="2"/><rect x="160" y="300" width="40" height="70" rx="2"/></g>
      <g stroke="#fff" stroke-linecap="round" fill="none"><path d="M-10 86H210M-10 180H210M-10 285H210" stroke-width="12"/><path d="M55 -10V410M145 -10V410" stroke-width="12"/><path d="M100 -10V410" stroke-width="7"/></g>
      <path d="M-10 380 210 330" stroke="#F6D88B" stroke-width="9" fill="none"/>
      <g fill="#7E8C95" font-size="7.2" font-family="IBM Plex Sans Arabic,Tahoma,sans-serif" text-anchor="middle"><text x="172" y="176">شارع قريش</text><text x="28" y="281">شارع أبو يزيد</text><text x="60" y="372" transform="rotate(-14 60 372)" fill="#A1823A">طريق الملك عبدالعزيز</text></g>
      <circle class="zone" cx="100" cy="180" r="30" fill="#D23F45" fill-opacity=".14" stroke="#D23F45" stroke-opacity=".5" stroke-width="1.2"/>
      <circle class="zone z2" cx="145" cy="285" r="20" fill="#E7A23A" fill-opacity=".14" stroke="#E7A23A" stroke-opacity=".5" stroke-width="1.2"/>
      <path class="route" pathLength="1" d="M100 392V285H55V86H100V-10" fill="none" stroke="#3A7CA5" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
      <circle r="5.5" fill="#3A7CA5" stroke="#fff" stroke-width="2.4"><animateMotion dur="9s" repeatCount="indefinite" keyPoints="0;0;1;1" keyTimes="0;0.22;0.7;1" calcMode="linear" path="M100 392V285H55V86H100V-10"/></circle>
    </svg>
    <span class="mpin r" style="--x:50%;--y:45%">{svg(I_PIN)}</span><span class="mpin a" style="--x:72.5%;--y:71.25%">{svg(I_PIN)}</span>
    <div class="mtop">{svg(I_BACK)}<span>الاتجاهات</span></div>
    <div class="msheet"><div class="row"><span class="pill r">خطير</span><b>شارع قريش</b></div><span class="t3">ارتفاع الماء 80 سم · المسار يتجنّب الشارع</span><div class="btn">ابدأ</div></div>
  </div>''', lg=True)

# the illustrations on the safety cards, simplified from the report's art
ILLO = [
  ('عدم الاقتراب من تجمعات المياه، فعادة ما تكون حوافها قابلة للانهيار',
   '<path d="M8 74c4.7-3.6 9.3-3.6 14 0s9.3 3.6 14 0 9.3-3.6 14 0 9.3 3.6 14 0 9.3-3.6 14 0 9.3 3.6 14 0" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>'
   '<circle cx="50" cy="44" r="21" fill="#E2434A"/><circle cx="50" cy="44" r="21" fill="none" stroke="#fff" stroke-width="3"/><rect x="36" y="40" width="28" height="8" rx="2" fill="#fff"/>'),
  ('اتبع المسارات والطرق المستخدمة قدر الإمكان',
   '<path d="M22 30l18-7 20 7 18-7v48l-18 7-20-7-18 7z" fill="#F7F3E8"/><path d="M40 23v48M60 30v48" stroke="#D9CFB4" stroke-width="2"/>'
   '<path d="M26 58c8-10 16 4 24-6s14-6 24-14" fill="none" stroke="#3A7CA5" stroke-width="3" stroke-dasharray="4 4" stroke-linecap="round"/>'
   '<path d="M64 20c-6 0-10 4.6-10 10 0 7.6 10 17 10 17s10-9.4 10-17c0-5.4-4-10-10-10z" fill="#E2434A"/><circle cx="64" cy="30" r="3.6" fill="#fff"/>'),
  ('لا تجازف بالجلوس في مجاري السيول أو عبورها',
   '<path d="M24 54l6-12a5 5 0 0 1 4.5-3h31a5 5 0 0 1 4.5 3l6 12z" fill="#F4F6F8"/><rect x="20" y="52" width="60" height="12" rx="4" fill="#F4F6F8"/>'
   '<path d="M8 66c6-4 12-4 18 0s12 4 18 0 12-4 18 0 12 4 18 0 12-4 18 0V92H8z" fill="#2F6F95"/>'
   '<circle cx="72" cy="28" r="12" fill="#E2434A"/><circle cx="72" cy="28" r="12" fill="none" stroke="#fff" stroke-width="2.4"/><path d="M64 20l16 16" stroke="#fff" stroke-width="3"/>'),
]

def safety():
    blob = '<path d="M50 6c18 0 36 9 40 26s-4 34-18 44-34 12-48 2S4 50 8 32 32 6 50 6z" fill="#74A8C4"/>'
    slides = ''.join(f'<div class="sl"><svg class="illo" viewBox="0 0 100 100" aria-hidden="true">{blob}{art}</svg><p>{txt}</p></div>' for txt, art in ILLO)
    dots = ''.join(f'<i style="--k:{k}"></i>' for k in range(3))
    return phone(f'''{top('إرشادات السلامة')}
  <div class="car"><div class="trk">{slides}</div></div>
  <div class="dots">{dots}</div>
  <div class="pager"><span>رجوع</span><span>التالي</span></div>''')

def sensor():
    ticks = ''.join(f'<span style="--y:{v}%"><b>{v}</b></span>' for v in (0, 25, 50, 75, 100))
    return f'''<div class="sensor" dir="rtl" lang="ar"><span class="glow" aria-hidden="true"></span><p class="t3">نقطة تجمّع المياه</p><p class="h5">شارع قريش</p>
  <div class="gauge"><div class="tube"><div class="wfill"><svg viewBox="0 0 120 10" preserveAspectRatio="none" aria-hidden="true"><path d="M0 5q7.5-5 15 0t15 0 15 0 15 0 15 0 15 0 15 0 15 0V10H0z"/></svg></div></div><div class="scale">{ticks}</div>
    <div class="read"><b></b><span>سم</span><span class="pill r">خطير</span></div></div>
  <p class="ok"><i></i>حسّاس منسوب المياه · مباشر</p></div>'''


# ── laptop panels ────────────────────────────────────────────────────────────────────────────

def laptop(inner):
    return f'<div class="lp"><div class="lid"><div class="bez"><span class="camn"></span><div class="disp">{inner}</div></div></div><div class="base"></div></div>'

LOG = [('p', 'PS C:\\tawaqaa&gt; python -m unittest'),
       ('', '0: 480x640 1 flooded car, 118.8ms'),
       ('m', 'Speed: 2.1ms preprocess, 118.8ms inference, 0.0ms postprocess per image at shape (1, 3, 480, 640)'),
       ('g', "Test Result: PASS - Detected 'flooded car'"),
       ('', '0: 480x640 1 human in flood, 164.2ms'),
       ('m', 'Speed: 2.0ms preprocess, 164.2ms inference, 0.0ms postprocess per image at shape (1, 3, 480, 640)'),
       ('g', "Test Result: PASS - Detected 'human in flood'"),
       ('m', '----------------------------------------------------------------------'),
       ('', 'Ran 2 tests in 63.005s'),
       ('g', 'OK')]

def detect():
    """The webcam test from the report: cv2 window "Webcam" with supervision's box and label
    annotators (class name only, default palette), and the unittest output beside it."""
    lines = ''.join(f'<p class="{c}" style="--k:{k}">{t}</p>' for k, (c, t) in enumerate(LOG))
    return f'''<div class="pn det" lang="en">
  <div class="cvw"><div class="cvt"><svg viewBox="0 0 16 16" aria-hidden="true"><rect x="1" y="3" width="14" height="10" rx="2" fill="#5B8DEF"/><circle cx="8" cy="8" r="2.6" fill="#fff"/></svg><span>Webcam</span><i>&#8212;</i><i>&#9633;</i><i>&#10005;</i></div>
    <div class="cvf">
      <svg viewBox="0 0 640 480" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
        <defs>
          <linearGradient id="tqs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B4247"/><stop offset=".55" stop-color="#555A58"/><stop offset="1" stop-color="#6A6A62"/></linearGradient>
          <linearGradient id="tqw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6E6553"/><stop offset=".4" stop-color="#4E4637"/><stop offset="1" stop-color="#2D2820"/></linearGradient>
          <linearGradient id="tqb" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3C444C"/><stop offset=".5" stop-color="#1D2329"/><stop offset="1" stop-color="#101418"/></linearGradient>
          <radialGradient id="tql"><stop offset="0" stop-color="#FFF4D6"/><stop offset=".35" stop-color="#FFD98A" stop-opacity=".55"/><stop offset="1" stop-color="#FFD98A" stop-opacity="0"/></radialGradient>
          <filter id="tqblur" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="3"/></filter>
          <filter id="tqsoft"><feGaussianBlur stdDeviation="1.1"/></filter>
          <filter id="tqgrain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  0 0 0 .55 0"/></filter>
          <radialGradient id="tqv" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>
        </defs>
        <rect width="640" height="480" fill="url(#tqs)"/>
        <g filter="url(#tqblur)">
          <path d="M0 250V150l40-10 30 14 40-30 50 22 30-8 10 112z" fill="#2E3431"/>
          <path d="M210 250V120h120v130zM330 250V160l40-30 40 30v90z" fill="#4A4A47"/><path d="M200 128l70-48 72 48z" fill="#5A3B33"/>
          <g fill="#C9B88E" opacity=".55"><rect x="228" y="150" width="20" height="26"/><rect x="290" y="150" width="20" height="26"/><rect x="350" y="180" width="16" height="22"/></g>
          <path d="M420 250V170c30-40 70-60 120-50s100 30 100 60v70z" fill="#2B312C"/>
          <path d="M150 250c10-50 40-70 60-70" stroke="#26291F" stroke-width="10" fill="none"/>
        </g>
        <rect x="0" y="244" width="640" height="18" fill="#3D403B" filter="url(#tqsoft)"/>
        <g filter="url(#tqsoft)">
          <path d="M60 262c20-8 70-10 110-4" stroke="#7E8A8F" stroke-width="10" fill="none" opacity=".5"/>
          <path d="M70 258l8-14h70l16 14z" fill="#5E7E9B" opacity=".7"/>
        </g>
        <rect y="262" width="640" height="218" fill="url(#tqw)"/>
        <g class="cvwave" fill="none" stroke="#9C9076" stroke-opacity=".35" stroke-width="2"><path d="M-40 300c40-6 80 6 120 0s80-6 120 0 80 6 120 0 80-6 120 0 80 6 120 0 80-6 120 0"/><path d="M-40 352c40-8 80 8 120 0s80-8 120 0 80 8 120 0 80-8 120 0 80 8 120 0 80-8 120 0" stroke-opacity=".25"/><path d="M-40 410c40-10 80 10 120 0s80-10 120 0 80 10 120 0 80-10 120 0 80 10 120 0 80-10 120 0" stroke-opacity=".2"/></g>
        <!-- the car: a dark sedan pushing through the water, headlights on -->
        <g>
          <path d="M120 318c4-22 16-34 42-40l52-28c18-9 34-12 62-12h52c30 0 52 10 74 30l24 14c26 4 40 12 44 30l2 14H118z" fill="url(#tqb)"/>
          <path d="M228 254c16-8 30-10 52-10h40l8 46h-118zM338 244h4c22 0 38 8 56 24l8 22h-60z" fill="#121619"/>
          <path d="M240 258c12-5 24-6 40-6h30l4 20h-84z" fill="#3F4A55" opacity=".35"/>
          <path d="M130 300h340" stroke="#59636B" stroke-width="2" opacity=".6"/>
          <ellipse cx="452" cy="306" rx="16" ry="7" fill="#FFF6DF"/><circle cx="452" cy="306" r="44" fill="url(#tql)"/>
          <path d="M300 300h14" stroke="#2A3036" stroke-width="3"/>
        </g>
        <path d="M100 330c40-10 120-6 200-2s180 8 230 0l40 6v40H100z" fill="#5A503F"/>
        <g filter="url(#tqsoft)" fill="#D8D2C2"><path d="M430 328c20-16 46-20 70-6 16 10 30 8 40 2-6 14-30 24-60 22-22-2-38-8-50-18z" opacity=".75"/><path d="M110 334c18-10 40-10 54-2-12 8-34 10-54 2z" opacity=".5"/><ellipse cx="300" cy="334" rx="120" ry="5" opacity=".35"/></g>
        <path d="M452 336c-2 30 4 70 2 110" stroke="url(#tql)" stroke-width="22" opacity=".4" filter="url(#tqblur)"/>
        <!-- the person, waist-deep -->
        <g transform="translate(-40 0)">
          <circle cx="568" cy="268" r="11" fill="#2A2724"/>
          <path d="M553 282c4-4 26-4 30 0l6 50h-42z" fill="#2F3B46"/>
          <path d="M555 288l-14 18M581 288l16 14" stroke="#2F3B46" stroke-width="8" stroke-linecap="round"/>
          <ellipse cx="568" cy="333" rx="30" ry="4" fill="none" stroke="#B8AE96" stroke-opacity=".55" stroke-width="2"/>
        </g>
        <g class="cvrain" stroke="#E8ECEE" stroke-opacity=".22" stroke-width="1"><path d="M40 0l-14 60M130 30l-14 60M210 -10l-14 60M300 40l-14 60M390 0l-14 60M470 50l-14 60M560 10l-14 60M620 60l-14 60M80 150l-14 60M260 140l-14 60M440 160l-14 60M600 170l-14 60"/></g>
        <rect width="640" height="480" filter="url(#tqgrain)" opacity=".16"/>
        <rect width="640" height="480" fill="url(#tqv)"/>
        <!-- supervision annotations -->
        <g class="bx b1"><rect x="112" y="232" width="384" height="112" fill="none" stroke="#A351FB" stroke-width="3"/><rect x="112" y="210" width="106" height="22" fill="#A351FB"/><text x="120" y="226" fill="#fff" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="15">flooded car</text></g>
        <g class="bx b2"><rect x="494" y="252" width="66" height="84" fill="none" stroke="#FF4040" stroke-width="3"/><rect x="494" y="230" width="124" height="22" fill="#FF4040"/><text x="501" y="246" fill="#fff" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="15">human in flood</text></g>
      </svg>
    </div>
  </div>
  <div class="term"><div class="tt"><span>PROBLEMS</span><span>OUTPUT</span><span class="on">TERMINAL</span></div><div class="tl">{lines}<p class="cur" style="--k:10"></p></div></div>
</div>'''

ROWS = [('h', 'خطير', 'شارع قريش', '39.1823', '21.4858', '80 سم', '15'),
        ('h', 'خطير', 'شارع فلسطين', '39.1736', '21.5312', '55 سم', '9'),
        ('m', 'متوسط', 'شارع أبو يزيد', '39.2104', '21.5121', '30 سم', '2')]

def console():
    """The authorities' page: reports from Firebase in one table, high-risk and medium rows tinted,
    and the delete flow with its confirmation and success message."""
    rows = ''.join(f'<div class="tr {c}{" gone" if k == 2 else ""}"><span class="cb"></span><span class="st">{lv}</span><b>{s}</b><span>{lo}</span><span>{la}</span><span>{w}</span><span>{n}</span></div>'
                   for k, (c, lv, s, lo, la, w, n) in enumerate(ROWS))
    return f'''<div class="pn web" dir="rtl" lang="ar">
  <div class="wb"><span class="url">توقّى · الجهات المختصة</span><i></i><i></i><i></i></div>
  <div class="wbody">
    <div class="whead">{logo('tqlogo lg')}</div>
    <div class="wcard">
      <p class="wlink">لمشاهدة لوحة المعلومات للبلاغات <span>اضغط هنا</span></p>
      <div class="tbl"><div class="tr hd"><span></span><span>مستوى الخطر</span><span>الشارع</span><span>خط الطول</span><span>خط العرض</span><span>مستوى الماء</span><span>عدد البلاغات</span></div>{rows}</div>
    </div>
  </div>
  <div class="modal"><svg viewBox="0 0 48 28" aria-hidden="true"><path d="M4 18c6-8 12-8 18 0s12 8 18 0" fill="none" stroke="#1F4E6B" stroke-width="6" stroke-linecap="round"/><path d="M8 8c6-6 12-6 18 0s12 6 18 0" fill="none" stroke="#1F4E6B" stroke-width="6" stroke-linecap="round"/></svg>
    <p>هل أنت متأكد أنك تريد حذف الإنذار؟</p><div class="mbar"><span class="yes">نعم</span><span>إلغاء</span></div></div>
  <div class="wtoast">{CHECK_BADGE}<span>تم حذف الإنذار بنجاح</span></div>
</div>'''


def beams():
    """Raindrops that fall and splash on the floor of the stage (after Aceternity's beams with collision)."""
    drops = [(8, 4.2, 0), (19, 5.6, 2.1), (31, 4.8, 3.4), (46, 6.2, 1.1), (58, 5.0, 4.0), (69, 4.4, 0.6), (81, 5.8, 2.8), (92, 4.6, 1.7)]
    return '<div class="tq-rain" aria-hidden="true">' + ''.join(
        f'<span style="--x:{x}%;--d:{d}s;--w:-{w}s"><i></i><b></b><em></em><em></em><em></em></span>' for x, d, w in drops) + '</div>'


CARD = f'<div class="tq" aria-hidden="true">{beams()}{report()}{home()}{alerts()}</div>'

SHOTS_RAW = [
 ('01 · Report', 'Pick the street from the list or drop a pin on the map, and the report goes to the authorities.', f'<div class="tq">{beams()}{home()}{report()}</div>'),
 ('02 · Alerts', 'Every alert shows the street, its danger level and how high the water is. A submersible sensor measures the worst spot.', f'<div class="tq">{beams()}{alerts()}{sensor()}</div>'),
 ('03 · Directions', 'Reported streets show up on the map in red and amber, and the route goes around them.', f'<div class="tq">{beams()}{mapscr()}{safety()}</div>'),
 ('04 · Detect', 'Our YOLOv10 model watching a webcam feed. It was trained on 1,532 photos of flooded cars and 171 of people in floodwater.', f'<div class="tq">{beams()}{laptop(detect())}</div>'),
 ('05 · Respond', 'Authorities see every report in one table, riskiest first, and delete it once the street is clear.', f'<div class="tq">{beams()}{laptop(console())}</div>'),
]

SHOTS = [(l, h, c) for l, c, h in SHOTS_RAW]
