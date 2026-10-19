"""Mizan scenes: the app's screens drawn in HTML and CSS for the home card and the project page.

Copy, colours and layout follow the Android app (github.com/lujainaloufi0/Mizan): Arabic, right to left,
obsidian canvas with sand and mint. Prices and counts are sample data for one week. Every class is
prefixed with z- so the Tawaqaa scene styles never reach these screens.
"""

SB = '<div class="sb"><span>9:41</span><i>5G</i></div>'


def svg(path, cls='zi'):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>')


I_CLOCK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
I_USERS = '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/>'
I_GLOBE = '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/>'
I_SUN = '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
I_MOON = '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>'
I_SWAP = '<path d="M7 7h13l-3.5-3.5M17 17H4l3.5 3.5"/>'
I_CHECK = '<path d="m5 12.5 4.5 4.5L19 7"/>'
I_CHEF = '<path d="M7 18h10v3H7zM7 18v-4.4A4 4 0 1 1 9.2 6a4 4 0 0 1 5.6 0A4 4 0 1 1 17 13.6V18"/>'
I_COPY = '<rect x="8" y="3" width="8" height="4" rx="1"/><path d="M8 5H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-2"/>'
I_SEND = '<path d="M21 3 10 14M21 3l-6.5 18-4.5-7-7-4.5z"/>'
I_CAL = '<rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>'
I_HOME = '<path d="M4 11 12 4l8 7v9H4z"/><path d="M10 20v-5h4v5"/>'
I_LIST = '<path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>'
I_USER = '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>'
I_PIGGY = '<path d="M5 11a7 6 0 0 1 12.5-3.5H20v4l-1.6 1A7 6 0 0 1 15 17v3h-3v-2h-2v2H7v-3.3A6 6 0 0 1 5 11z"/><path d="M15.5 10h.01"/>'
I_WALLET = '<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M16 13h.01M3 10h18"/>'
I_STORE = '<path d="M3.5 9 5 4h14l1.5 5M4.5 9v11h15V9M3.5 9h17M9.5 20v-5h5v5"/>'
I_BAN = '<circle cx="12" cy="12" r="9"/><path d="m5.6 5.6 12.8 12.8"/>'
DISH = '<path d="M3 11h18a9 9 0 0 1-18 0z"/><path d="M8.5 7.5c0-1.5 1-2 1-3.5M12.5 7.5c0-1.5 1-2 1-3.5"/>'
LEAF = '<path d="M5 19c0-8 5-14 15-14 0 10-6 15-14 15"/><path d="M5 19 13 11"/>'
DROP = '<path d="M12 3s6 6.4 6 10.5A6 6 0 0 1 6 13.5C6 9.4 12 3 12 3z"/>'
EGG = '<path d="M12 3c3.6 0 6.5 5.6 6.5 10a6.5 6.5 0 0 1-13 0C5.5 8.6 8.4 3 12 3z"/>'
GRAIN = '<path d="M12 21V9M12 9c-3-1-4-3.5-4-6 3 0 4 2 4 6zm0 0c3-1 4-3.5 4-6-3 0-4 2-4 6zM12 15c-3-1-4-3.5-4-6M12 15c3-1 4-3.5 4-6"/>'

# the spoon-and-pivot mark, same paths as MizanMark in app/src/ui/brand.tsx
MARK = ('<svg class="z-mark" viewBox="205 207 640 640" aria-hidden="true">'
        '<path d="M230 400C230 330 310 310 360 360C410 410 390 490 310 510C250 530 230 460 230 400Z" fill="var(--z-sand)"/>'
        '<path d="M320 460C420 640 680 640 794 400" fill="none" stroke="var(--z-sand)" stroke-width="52" stroke-linecap="round"/>'
        '<circle cx="512" cy="680" r="44" fill="var(--z-mint)"/></svg>')


def wordmark():
    return f'<span class="z-wm">{MARK}<b>مِيزان</b></span>'


def tabbar(on):
    tabs = [('home', I_HOME, 'الرئيسية'), ('week', I_CAL, 'الأسبوع'), ('list', I_LIST, 'المقاضي'), ('me', I_USER, 'ملفي')]
    return '<div class="z-tabs">' + ''.join(f'<span class="{"on" if k == on else ""}">{svg(i)}<em>{t}</em></span>' for k, i, t in tabs) + '</div>'


def pill(icon, label, strong=False):
    return f'<span class="z-pill{" st" if strong else ""}">{svg(icon)}{label}</span>'


def phone(body, light=False, lg=False):
    return (f'<div class="iph z-ph{" lg" if lg else ""}"><div class="scr z-scr{" light" if light else ""}" lang="ar" dir="rtl">'
            f'{SB}{body}</div></div>')


def tile(icon=DISH, size=''):
    return f'<span class="z-tile{(" " + size) if size else ""}">{svg(icon)}</span>'


def recipe_card(compact=True):
    macros = '' if compact else (
        '<div class="z-mac"><span><b>622</b>سعرة</span><span><i style="--c:var(--z-mint)"></i><b>38غ</b>بروتين</span>'
        '<span><i style="--c:var(--z-sand-dim)"></i><b>68غ</b>كربوهيدرات</span><span><i style="--c:var(--z-clay)"></i><b>22غ</b>دهون</span></div>')
    return f'''<div class="z-rc">
    <div class="z-pills">{pill(I_SUN, 'غداء', True)}{pill(I_CLOCK, '50 دقيقة')}{pill(I_USERS, '4 حصص')}{pill(I_GLOBE, 'سعودي')}</div>
    <div class="z-ttl">{tile()}<b>كبسة دجاج</b><span class="z-cost"><b>9.80</b><em>ر.س للحصة</em></span></div>
    {macros}
    <div class="z-acts"><span class="z-b mint z-cook">{svg(I_CHEF)}تم الطبخ</span><span class="z-b">{svg(I_SWAP)}بدّل</span><span class="z-b sq">{svg(I_BAN)}</span></div>
  </div>'''


def budget_card(cls=''):
    return f'''<div class="z-bc {cls}">
    <span class="z-kick">سلة هذا الأسبوع</span>
    <div class="z-fig"><b>412</b><em>ر.س</em></div>
    <span class="z-t3">من ميزانية 500 ر.س · 82%</span>
    <div class="z-bar"><span></span></div>
    <div class="z-stats"><span class="z-s mint">{svg(I_PIGGY)}<em>وفّرت</em><b>36 <i>ر.س</i></b></span><span class="z-s">{svg(I_WALLET)}<em>المتبقي</em><b>88 <i>ر.س</i></b></span></div>
  </div>'''


def home(light=False, lg=True, cook=True):
    toast = (f'<div class="z-toast">{svg(I_CHEF)}بالعافية! خصمنا مقادير «كبسة دجاج» من مطبخك</div>') if cook else ''
    return phone(f'''
  <div class="z-hd"><div><span class="z-t3">صباح الخير</span>{wordmark()}</div>
    <span class="z-ring{" go" if cook else ""}"><svg viewBox="0 0 36 36"><circle cx="18" cy="18" r="15.5"/><circle class="pr" cx="18" cy="18" r="15.5" pathLength="100"/></svg><b></b></span></div>
  <div class="z-today"><div><span class="z-kick">اليوم · الأحد</span><p class="z-disp">وش نطبخ؟</p></div><span class="z-t3">طبخت 3 من 14 وجبة</span></div>
  <div class="{"z-cooking" if cook else ""}">{recipe_card()}</div>
  <div class="z-allw">{svg(I_CAL)}كل وجبات الأسبوع</div>
  {budget_card()}
  {toast}
  {tabbar("home")}''', light, lg)


def scale_svg():
    return '''<svg class="z-scale" viewBox="0 0 320 176" aria-hidden="true">
      <path d="M160 48V160M120 164H200" stroke="var(--z-sand-dim)" stroke-width="2" stroke-linecap="round"/>
      <g class="z-beam"><path d="M48 48H272" stroke="var(--z-sand)" stroke-width="2.5" stroke-linecap="round"/>
        <g transform="translate(272 48)"><g class="z-pan"><path d="M0 0 L-32 40 M0 0 L32 40" stroke="var(--z-sand-dim)" stroke-width="1.25"/><path d="M-40 40H40A40 18 0 0 1-40 40Z" fill="rgba(16,185,129,.12)" stroke="var(--z-mint)" stroke-width="2"/></g></g>
        <g transform="translate(48 48)"><g class="z-pan"><path d="M0 0 L-32 40 M0 0 L32 40" stroke="var(--z-sand-dim)" stroke-width="1.25"/><path d="M-40 40H40A40 18 0 0 1-40 40Z" fill="rgba(229,212,192,.08)" stroke="var(--z-sand)" stroke-width="2"/></g></g></g>
      <circle cx="160" cy="48" r="7" fill="var(--z-canvas)" stroke="var(--z-sand)" stroke-width="2"/><circle cx="160" cy="48" r="2.5" fill="var(--z-mint)"/>
    </svg>'''


def wizard(lg=False):
    return phone(f'''
  <div class="z-wtop"><span class="z-t3">أسبوع جديد · 3 من 4</span><div class="z-steps"><i class="on"></i><i class="on"></i><i class="on"></i><i></i></div></div>
  <p class="z-h2">الأسرة والميزانية</p>
  <div class="z-hh"><span class="z-cnt"><em>البالغون</em><b>2</b></span><span class="z-cnt"><em>الأطفال</em><b>2</b></span></div>
  <div class="z-scalebox">{scale_svg()}
    <div class="z-legs"><span><i style="--c:var(--z-sand)"></i>سلة متوقعة<b>486 ر.س</b></span><span><i style="--c:var(--z-mint)"></i>الميزانية<b class="z-bud"> ر.س</b></span></div>
  </div>
  <div class="z-slider"><span class="z-trk"><span class="z-fil"></span></span><span class="z-thumb"></span></div>
  <p class="z-hint">تنوّع كامل، والسلة تقريباً بقدر ميزانيتك.</p>
  <p class="z-note">تقدر تبدّل أي وجبة من صفحة الأسبوع.</p>
  <div class="z-cta z-b mint">اصنع خطتي</div>''', lg=lg)


def week():
    days = [('الأحد', [('غداء', I_SUN, 'كبسة دجاج', '50 د · 622 سعرة · 38غ بروتين', True)]),
            ('الإثنين', [('غداء', I_SUN, 'مقلوبة', '60 د · 580 سعرة · 32غ بروتين', False), ('عشاء', I_MOON, 'شوربة عدس', '30 د · 340 سعرة · 18غ بروتين', False)]),
            ('الثلاثاء', [('غداء', I_SUN, 'جريش بالدجاج', '70 د · 470 سعرة · 32غ بروتين', False)]),
            ('الأربعاء', [('عشاء', I_MOON, 'مندي دجاج', '75 د · 640 سعرة · 41غ بروتين', False)])]
    out, k = '', 0
    for d, meals in days:
        out += f'<p class="z-dayh">{d}</p>'
        for slot, ic, name, meta, done in meals:
            ok = svg(I_CHECK, 'zi z-ok') if done else ''
            out += f'<div class="z-wi{" done" if done else ""}" style="--k:{k}">{tile()}<div><b>{name}</b><span class="z-t3">{slot} · {meta}</span></div>{ok}</div>'
            k += 1
    return phone(f'''
  <div class="z-hd"><div><span class="z-t3">14 وجبة · 4 حصص لكل وجبة</span><p class="z-h2">وصفات الأسبوع</p></div></div>
  <div class="z-wk">{out}</div>
  {tabbar("week")}''')


SWAPS = [('مقلوبة', 'من سلتك', '−3.20'), ('مندي دجاج', 'من سلتك', '+1.10'), ('صالونة خضار', 'سعودي', '−4.60')]


def swap_option(k, n, t, d, pick=False):
    return f'<div class="z-op{" pick" if pick else ""}" style="--k:{k}">{tile(size="sm")}<div><b>{n}</b><span class="z-t3">{t}</span></div><span class="z-dlt">{d} <i>ر.س</i></span></div>'


def swap():
    o = ''.join(swap_option(k, n, t, d, k == 0) for k, (n, t, d) in enumerate(SWAPS))
    return phone(f'''
  <div class="z-hd"><div><span class="z-kick">الإثنين · غداء</span><p class="z-h2">اختر وجبتك</p></div></div>
  {recipe_card(compact=False)}
  <div class="z-tray"><span class="z-t3">بدائل سريعة · مرتّبة حسب المتوفر في سلتك</span>{o}</div>
  <div class="z-toast">{svg(I_SWAP)}مقلوبة بدل كبسة دجاج · السلة −3.20 ر.س</div>''')


AISLES = [('الخضار والفواكه', LEAF, '#7FB069', [('بصل', '× 1 كيس', '4.50', 1), ('طماطم', '× 2 كغ', '7.00', 1), ('ثوم', '× 1 علبة', '3.25', 1)]),
          ('اللحوم والدواجن', DROP, '#E8805F', [('دجاج كامل', '× 3 حبة', '57.00', 0)]),
          ('الأرز والحبوب', GRAIN, '#E5D4C0', [('أرز بسمتي', '× 1 كيس 5 كغ', '39.95', 0), ('جريش', '× 1 كيس', '8.50', 0)]),
          ('الألبان والبيض', EGG, '#9CC3E6', [('لبن', '× 2 علبة', '9.00', 0)])]


def grocery():
    out, k = '', 0
    for name, ic, hue, items in AISLES:
        out += f'<p class="z-aisle"><span class="z-tile xs" style="--h:{hue}">{svg(ic)}</span>{name}</p>'
        for n, pk, pr, auto in items:
            out += f'<div class="z-gi{" tick" if auto else ""}" style="--k:{k}"><span class="z-cb">{svg(I_CHECK)}</span><b>{n}</b><span class="z-t3">{pk}</span><span class="z-pr">{pr}</span></div>'
            k += auto
    return phone(f'''
  <div class="z-hd"><div><span class="z-t3">للشراء · 23 صنف</span><p class="z-h2">المقاضي</p></div><span class="z-tg">{svg(I_STORE)}حسب المتجر</span></div>
  <div class="z-seg"><span class="on">المقاضي</span><span>في مطبخي</span></div>
  <div class="z-gl">{out}</div>
  <div class="z-foot"><span class="z-b">{svg(I_COPY)}انسخ القائمة</span><span class="z-b mint">{svg(I_SEND)}أرسل</span></div>
  {tabbar("list")}''')


APPS = [('هنقرستيشن', '#F5C400', '#1a1a1a'), ('نعناع', '#1FA35B', '#fff'), ('نينجا', '#6C2BD9', '#fff'), ('كيتا', '#FFD43B', '#1a1a1a'),
        ('تويو', '#2B6CF6', '#fff'), ('جاهز', '#E53935', '#fff'), ('مرسول', '#0FB5AE', '#fff')]


def delivery():
    rows = ''.join(f'<div class="z-gi"><span class="z-cb"></span><b>{n}</b><span class="z-t3">{pk}</span><span class="z-pr">{pr}</span></div>' for _, _, _, it in AISLES for n, pk, pr, _ in it)
    a = ''.join(f'<div class="z-app" style="--k:{k}"><span class="z-ai" style="background:{bg};color:{fg}">{n[0]}</span><b>{n}</b></div>' for k, (n, bg, fg) in enumerate(APPS))
    return phone(f'''
  <div class="z-dim">
    <div class="z-hd"><div><span class="z-t3">للشراء · 23 صنف</span><p class="z-h2">المقاضي</p></div></div>
    <div class="z-gl">{rows}</div>
  </div>
  <div class="z-sheet"><span class="z-grab"></span><p class="z-h3">أرسل للتوصيل</p>
    <span class="z-t3">ننسخ القائمة ونفتح التطبيق اللي تختاره.</span>
    <div class="z-apps">{a}</div></div>
  <div class="z-toast top">{svg(I_COPY)}نُسخت القائمة مرتّبة حسب الأقسام</div>''')


def profile():
    rows = [('الهدف', 'بروتين عالي'), ('الحساسية', 'الفول السوداني'), ('أجهزة المطبخ', 'فرن · قلاية هوائية'),
            ('دائماً عندي', 'أرز · زيت · بهارات'), ('قائمة الاستبعاد', 'لا شيء')]
    r = ''.join(f'<div class="z-prow"><em>{a}</em><b>{b}</b></div>' for a, b in rows)
    return phone(f'''
  <div class="z-hd"><div><span class="z-t3">محفوظ على جوالك</span><p class="z-h2">ملفي</p></div></div>
  <div class="z-pf">{r}</div>
  <p class="z-lab">المظهر</p>
  <div class="z-seg3"><i class="z-hl"></i><span>تلقائي</span><span class="lt">فاتح</span><span class="dk">داكن</span></div>
  {tabbar("me")}''')


# floating cards pulled out of the UI, the way product shots present a feature beside the phone
def fl(cls, inner, light=False):
    return f'<div class="z-fl {cls}{" light" if light else ""}" lang="ar" dir="rtl">{inner}</div>'


FL_BUDGET = fl('f-bud', '<span class="z-kick">الميزانية</span><div class="z-fig"><b class="z-bud"></b><em>ر.س</em></div><span class="z-t3">4 أشخاص · 6 متاجر</span>')
FL_CUISINE = fl('f-cui', '<span class="z-kick">المطابخ</span><div class="z-chips"><span class="on">سعودي</span><span class="on">شامي</span><span>يمني</span><span>مصري</span><span>إيطالي</span><span>+13</span></div>')
FL_BASKET = fl('f-bask', budget_card('flat'))
FL_COOKED = fl('f-cooked', f'{svg(I_CHEF)}<div><b>تم الطبخ</b><span class="z-t3">خصمنا المقادير من مطبخك</span></div>')
FL_MACRO = fl('f-mac', '<span class="z-kick">كبسة دجاج · للحصة</span><div class="z-mac big"><span><b>622</b>سعرة</span><span><i style="--c:var(--z-mint)"></i><b>38غ</b>بروتين</span><span><i style="--c:var(--z-sand-dim)"></i><b>68غ</b>كربوهيدرات</span></div>')
FL_FILTER = fl('f-filt', '<span class="z-kick">نستبعد تلقائياً</span><div class="z-chips"><span>الفول السوداني</span><span>بدون فرن</span><span>أطباق استبعدتها</span></div>')
FL_SWAP = fl('f-swap', '<span class="z-kick">بدّل</span>' + ''.join(swap_option(k, n, t, d, k == 0) for k, (n, t, d) in enumerate(SWAPS[:2])))
FL_AISLE = fl('f-aisle', '<span class="z-kick">حسب المتجر</span><div class="z-stores">' + ''.join(f'<span><i>{s[0]}</i>{s}</span>' for s in ['كارفور', 'بنده', 'العثيم', 'الدانوب', 'التميمي', 'لولو']) + '</div>')
FL_APPS = fl('f-apps', '<span class="z-kick">7 تطبيقات توصيل</span><div class="z-dots">' + ''.join(f'<i style="background:{bg};color:{fg}">{n[0]}</i>' for n, bg, fg in APPS) + '</div>')
FL_THEME = fl('f-theme', '<span class="z-kick">ألوان مِيزان</span><div class="z-sw"><i style="--c:#121417"></i><i style="--c:#E5D4C0"></i><i style="--c:#10B981"></i><i style="--c:#F6F3EE"></i><i style="--c:#7A5C3A"></i><i style="--c:#047857"></i></div>')

CARD = f'<div class="mz mz-card" aria-hidden="true">{wizard()}{home(cook=False)}{grocery()}</div>'

SHOTS_RAW = [
    ('01 · Plan', 'Pick cuisines, stores and a weekly budget in SAR. The scale weighs the expected basket against the budget as the slider moves.',
     f'<div class="mz">{FL_CUISINE}{wizard(lg=True)}{FL_BUDGET}</div>'),
    ('02 · Today', "Home opens on today's meals and the week's basket. Marking a meal as cooked takes its ingredients out of the kitchen.",
     f'<div class="mz">{FL_COOKED}{home()}{FL_BASKET}</div>'),
    ('03 · Week', 'Every meal in the week, with time, calories and protein, filtered by your allergies, appliances, goal and banned dishes.',
     f'<div class="mz">{FL_FILTER}{week()}{FL_MACRO}</div>'),
    ('04 · Swap', 'Swap any meal. The three quick options are ranked by what the basket already covers, with the price change for each.',
     f'<div class="mz">{swap()}{FL_SWAP}</div>'),
    ('05 · Shop', 'The grocery list is sorted by aisle and can split by store. Ticked items move into the kitchen view.',
     f'<div class="mz">{FL_AISLE}{grocery()}</div>'),
    ('06 · Deliver', 'Send copies the list and opens the delivery app you pick.',
     f'<div class="mz">{delivery()}{FL_APPS}</div>'),
    ('07 · Theme', 'The profile is asked once and saved on the phone. Appearance switches between automatic, light and dark.',
     f'<div class="mz">{profile()}{FL_THEME}{home(light=True, lg=False, cook=False)}</div>'),
]

SHOTS = [(l, h, c) for l, c, h in SHOTS_RAW]
