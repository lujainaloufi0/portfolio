"""Tawaqaa scenes: HTML for the home card and the project-page shots."""

SB = '<div class="sb"><span>9:41</span><i>5G</i></div>'

def svg(path, extra=''):
    return f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{path}</svg>'

I_REPORT = '<path d="M12 3s6 6.4 6 10.5A6 6 0 0 1 6 13.5C6 9.4 12 3 12 3z"/><path d="M12 11v4M12 17.5v.01"/>'
I_MAP = '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2z"/><path d="M9 4v14M15 6v14"/>'
I_BELL = '<path d="M6 16V11a6 6 0 1 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>'
I_SHIELD = '<path d="M12 3 5 6v6c0 4.4 3 7.6 7 9 4-1.4 7-4.6 7-9V6z"/><path d="m9 12 2 2 4-4"/>'
I_RAIN = '<path d="M7 15a4.5 4.5 0 1 1 1.6-8.7A6 6 0 0 1 20 9.5 3.5 3.5 0 0 1 18 15z"/><path d="M8 18l-1 2M12 18l-1 2M16 18l-1 2"/>'
I_BACK = '<path d="m15 6-6 6 6 6"/>'
I_CHECK = '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>'
I_WARN = '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17v.01"/>'
PIN = '<svg class="pin" viewBox="0 0 24 32" aria-hidden="true"><path d="M12 0C5.4 0 0 5.2 0 11.6 0 20.3 12 32 12 32s12-11.7 12-20.4C24 5.2 18.6 0 12 0z" fill="currentColor"/><circle cx="12" cy="11.5" r="4.5" fill="#fff"/></svg>'

def home():
    tiles = [('tap', I_REPORT, 'New report', 'Flooded street'), ('', I_MAP, 'Map', 'Reported spots'),
             ('red', I_BELL, 'Alerts', '3 streets'), ('amb', I_SHIELD, 'Safety tips', 'During rain')]
    t = ''.join(f'<div class="tile {c}"><span class="bub">{svg(i)}</span><span class="t2">{a}</span><span class="t3">{b}</span></div>' for c, i, a, b in tiles)
    return f'''<div class="iph lg"><div class="scr" lang="en">{SB}
  <div class="pad"><div class="t1">Hi, Lujain</div><div class="t3">Jeddah · rainy season</div></div>
  <div class="wx">{svg(I_RAIN,' style="width:12cqw;height:12cqw"')}<div><b>24°</b><div class="t3">Heavy rain until 9 PM</div></div></div>
  <div class="tiles">{t}</div>
  <div class="nav"><span class="on"></span><span></span><span></span><span></span></div>
</div></div>'''

def report():
    return f'''<div class="iph"><div class="scr" lang="en">{SB}
  <div class="pad row">{svg(I_BACK)}<span class="t1">New report</span></div>
  <div class="seg"><span class="on">Flooding</span><span>Unusual activity</span></div>
  <div class="lbl2">Street name</div>
  <div class="inp"><span class="typed">Palestine St</span><span class="caret"></span></div>
  <div class="lbl2">Or drop a pin on the map</div>
  <div class="mapbox"><span class="wat"></span>{PIN}</div>
  <div class="btn">Send report</div>
  <div class="toast">{svg(I_CHECK)}Report sent</div>
</div></div>'''

def alerts():
    items = [('Palestine St', 'r', 'Danger', '42', '84%', '#D93A40'), ('King Abdulaziz Rd', 'a', 'Medium', '18', '40%', '#E59A2F'),
             ('Prince Majid Rd', 'a', 'Medium', '15', '32%', '#E59A2F')]
    li = ''.join(f'<div class="it" style="--k:{k}"><div class="row"><span class="t2">{n}</span><span class="sp"></span><span class="chip {c}">{lv}</span></div><span class="t3">Water level: {h} cm</span><div class="lvl"><span style="--w:{w};--c:{col};--k:{k}"></span></div></div>' for k, (n, c, lv, h, w, col) in enumerate(items))
    return f'''<div class="iph"><div class="scr" lang="en">{SB}
  <div class="pad row"><span class="t1">Alerts</span><span class="sp"></span>{svg(I_BELL)}</div>
  <div class="ban">{svg(I_WARN,' style="width:8cqw;height:8cqw"')}<div><div class="t2">Palestine St · danger</div><div class="t3">Avoid this street: the water is high</div></div></div>
  <div class="al">{li}</div>
</div></div>'''

def mapscr():
    return f'''<div class="iph lg"><div class="scr" lang="en">{SB}
  <div class="pad row"><span class="t1">Map</span></div>
  <div class="mapfull">
    <svg viewBox="0 0 200 330" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
      <g stroke="#fff" stroke-linecap="round"><path d="M-10 80H210M-10 170H210M-10 260H210" stroke-width="11"/><path d="M50 -10V340M140 -10V340" stroke-width="11"/><path d="M95 -10V340" stroke-width="6"/></g>
      <g fill="#7A8F99" font-size="7" font-family="sans-serif"><text x="150" y="76">Palestine St</text><text x="146" y="166">Prince Majid Rd</text><text x="56" y="20" transform="rotate(90 56 20)">King Abdulaziz Rd</text></g>
      <circle class="zone" cx="95" cy="170" r="34" fill="#D93A40" fill-opacity=".22" stroke="#D93A40" stroke-width="1.5"/>
      <text x="95" y="174" text-anchor="middle" fill="#D93A40" font-size="10" font-weight="700" font-family="sans-serif">42 cm</text>
      <path class="route" pathLength="1" d="M95 320V260H140V80H95V20" fill="none" stroke="#1E8A5A" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
      <circle r="6" fill="#13879B" stroke="#fff" stroke-width="2.5"><animateMotion dur="7s" repeatCount="indefinite" keyPoints="0;0;1;1" keyTimes="0;0.18;0.55;1" calcMode="linear" path="M95 320V260H140V80H95V20"/></circle>
    </svg>
    <div class="topcard"><span class="dot"></span>Safer route found</div>
    <div class="sheet"><div class="row"><span class="t2">Palestine St closed</span><span class="sp"></span><span class="chip r">Danger</span></div><span class="t3">Water 42 cm · detour adds 4 min</span></div>
  </div>
</div></div>'''

def camera():
    return '''<div class="pn cam" lang="en">
  <svg viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <defs><linearGradient id="tqsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14262F"/><stop offset="1" stop-color="#0A151B"/></linearGradient>
      <linearGradient id="tqwat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2F6E7C" stop-opacity=".9"/><stop offset="1" stop-color="#0E3440"/></linearGradient></defs>
    <rect width="800" height="500" fill="url(#tqsky)"/>
    <g fill="#1B2E37"><rect x="0" y="120" width="120" height="170"/><rect x="130" y="80" width="90" height="210"/><rect x="600" y="100" width="110" height="190"/><rect x="715" y="150" width="85" height="140"/></g>
    <g fill="#E8C76A" opacity=".55"><rect x="20" y="150" width="10" height="14"/><rect x="60" y="190" width="10" height="14"/><rect x="150" y="110" width="10" height="14"/><rect x="180" y="170" width="10" height="14"/><rect x="630" y="130" width="10" height="14"/><rect x="670" y="200" width="10" height="14"/></g>
    <rect x="0" y="280" width="800" height="220" fill="#16252C"/>
    <!-- flooded car, tilted and half under water -->
    <g transform="rotate(-5 300 330)"><path d="M190 340l28-46h132l40 46z" fill="#C9D3D8"/><path d="M226 300h56v34h-80zM292 300h52l30 34h-82z" fill="#5B7A88"/><rect x="180" y="336" width="232" height="44" rx="10" fill="#E4EBEE"/><circle cx="378" cy="352" r="6" fill="#F2D27A"/></g>
    <!-- person waist-deep -->
    <g fill="#D7C2A8"><circle cx="560" cy="290" r="13"/><path d="M546 306h28l6 52h-40z" fill="#B5473A"/><path d="M546 312l-16 26M574 312l18 22" stroke="#D7C2A8" stroke-width="7" stroke-linecap="round"/></g>
    <!-- water surface -->
    <g class="waves"><path d="M0 352q25-10 50 0t50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0 50 0V500H0z" fill="url(#tqwat)"/></g>
    <!-- detection boxes -->
    <g fill="none" stroke-width="3"><rect class="bx" pathLength="1" x="172" y="276" width="252" height="120" stroke="#F59E4B"/><rect class="bx" pathLength="1" x="528" y="264" width="72" height="110" stroke="#4FD1C5" style="--dl:.5s"/></g>
    <g font-family="Helvetica,Arial,sans-serif" font-size="15" font-weight="700"><g class="bl"><rect x="172" y="252" width="150" height="24" fill="#F59E4B"/><text x="180" y="269" fill="#111">flooded car 0.91</text></g>
      <g class="bl" style="--dl:.5s"><rect x="528" y="240" width="160" height="24" fill="#4FD1C5"/><text x="536" y="257" fill="#111">human in flood 0.87</text></g></g>
  </svg>
  <div class="scan"></div>
  <div class="hud"><span class="rec"></span>LIVE · YOLOv10 · CAM-02</div>
  <div class="dets"><span class="det" style="--c:#F59E4B"><i></i>Flooded car detected · Palestine St</span><span class="det" style="--c:#4FD1C5;--dl:.5s"><i></i>Human in flood detected · Palestine St</span></div>
</div>'''

def console():
    rows = [('Palestine St', '7', '42 cm', 'h', 'High', '10:24 PM', ''), ('King Abdulaziz Rd', '3', '18 cm', 'm', 'Medium', '10:11 PM', ''),
            ('Prince Majid Rd', '2', '15 cm', 'm', 'Medium', '9:58 PM', ' gone')]
    r = ''.join(f'<div class="tr{g}"><b>{a}</b><span>{b}</span><span>{c}</span><span class="st {s}">{t}</span><span>{tm}</span><span class="del">Delete</span></div>' for a, b, c, s, t, tm, g in rows)
    return f'''<div class="pn web" lang="en">
  <div class="wb"><i></i><i></i><i></i><span>tawaqaa · authority console</span></div>
  <div class="wbody">
    <div class="side"><b><svg viewBox="0 0 24 24" width="1.1em" height="1.1em" fill="#2BB7CC" aria-hidden="true"><path d="M12 2s7 7.5 7 12.3A7 7 0 0 1 5 14.3C5 9.5 12 2 12 2z"/></svg>Tawaqaa</b><span class="on">Alerts &amp; reports</span><span>Analytics</span><span>Detections</span></div>
    <div class="main">
      <p class="h4">Flood reports</p><div class="sub">Ranked by repetition · live from Firebase</div>
      <div class="kpis"><div class="kpi">Open reports<b><span>12</span><span>10</span></b></div><div class="kpi red">Dangerous streets<b><span>1</span><span>1</span></b></div><div class="kpi">Medium streets<b><span>2</span><span>1</span></b></div><div class="kpi">AI detections<b><span>2</span><span>2</span></b></div></div>
      <div class="tbl"><div class="tr h"><span>Street</span><span>Reports</span><span>Water</span><span>Status</span><span>Last report</span><span>Action</span></div>{r}</div>
    </div>
  </div>
  <div class="wtoast"><i></i>Deleted successfully · Prince Majid Rd</div>
</div>'''

def sensor():
    return '''<div class="sensor" lang="en"><span class="t3">Hotspot · Palestine St</span><p class="h5">Water level</p>
  <div class="gauge"><div class="tube"><span></span></div><div class="read"><b></b><span class="t3">cm of water</span></div></div>
  <div class="ok"><span class="dot"></span>Water sensor · live</div></div>'''

def laptop(inner):
    return f'<div class="lp"><div class="lid"><div class="bez"><span class="camn"></span><div class="disp">{inner}</div></div></div><div class="base"></div></div>'

CARD = f'<div class="tq" aria-hidden="true">{report()}{home()}{alerts()}</div>'

SHOTS_RAW = [
 ('01 · Report', 'Citizens report a flooded street by name or by dropping a pin, and get a confirmation.', f'<div class="tq">{home()}{report()}</div>'),
 ('02 · Alerts', 'Streets are ranked by repeated reports and measured water height, and drivers see the danger level.', f'<div class="tq">{alerts()}{sensor()}</div>'),
 ('03 · Reroute', 'The map marks the flooded street and draws a safer route around it.', f'<div class="tq">{mapscr()}</div>'),
 ('04 · Detect', 'YOLOv10 spots flooded cars and people in the water on live camera frames.', f'<div class="tq">{laptop(camera())}</div>'),
 ('05 · Respond', 'Authorities review ranked reports live and delete the ones that are resolved.', f'<div class="tq">{laptop(console())}</div>'),
]

SHOTS = [(l, h, c) for l, c, h in SHOTS_RAW]
