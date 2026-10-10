#!/usr/bin/env python3
"""United Electrical Surplus — static site generator.
Run:  python3 _generator/build.py   (from the repo root or anywhere)
Writes the HTML pages into the repo root. No dependencies.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- business facts
BIZ = {
    "name": "United Electrical Surplus",
    "phone_disp": "404-831-3600",
    "phone_tel": "4048313600",
    "email": "info@unitedelectricalsurplus.com",
    "email2": "unitedelectricalsurplus@yahoo.com",
    "addr1": "621 Hurricane Shoals Rd NW, Lawrenceville, GA 30046",
    "addr2": "1901 Peachtree Industrial Blvd, Buford, GA 30518",
    "hours": "Open 7 days a week — even Sundays",
    "domain": "https://unitedelectricalsurplus.com",
    "google_page": "https://maps.google.com/?cid=3954105873428335092",
    # Facebook link from Corban 10/10 — a group post of Vinnie's; swap for a
    # business Page URL if he ever makes one.
    "facebook": "https://www.facebook.com/groups/417309805544906/posts/1745200596089147/",
}

MAP1 = ("https://maps.google.com/maps?q=United%20Electrical%20Surplus%2C%20621%20Hurricane"
        "%20Shoals%20Rd%20NW%2C%20Lawrenceville%2C%20GA%2030046&output=embed")
MAP2 = ("https://maps.google.com/maps?q=1901%20Peachtree%20Industrial%20Blvd%2C%20Buford"
        "%2C%20GA%2030518&output=embed")

# ---------------------------------------------------------------- Atlanta skyline
# Stylized silhouette — spire ≈ Bank of America Plaza, cylinder ≈ the Westin,
# stepped crowns ≈ 191 Peachtree / King & Queen. Gold glow behind, pine in front.
SKYLINE = """
<div class="skyline" aria-hidden="true"><svg viewBox="0 0 1440 240" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg">
  <polygon fill="rgba(232,176,33,0.20)" points="0,240 0,150 55,150 55,120 120,120 120,165 165,165 165,95 185,95 185,80 230,80 230,95 250,95 250,170 305,170 305,115 355,115 355,140 420,140 420,70 432,70 432,52 448,52 448,70 460,70 460,140 520,140 520,160 585,160 585,46 597,46 597,10 603,10 603,46 615,46 615,160 680,160 680,120 745,120 745,145 800,145 800,90 818,78 836,90 836,145 905,145 905,170 970,170 970,105 988,92 1006,105 1006,170 1070,170 1070,135 1130,135 1130,155 1195,155 1195,110 1250,110 1250,175 1310,175 1310,140 1380,140 1380,165 1440,165 1440,240"/>
  <polygon fill="rgba(8,30,22,0.88)" points="0,240 0,175 70,175 70,145 135,145 135,185 190,185 190,118 212,118 212,100 258,100 258,118 278,118 278,190 335,190 335,138 390,138 390,162 455,162 455,92 468,92 468,72 484,72 484,92 497,92 497,162 558,162 558,180 625,180 625,66 637,66 637,28 643,28 643,66 655,66 655,180 722,180 722,142 788,142 788,166 845,166 845,112 863,98 881,112 881,166 950,166 950,190 1015,190 1015,126 1033,112 1051,126 1051,190 1115,190 1115,156 1175,156 1175,176 1240,176 1240,132 1295,132 1295,196 1355,196 1355,162 1440,162 1440,240"/>
</svg></div>"""

# ---------------------------------------------------------------- svg icons
I = {
    "phone": '<svg viewBox="0 0 16 16"><path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.6 17.6 0 0 0 4.168 6.608 17.6 17.6 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.68.68 0 0 0-.58-.122l-2.19.547a1.75 1.75 0 0 1-1.657-.459L5.482 8.062a1.75 1.75 0 0 1-.46-1.657l.548-2.19a.68.68 0 0 0-.122-.58z"/></svg>',
    "pin": '<svg viewBox="0 0 16 16"><path d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10m0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6"/></svg>',
    "mail": '<svg viewBox="0 0 16 16"><path d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414zM0 4.697v7.104l5.803-3.558zM6.761 8.83l-6.57 4.026A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586zm3.436-.586L16 11.801V4.697z"/></svg>',
    "clock": '<svg viewBox="0 0 16 16"><path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71z"/><path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16m7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0"/></svg>',
    "check": '<svg viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5"/></svg>',
    "arrow": '<svg viewBox="0 0 16 16"><path d="M1 8a.5.5 0 0 1 .5-.5h11.793L8.146 2.354a.5.5 0 1 1 .708-.708l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8"/></svg>',
    "star": '<svg viewBox="0 0 16 16"><path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187z"/></svg>',
    "truck": '<svg viewBox="0 0 16 16"><path d="M0 3.5A1.5 1.5 0 0 1 1.5 2h9A1.5 1.5 0 0 1 12 3.5V5h1.02a1.5 1.5 0 0 1 1.17.563l1.481 1.85a1.5 1.5 0 0 1 .329.938V10.5a1.5 1.5 0 0 1-1.5 1.5H14a2 2 0 1 1-4 0H6a2 2 0 1 1-3.998-.085A1.5 1.5 0 0 1 0 10.5zm1.294 7.456A2 2 0 0 1 4.732 11h5.536a2 2 0 0 1 .732-.732V3.5a.5.5 0 0 0-.5-.5h-9a.5.5 0 0 0-.5.5v7a.5.5 0 0 0 .294.456M12 10a2 2 0 0 1 1.732 1h.768a.5.5 0 0 0 .5-.5V8.35a.5.5 0 0 0-.11-.312l-1.48-1.85A.5.5 0 0 0 13.02 6H12zm-9 1a1 1 0 1 0 0 2 1 1 0 0 0 0-2m9 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2"/></svg>',
    "cash": '<svg viewBox="0 0 16 16"><path d="M12.136.326A1.5 1.5 0 0 1 14 1.78V3h.5A1.5 1.5 0 0 1 16 4.5v9a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 13.5v-9a1.5 1.5 0 0 1 1.432-1.499zM5.562 3H13V1.78a.5.5 0 0 0-.621-.484zM1.5 4a.5.5 0 0 0-.5.5v9a.5.5 0 0 0 .5.5h13a.5.5 0 0 0 .5-.5v-9a.5.5 0 0 0-.5-.5z"/><path d="M8 11.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5"/></svg>',
    "bolt": '<svg viewBox="0 0 16 16"><path d="M11.251.068a.5.5 0 0 1 .227.58L9.677 6.5H13a.5.5 0 0 1 .364.843l-8 8.5a.5.5 0 0 1-.842-.49L6.323 9.5H3a.5.5 0 0 1-.364-.843l8-8.5a.5.5 0 0 1 .615-.09z"/></svg>',
    "shield": '<svg viewBox="0 0 16 16"><path d="M5.338 1.59a61 61 0 0 0-2.837.856.48.48 0 0 0-.328.39c-.554 4.157.726 7.19 2.253 9.188a10.7 10.7 0 0 0 2.287 2.233c.346.244.652.42.893.533q.18.085.293.118a1 1 0 0 0 .101.025 1 1 0 0 0 .1-.025q.114-.034.294-.118c.24-.113.547-.29.893-.533a10.7 10.7 0 0 0 2.287-2.233c1.527-1.997 2.807-5.031 2.253-9.188a.48.48 0 0 0-.328-.39c-.651-.213-1.75-.56-2.837-.855C9.552 1.29 8.531 1.067 8 1.067c-.53 0-1.552.223-2.662.524zM5.072.56C6.157.265 7.31 0 8 0s1.843.265 2.928.56c1.11.3 2.229.655 2.887.87a1.54 1.54 0 0 1 1.044 1.262c.596 4.477-.787 7.795-2.465 9.99a11.8 11.8 0 0 1-2.517 2.453 7 7 0 0 1-1.048.625c-.28.132-.581.24-.829.24s-.548-.108-.829-.24a7 7 0 0 1-1.048-.625 11.8 11.8 0 0 1-2.517-2.453C1.928 10.487.545 7.169 1.141 2.692A1.54 1.54 0 0 1 2.185 1.43 63 63 0 0 1 5.072.56"/><path d="M10.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0"/></svg>',
    "weight": '<svg viewBox="0 0 16 16"><path d="M8 1a2 2 0 0 1 2 2c0 .73-.39 1.37-.975 1.72A.5.5 0 0 0 9 5.5h2.72a1.5 1.5 0 0 1 1.47 1.206l1.6 8A1.5 1.5 0 0 1 13.32 16H2.68a1.5 1.5 0 0 1-1.47-1.794l1.6-8A1.5 1.5 0 0 1 4.28 5.5H7a.5.5 0 0 0-.025-.78A2 2 0 0 1 8 1m0 1a1 1 0 0 0-1 1c0 .55.45 1 1 1s1-.45 1-1a1 1 0 0 0-1-1M4.28 6.5a.5.5 0 0 0-.49.402l-1.6 8a.5.5 0 0 0 .49.598h10.64a.5.5 0 0 0 .49-.598l-1.6-8a.5.5 0 0 0-.49-.402z"/></svg>',
    "box": '<svg viewBox="0 0 16 16"><path d="M8.186 1.113a.5.5 0 0 0-.372 0L1.846 3.5 8 5.961 14.154 3.5zM15 4.239l-6.5 2.6v7.922l6.5-2.6V4.24zM7.5 14.762V6.838L1 4.239v7.923zM7.443.184a1.5 1.5 0 0 1 1.114 0l7.129 2.852A.5.5 0 0 1 16 3.5v8.662a1 1 0 0 1-.629.928l-7.185 2.874a.5.5 0 0 1-.372 0L.63 13.09a1 1 0 0 1-.63-.928V3.5a.5.5 0 0 1 .314-.464z"/></svg>',
    "fb": '<svg viewBox="0 0 16 16"><path d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951"/></svg>',
    "google": '<svg viewBox="0 0 16 16"><path d="M15.545 6.558a9.4 9.4 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.7 7.7 0 0 1 5.352 2.082l-2.284 2.284A4.35 4.35 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.8 4.8 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.7 3.7 0 0 0 1.599-2.431H8v-3.08z"/></svg>',
    "sms": '<svg viewBox="0 0 16 16"><path d="M5 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2zM4 4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1zm4 9.5a.75.75 0 1 1 0-1.5.75.75 0 0 1 0 1.5"/></svg>',
}

CHECK24 = '<svg viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5"/></svg>'

NAV = [
    ("index.html", "Home"),
    ("sell.html", "Sell Your Surplus"),
    ("buy.html", "Buy Equipment"),
    ("pickup.html", "Pickup & Logistics"),
    ("locations.html", "Locations"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]


def head(title, desc, canonical):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BIZ['domain']}/{canonical}">
<link rel="icon" type="image/png" href="assets/img/logo.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="{BIZ['domain']}/assets/img/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css?v=3">
</head>
<body>
"""


def chrome_top(active):
    links = ""
    for href, label in NAV[1:]:
        cls = ' class="active"' if href == active else ""
        links += f'    <a href="{href}"{cls}>{label}</a>\n'
    return f"""
<!-- DEMO — delete this div, the .footer-demo block, section 5 of main.js and
     the .demo-bar/.demo-modal CSS when the site goes live. -->
<div class="demo-bar"><span class="demo-dot"></span><strong>DEMO PREVIEW</strong><span
  class="demo-tail"> &mdash; a design concept for United Electrical Surplus by
  <a href="https://60minutesites.com" target="_blank" rel="noopener">60&nbsp;Minute&nbsp;Sites</a>
  &middot; photos from the current site &middot; forms deliver to 60MS, not to the shop</span>
  <button type="button" data-demo-open>What&rsquo;s this?</button></div>

<div class="util-bar"><div class="wrap">
  <a href="tel:{BIZ['phone_tel']}">{I['phone']} {BIZ['phone_disp']}</a>
  <span class="util-hide">{I['clock']} {BIZ['hours']}</span>
  <span class="util-hide">{I['pin']} Lawrenceville &amp; Buford, Georgia</span>
  <span class="util-spacer"></span>
  <a class="util-hide" href="mailto:{BIZ['email']}">{I['mail']} {BIZ['email']}</a>
</div></div>

<header class="site-header"><div class="wrap nav-row">
  <a class="brand" href="index.html" aria-label="United Electrical Surplus &mdash; home">
    <img src="assets/img/logo.png" alt="United Electrical Surplus" width="791" height="754">
  </a>
  <button class="nav-burger" aria-label="Menu" aria-expanded="false"><svg viewBox="0 0 16 16"><path d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/></svg></button>
  <nav class="main-nav">
{links}    <a class="btn-gold nav-cta" href="sell.html">Get a Cash Offer</a>
  </nav>
</div></header>
"""


def chrome_footer():
    nav_links = "".join(
        f'      <li><a href="{href}">{label}</a></li>\n' for href, label in NAV
    )
    return f"""
<footer class="site-footer">
  <div class="wrap footer-main">
    <div class="footer-brand">
      <img src="assets/img/logo-white.png" alt="United Electrical Surplus" width="454" height="405">
      <p>We buy and sell surplus electrical equipment &mdash; and we pay more for it than
      anyone in the business. Based in Gwinnett County, Georgia. Buying nationwide.</p>
      <div class="footer-social">
        <a href="{BIZ['facebook']}" target="_blank" rel="noopener" aria-label="Facebook">{I['fb']}</a>
        <a href="{BIZ['google_page']}" target="_blank" rel="noopener" aria-label="Google Business Profile">{I['google']}</a>
      </div>
    </div>
    <div class="footer-nav">
      <h4>Explore</h4>
      <ul>
{nav_links}      </ul>
    </div>
    <div class="footer-nav">
      <h4>Top brands we buy</h4>
      <ul>
        <li>Square&nbsp;D</li>
        <li>Siemens</li>
        <li>Eaton / Cutler-Hammer</li>
        <li>ABB</li>
        <li>General Electric</li>
        <li>Westinghouse</li>
      </ul>
    </div>
    <div class="footer-contact">
      <h4>Talk to us</h4>
      <ul>
        <li>{I['phone']} <a href="tel:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a></li>
        <li>{I['mail']} <a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
        <li>{I['pin']} <span>{BIZ['addr1']}</span></li>
        <li>{I['pin']} <span>{BIZ['addr2']}</span></li>
        <li>{I['clock']} <span>{BIZ['hours']}</span></li>
      </ul>
    </div>
  </div>

  <!-- DEMO — delete this block when the site goes live. -->
  <div class="wrap footer-demo"><b>This is a demo site.</b> It was built as a free design
  concept by <a href="https://60minutesites.com" target="_blank" rel="noopener">60 Minute Sites</a>
  to show what unitedelectricalsurplus.com could look like. Photos come from the current site;
  copy, layout and every detail can be changed before launch.</div>

  <div class="wrap footer-base">
    <span>&copy; 2026 United Electrical Surplus. All rights reserved.</span>
    <span>Demo site by <a href="https://60minutesites.com" target="_blank" rel="noopener">60 Minute Sites</a></span>
  </div>
</footer>

<script src="assets/js/main.js?v=3"></script>
</body>
</html>
"""


def page_hero(crumb, title, sub):
    return f"""
<div class="page-hero">
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; {crumb}</div>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</div>
"""


def cta_band(h, p, primary=("sell.html", "Get a Cash Offer"), secondary=None):
    sec = ""
    if secondary:
        sec = f'      <a class="btn btn-ghost" href="{secondary[0]}">{secondary[1]}</a>\n'
    return f"""
<section class="cta-band">
  <div class="wrap" data-reveal>
    <h2>{h}</h2>
    <p>{p}</p>
    <div class="hero-ctas">
      <a class="btn btn-gold" href="{primary[0]}">{I['cash']} {primary[1]}</a>
      <a class="btn btn-ghost" href="tel:{BIZ['phone_tel']}">{I['phone']} Call {BIZ['phone_disp']}</a>
{sec}    </div>
  </div>
</section>
"""


# ================================================================ INDEX
schema = f"""
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "United Electrical Surplus",
  "description": "Buyer and seller of surplus electrical equipment: circuit breakers, panelboards, switchgear, transformers, bus duct, motor controls and more. Cash paid on the spot; pickup available nationwide.",
  "url": "{BIZ['domain']}",
  "telephone": "+1-404-831-3600",
  "email": "{BIZ['email']}",
  "image": "{BIZ['domain']}/assets/img/logo.jpg",
  "priceRange": "$$",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "621 Hurricane Shoals Rd NW",
    "addressLocality": "Lawrenceville",
    "addressRegion": "GA",
    "postalCode": "30046",
    "addressCountry": "US"
  }},
  "openingHours": "Mo-Su 00:00-23:59",
  "areaServed": ["Georgia", "Tennessee", "Alabama", "Florida", "Texas", "Oklahoma", "Louisiana", "North Carolina"],
  "sameAs": ["{BIZ['google_page']}"]
}}
</script>"""

index_body = f"""
<div class="hero">
  <div class="hero-media"><img src="assets/img/photos/hero-warehouse.jpg" alt="Aisles of surplus electrical equipment in the United Electrical Surplus warehouse" fetchpriority="high"></div>
  <div class="wrap"><div class="hero-split">
    <div class="hero-inner" data-reveal>
      <div class="kicker on-dark" style="color:var(--gold)">Lawrenceville, Georgia &middot; Buying Nationwide</div>
      <h1>We pay more for surplus electrical. <em>Cash, on the spot.</em></h1>
      <p class="hero-sub">Square&nbsp;D, Siemens, Eaton, ABB, GE &mdash; breakers, panels, switchgear,
      transformers and everything in between. If it&rsquo;s sitting in your warehouse, on your job site
      or coming out of a demo, we&rsquo;ll beat any other offer on it.</p>
      <div class="hero-ctas">
        <a class="btn btn-gold" href="sell.html">{I['cash']} Get a Cash Offer</a>
        <a class="btn btn-ghost" href="buy.html">Browse What We Sell</a>
      </div>
      <div class="hero-chips">
        <span>{I['star']} 5.0 rating on Google</span>
        <span>{I['truck']} We come to you</span>
        <span>{I['bolt']} Same-day offers</span>
      </div>
    </div>
    <aside class="hero-card" data-reveal>
      <h3>Selling takes three steps</h3>
      <p>No appointments, no haggling marathons. Most offers go out the same day.</p>
      <ol class="hero-steps">
        <li><span class="step-n">1</span><span><b>Text us pictures.</b> Snap the nameplates and the pile &mdash; that&rsquo;s all we need.</span></li>
        <li><span class="step-n">2</span><span><b>Get our number.</b> A real offer, not a lowball &mdash; we pay more than anyone.</span></li>
        <li><span class="step-n">3</span><span><b>Get paid.</b> Cash on the spot. We load and haul it ourselves.</span></li>
      </ol>
      <a class="btn btn-gold" href="sms:{BIZ['phone_tel']}">{I['sms']} Text photos to {BIZ['phone_disp']}</a>
    </aside>
  </div></div>
</div>

<div class="trust-bar"><div class="wrap">
  <div class="trust-item">{I['cash']}<span><b>Top dollar, guaranteed</b><small>Bring any written offer &mdash; we&rsquo;ll beat it</small></span></div>
  <div class="trust-item">{I['truck']}<span><b>Tractors &amp; trailers</b><small>We pick up on site, any size load</small></span></div>
  <div class="trust-item">{I['weight']}<span><b>40,000&nbsp;lb+ lifts</b><small>Crane capability for the heavy stuff</small></span></div>
  <div class="trust-item">{I['box']}<span><b>Nationwide shipping</b><small>Surplus sales shipped coast to coast</small></span></div>
</div></div>

<div class="brand-strip"><div class="wrap">
  <span class="label">We buy &amp; stock</span>
  <span class="brand-mark first">SQUARE&nbsp;D</span>
  <span class="brand-mark">SIEMENS</span>
  <span class="brand-mark">EATON</span>
  <span class="brand-mark">ABB</span>
  <span class="brand-mark">GE</span>
  <span class="brand-mark">WESTINGHOUSE</span>
</div></div>

<section>
  <div class="wrap">
    <div class="section-head" data-reveal>
      <div class="kicker">What we buy</div>
      <h2>If it moves power, we want it.</h2>
      <p class="lead">New in the box, pulled from service, or straight off a demolition &mdash; condition
      matters less than you think. Here&rsquo;s where the money is.</p>
    </div>
    <div class="card-grid">
      <a data-reveal class="card" href="sell.html"><div class="card-img"><img src="assets/img/photos/breakers-yellow.jpg" alt="Molded case circuit breakers" loading="lazy"></div><div class="card-body"><h3>Circuit Breakers</h3><p>Molded case, miniature and industrial frame &mdash; Square&nbsp;D PowerPact breakers are our bread and butter.</p><span class="card-link">See what it&rsquo;s worth {I['arrow']}</span></div></a>
      <a data-reveal class="card" href="sell.html"><div class="card-img"><img src="assets/img/photos/panels-lineup.jpg" alt="Distribution panels and switchboards" loading="lazy"></div><div class="card-body"><h3>Panels &amp; Switchgear</h3><p>Panelboards, distribution panels, switchboards and full MCC lineups with buckets.</p><span class="card-link">See what it&rsquo;s worth {I['arrow']}</span></div></a>
      <a data-reveal class="card" href="sell.html"><div class="card-img"><img src="assets/img/photos/transformer-padmount.jpg" alt="Padmount transformer" loading="lazy"></div><div class="card-body"><h3>Transformers</h3><p>Dry-type and padmount units of all sizes &mdash; the heavier it is, the more we like it.</p><span class="card-link">See what it&rsquo;s worth {I['arrow']}</span></div></a>
      <a data-reveal class="card" href="sell.html"><div class="card-img"><img src="assets/img/photos/contactors.jpg" alt="Bus plugs and contactors" loading="lazy"></div><div class="card-body"><h3>Bus Duct &amp; Bus Plugs</h3><p>Busway runs, plugs and fittings &mdash; working pulls or whole systems out of a plant.</p><span class="card-link">See what it&rsquo;s worth {I['arrow']}</span></div></a>
      <a data-reveal class="card" href="sell.html"><div class="card-img"><img src="assets/img/photos/component-trays.jpg" alt="Motor starters and controls" loading="lazy"></div><div class="card-body"><h3>Starters, Contactors &amp; VFDs</h3><p>Motor controls, drives, lighting and ballasts &mdash; by the piece or by the pallet.</p><span class="card-link">See what it&rsquo;s worth {I['arrow']}</span></div></a>
      <a data-reveal class="card" href="sell.html"><div class="card-img"><img src="assets/img/photos/wire-spools.jpg" alt="Spools of electrical wire" loading="lazy"></div><div class="card-body"><h3>Wire, Conduit &amp; More</h3><p>Wire and cable, conduit, troughing, meter sockets and single-phase motors under 20&nbsp;HP.</p><span class="card-link">See what it&rsquo;s worth {I['arrow']}</span></div></a>
    </div>
  </div>
</section>

<section class="tight" style="background:var(--white)">
  <div class="wrap split">
    <div class="split-img" data-reveal>
      <img src="assets/img/photos/truck-load.jpg" alt="United Electrical Surplus trailer loaded with electrical equipment" loading="lazy">
      <span class="split-badge">We load. We haul. You get paid.</span>
    </div>
    <div data-reveal>
      <div class="kicker">Don&rsquo;t scrap it &mdash; sell it</div>
      <h2>Scrap value is the floor, not the price.</h2>
      <p class="lead">A recycler weighs your gear. We read the nameplate. Surplus electrical equipment
      is worth multiples of its metal, and we&rsquo;re the buyer who actually pays that difference.</p>
      <ul class="checks">
        <li>{CHECK24}<span><b>Cash on the spot</b> &mdash; no net-30, no &ldquo;check&rsquo;s in the mail.&rdquo;</span></li>
        <li>{CHECK24}<span><b>Our trucks, our crew</b> &mdash; tractors and trailers for full plant pulls.</span></li>
        <li>{CHECK24}<span><b>Heavy is fine</b> &mdash; crane lifts to 40,000&nbsp;lbs and beyond.</span></li>
        <li>{CHECK24}<span><b>One call clears the warehouse</b> &mdash; we take the whole lot, not the cherries.</span></li>
      </ul>
      <a class="btn btn-pine" href="pickup.html">How pickup works {I['arrow']}</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split flip">
    <div class="split-img" data-reveal>
      <img src="assets/img/photos/warehouse-racks.jpg" alt="Racks of stocked electrical equipment" loading="lazy">
    </div>
    <div data-reveal>
      <div class="kicker">What we sell</div>
      <h2>Stocked deep. Priced under the distributor.</h2>
      <p class="lead">Contractors and plant managers shop us for the same reason sellers call us:
      the numbers work. Breakers, panels, switchgear, wire and transformers &mdash; tested, guaranteed,
      and shipped nationwide.</p>
      <ul class="checks">
        <li>{CHECK24}<span><b>Hard-to-find and obsolete</b> &mdash; including out-of-production Square&nbsp;D and Westinghouse.</span></li>
        <li>{CHECK24}<span><b>Same-day local pickup</b> in Lawrenceville, next-day freight most places.</span></li>
        <li>{CHECK24}<span><b>Real inventory</b> &mdash; call and we&rsquo;ll put our hands on it while you&rsquo;re on the line.</span></li>
      </ul>
      <a class="btn btn-pine" href="buy.html">Browse equipment {I['arrow']}</a>
    </div>
  </div>
</section>

<div class="google-band"><div class="wrap" data-reveal>
  <div class="g-score">
    <span class="g-num">5.0</span>
    <span><span class="g-stars">{I['star']}{I['star']}{I['star']}{I['star']}{I['star']}</span>
    <span class="g-label">United Electrical Surplus on Google</span></span>
  </div>
  <div class="g-actions">
    <a class="btn btn-pine" href="{BIZ['google_page']}" target="_blank" rel="noopener">{I['google']} Find us on Google</a>
    <a class="btn btn-ghost" href="{BIZ['google_page']}" target="_blank" rel="noopener">Leave a review</a>
  </div>
</div></div>

<section>
  <div class="wrap">
    <div class="section-head center" data-reveal>
      <div class="kicker">The warehouse</div>
      <h2>Come see the inventory for yourself.</h2>
    </div>
    <div class="gallery" data-reveal>
      <a href="assets/img/photos/warehouse-green.jpg" data-lightbox><img src="assets/img/photos/warehouse-green.jpg" alt="Pallets of surplus electrical stock" loading="lazy"></a>
      <a href="assets/img/photos/breakers-dark.jpg" data-lightbox><img src="assets/img/photos/breakers-dark.jpg" alt="Industrial circuit breakers" loading="lazy"></a>
      <a href="assets/img/photos/panels-switchgear.jpg" data-lightbox><img src="assets/img/photos/panels-switchgear.jpg" alt="Panels and switchgear" loading="lazy"></a>
      <a href="assets/img/photos/boxes-racks.jpg" data-lightbox><img src="assets/img/photos/boxes-racks.jpg" alt="Boxed inventory on warehouse racking" loading="lazy"></a>
    </div>
  </div>
</section>

<section class="band-dark skyline-band" style="padding-bottom:clamp(170px,24vw,300px)">
  {SKYLINE}
  <div class="wrap">
    <div class="section-head" data-reveal>
      <div class="kicker">Atlanta, Georgia &middot; Service area</div>
      <h2>Atlanta today. <em>The Southeast and beyond tomorrow.</em></h2>
      <p class="lead">Headquartered just outside Atlanta in Gwinnett County, with buyers on the
      road across the region &mdash; and new locations on the map.</p>
    </div>
    <div class="chip-row" data-reveal>
      <span class="chip now">{I['pin']} Lawrenceville, GA &mdash; HQ</span>
      <span class="chip now">{I['pin']} Buford, GA</span>
      <span class="chip">{I['pin']} Dallas, TX</span>
      <span class="chip">{I['pin']} Houston, TX</span>
      <span class="chip">{I['pin']} Charlotte, NC</span>
      <span class="chip">{I['pin']} Oklahoma City, OK</span>
      <span class="chip">{I['pin']} New Orleans, LA</span>
      <span class="chip">{I['pin']} Baton Rouge, LA</span>
      <span class="chip">{I['bolt']} Tennessee</span>
      <span class="chip">{I['bolt']} Alabama</span>
      <span class="chip">{I['bolt']} Florida</span>
      <span class="chip">{I['bolt']} Texas</span>
    </div>
  </div>
</section>
""" + cta_band(
    "Got a pile of breakers? Let&rsquo;s talk.",
    "Text pictures right now and you&rsquo;ll have a number before you finish your coffee. "
    "We pay more than anyone &mdash; and we can prove it.",
)

# ================================================================ SELL
sell_body = page_hero(
    "Sell Your Surplus",
    "Sell your surplus electrical equipment",
    "We pay more for surplus electrical than anyone in the business — cash on the spot, "
    "and we come get it with our own trucks.",
) + f"""
<section class="tight">
  <div class="wrap">
    <div class="steps">
      <div class="step" data-reveal><h3>Text us pictures</h3><p>Photograph the nameplates, the labels and the pile itself, and text them to
      <a href="sms:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a>. New, used, or pulled from a demo &mdash; send it all.</p></div>
      <div class="step" data-reveal><h3>Get a real offer</h3><p>Most offers go out the same day. Already have a bid from someone else?
      Show it to us &mdash; beating it is the whole business model.</p></div>
      <div class="step" data-reveal><h3>Get paid on the spot</h3><p>Cash when we pick up. Our tractors, trailers and crew handle the loading,
      from one pallet to an entire plant.</p></div>
    </div>
  </div>
</section>

<section style="background:var(--white)">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <div class="kicker">The buy list</div>
      <h2>What we&rsquo;re buying right now</h2>
      <p class="lead">Square&nbsp;D, Siemens, Eaton / Cutler-Hammer, ABB, GE, Westinghouse and every
      other major brand. Quantity helps, but singles of the right item get paid too.</p>
    </div>
    <div class="panel-grid">
      <div class="panel" data-reveal>
        <h3>{I['bolt']} Breakers &amp; Distribution</h3>
        <ul>
          <li>{CHECK24}<span>Molded case circuit breakers (incl. Square&nbsp;D PowerPact)</span></li>
          <li>{CHECK24}<span>Miniature &amp; industrial-frame breakers</span></li>
          <li>{CHECK24}<span>Panelboards &amp; distribution panels</span></li>
          <li>{CHECK24}<span>Switchboards &amp; switchgear</span></li>
          <li>{CHECK24}<span>Meter sockets</span></li>
        </ul>
      </div>
      <div class="panel" data-reveal>
        <h3>{I['box']} Busway &amp; Power</h3>
        <ul>
          <li>{CHECK24}<span>Bus duct &amp; busway runs</span></li>
          <li>{CHECK24}<span>Bus plugs &amp; fittings</span></li>
          <li>{CHECK24}<span>Transformers &mdash; dry-type &amp; padmount</span></li>
          <li>{CHECK24}<span>MCC lineups &amp; buckets</span></li>
        </ul>
      </div>
      <div class="panel" data-reveal>
        <h3>{I['weight']} Controls &amp; Motors</h3>
        <ul>
          <li>{CHECK24}<span>Starters &amp; contactors</span></li>
          <li>{CHECK24}<span>Variable frequency drives (VFDs)</span></li>
          <li>{CHECK24}<span>Single-phase motors under 20&nbsp;HP</span></li>
          <li>{CHECK24}<span>Lighting &amp; ballasts</span></li>
        </ul>
      </div>
      <div class="panel" data-reveal>
        <h3>{I['truck']} Wire &amp; Raceway</h3>
        <ul>
          <li>{CHECK24}<span>Wire &amp; cable, all gauges</span></li>
          <li>{CHECK24}<span>Conduit &amp; fittings</span></li>
          <li>{CHECK24}<span>Wire troughing</span></li>
          <li>{CHECK24}<span>Job-site overstock &amp; returns</span></li>
        </ul>
      </div>
    </div>

    <div style="margin-top:28px" class="no-buy" data-reveal>
      <h3>A few things we pass on</h3>
      <p style="font-size:0.92rem;color:var(--muted)">So nobody wastes a trip &mdash; we currently do <b>not</b> buy:</p>
      <ul>
        <li>Three-phase motors 20&nbsp;HP and up</li>
        <li>UPS systems</li>
        <li>Transfer switches</li>
        <li>PDU units</li>
        <li>Disconnects</li>
        <li>Fused pullouts</li>
      </ul>
    </div>
  </div>
</section>

<section id="offer">
  <div class="wrap split">
    <div data-reveal>
      <div class="kicker">Get your number</div>
      <h2>Tell us what you&rsquo;re sitting on.</h2>
      <p class="lead">The fastest route is still a text to
      <a href="sms:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a> with pictures &mdash; but the form works
      too, and we answer both the same day.</p>
      <ul class="checks">
        <li>{CHECK24}<span>Include brand names and amp ratings if you can see them.</span></li>
        <li>{CHECK24}<span>Rough quantity is fine &mdash; &ldquo;about three pallets&rdquo; tells us plenty.</span></li>
        <li>{CHECK24}<span>Tell us where it is; we&rsquo;ll figure out the trucking.</span></li>
      </ul>
    </div>
    <div class="form-card" data-reveal>
      <form name="cash-offer" method="POST" data-netlify="true" action="thank-you.html">
        <input type="hidden" name="form-name" value="cash-offer">
        <input type="hidden" name="source" value="United Electrical Surplus demo — sell page">
        <div class="form-grid">
          <div><label for="s-name">Name</label><input id="s-name" name="name" type="text" required autocomplete="name"></div>
          <div><label for="s-phone">Phone</label><input id="s-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="full"><label for="s-email">Email (optional)</label><input id="s-email" name="email" type="email" autocomplete="email"></div>
          <div class="full"><label for="s-what">What do you have?</label><textarea id="s-what" name="details" required placeholder="e.g. ~200 Square D molded case breakers, two pallets of bus plugs, one 750 kVA padmount — located in Marietta"></textarea></div>
          <div class="full"><button class="btn btn-gold" type="submit" style="width:100%">{I['cash']} Request my cash offer</button></div>
        </div>
        <p class="form-note"><b>Demo note:</b> while this site is a preview, submissions go to
        60 Minute Sites so the owner can see the leads coming in &mdash; on the live site they go straight to the shop.</p>
      </form>
    </div>
  </div>
</section>
""" + cta_band(
    "Already have someone else&rsquo;s offer?",
    "Perfect. Bring it. Beating the other guy&rsquo;s number is our favorite part of the day.",
)

# ================================================================ BUY
buy_body = page_hero(
    "Buy Equipment",
    "Surplus electrical equipment, priced right",
    "Tested, guaranteed and stocked deep in Lawrenceville — with same-day local pickup "
    "and nationwide shipping.",
) + f"""
<section>
  <div class="wrap">
    <div class="section-head" data-reveal>
      <div class="kicker">Inventory</div>
      <h2>What&rsquo;s on the shelves</h2>
      <p class="lead">Stock turns fast and the obscure stuff is the specialty. If you don&rsquo;t see it,
      call &mdash; it may have come in this morning.</p>
    </div>
    <div class="card-grid">
      <div data-reveal class="card"><div class="card-img"><img src="assets/img/photos/breakers-yellow.jpg" alt="Square D circuit breakers" loading="lazy"></div><div class="card-body"><h3>Circuit Breakers</h3><p>Molded case, miniature and industrial &mdash; deep Square&nbsp;D PowerPact stock, plus Siemens, Eaton, GE and obsolete frames you can&rsquo;t get from a distributor.</p></div></div>
      <div data-reveal class="card"><div class="card-img"><img src="assets/img/photos/panels-lineup.jpg" alt="Panelboards and switchboards" loading="lazy"></div><div class="card-body"><h3>Panels &amp; Switchgear</h3><p>Panelboards, distribution panels, switchboards and gear sections, ready to ship.</p></div></div>
      <div data-reveal class="card"><div class="card-img"><img src="assets/img/photos/transformers-teal.jpg" alt="Dry-type transformers" loading="lazy"></div><div class="card-body"><h3>Transformers</h3><p>Dry-type and padmount units across the kVA range &mdash; freight arranged to your site.</p></div></div>
      <div data-reveal class="card"><div class="card-img"><img src="assets/img/photos/wire-spools.jpg" alt="Wire and cable spools" loading="lazy"></div><div class="card-body"><h3>Wire &amp; Cable</h3><p>Copper and aluminum in the common gauges and colors, by the spool or the skid.</p></div></div>
      <div data-reveal class="card"><div class="card-img"><img src="assets/img/photos/tools.jpg" alt="Electrical tools and accessories" loading="lazy"></div><div class="card-body"><h3>Tools &amp; Accessories</h3><p>Testers, pliers, fuses, fittings and the job-box odds and ends every crew burns through.</p></div></div>
      <div data-reveal class="card"><div class="card-img"><img src="assets/img/photos/component-trays.jpg" alt="Motor controls and starters" loading="lazy"></div><div class="card-body"><h3>Motor Controls</h3><p>Starters, contactors, VFDs and MCC buckets, pulled, tested and tagged.</p></div></div>
    </div>
  </div>
</section>

<section class="tight band-dark">
  <div class="wrap">
    <div class="stat-row" data-reveal>
      <div class="stat"><b>Same day</b><span>Local pickup in Lawrenceville</span></div>
      <div class="stat"><b>50 states</b><span>Nationwide freight &amp; parcel</span></div>
      <div class="stat"><b>6 brands</b><span>Square&nbsp;D, Siemens, Eaton, ABB, GE, Westinghouse</span></div>
      <div class="stat"><b>1 call</b><span>{BIZ['phone_disp']} &mdash; hands on your part while you hold</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="split-img" data-reveal><img src="assets/img/photos/aisle-dark.jpg" alt="Warehouse aisle stocked with electrical surplus" loading="lazy"></div>
    <div data-reveal>
      <div class="kicker">Why buy surplus</div>
      <h2>Distributor quality without the distributor invoice.</h2>
      <ul class="checks">
        <li>{CHECK24}<span><b>Serious savings</b> over list on name-brand gear.</span></li>
        <li>{CHECK24}<span><b>Obsolete &amp; hard-to-find</b> &mdash; keep an old building running without a retrofit.</span></li>
        <li>{CHECK24}<span><b>Everything checked</b> before it leaves the building.</span></li>
        <li>{CHECK24}<span><b>Straight answers</b> &mdash; if we wouldn&rsquo;t install it, we won&rsquo;t sell it.</span></li>
      </ul>
      <a class="btn btn-gold" href="tel:{BIZ['phone_tel']}">{I['phone']} Call for availability &amp; pricing</a>
    </div>
  </div>
</section>
""" + cta_band(
    "Need a breaker nobody else can find?",
    "Give us the catalog number off the old one. The odd stuff is exactly what a surplus house is for.",
    primary=("contact.html", "Ask About a Part"),
)

# ================================================================ PICKUP
pickup_body = page_hero(
    "Pickup &amp; Logistics",
    "Our trucks. Your dock. Zero hassle.",
    "Tractors, trailers and crane capability past 40,000 pounds — we move the equipment "
    "other buyers won’t even quote.",
) + f"""
<section class="tight">
  <div class="wrap split">
    <div class="split-img" data-reveal>
      <img src="assets/img/photos/truck-load.jpg" alt="Loaded flatbed trailer leaving a pickup" loading="lazy">
      <span class="split-badge">Door to dock, handled</span>
    </div>
    <div data-reveal>
      <div class="kicker">Heavy is our specialty</div>
      <h2>If it fits on a trailer, we&rsquo;ll come get it.</h2>
      <p class="lead">Most surplus buyers want you to palletize, shrink-wrap and ship. We bring the
      tractor, the trailer and the muscle instead &mdash; because the easiest seller to win is the one
      everyone else made do the work.</p>
      <ul class="checks">
        <li>{CHECK24}<span><b>Tractors &amp; trailers</b> for full-plant and warehouse pulls.</span></li>
        <li>{CHECK24}<span><b>Crane lifts past 40,000&nbsp;lbs</b> &mdash; switchgear lineups, padmounts, the big iron.</span></li>
        <li>{CHECK24}<span><b>Demolition &amp; decommission friendly</b> &mdash; we work your schedule, not ours.</span></li>
        <li>{CHECK24}<span><b>Insured, careful crews</b> on your site and off it fast.</span></li>
      </ul>
      <a class="btn btn-gold" href="sell.html">{I['cash']} Get an offer with pickup included</a>
    </div>
  </div>
</section>

<section style="background:var(--white)">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <div class="kicker">How it goes</div>
      <h2>Pickup in three moves</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal><h3>Walk us the site</h3><p>Photos or a quick video call. We scope the load, the access and the lift
      before anyone rolls a wheel.</p></div>
      <div class="step" data-reveal><h3>We schedule the iron</h3><p>Truck, trailer, crane if the job needs one &mdash; booked around your
      operating hours, including nights and weekends on demo jobs.</p></div>
      <div class="step" data-reveal><h3>Loaded, paid, gone</h3><p>Our crew loads, you count the cash, and your floor space is back
      the same day.</p></div>
    </div>
  </div>
</section>

<section class="band-dark tight">
  <div class="wrap" data-reveal style="display:flex;align-items:center;gap:26px 44px;flex-wrap:wrap">
    <h2 style="margin:0;flex:1;min-width:280px">Plant managers: clearing a facility?</h2>
    <a class="btn btn-gold" href="contact.html">{I['truck']} Book a site walk-through</a>
  </div>
</section>
""" + cta_band(
    "One text starts the truck.",
    f"Send photos of the load to {BIZ['phone_disp']} and we&rsquo;ll quote the equipment and the haul together.",
)

# ================================================================ LOCATIONS
locations_body = page_hero(
    "Locations",
    "Two Georgia locations. One phone number.",
    "Headquartered in Lawrenceville with a second building in Buford — and new markets "
    "opening across the South.",
) + f"""
<section class="tight">
  <div class="wrap loc-grid">
    <div class="loc-card" data-reveal>
      <div class="map-frame" style="border-radius:0;border:0;box-shadow:none"><iframe src="{MAP1}" title="Map — United Electrical Surplus, Lawrenceville GA" loading="lazy" style="height:300px"></iframe></div>
      <div class="loc-body">
        <span class="loc-tag">Headquarters</span>
        <h3>Lawrenceville, Georgia</h3>
        <address>{BIZ['addr1']}</address>
        <div class="loc-meta">
          <span>{I['clock']} Open 7 days a week &mdash; yes, Sundays too</span>
          <span>{I['phone']} <a href="tel:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a></span>
        </div>
        <a class="btn btn-pine" href="https://maps.google.com/maps?q=United+Electrical+Surplus,+621+Hurricane+Shoals+Rd+NW,+Lawrenceville,+GA+30046" target="_blank" rel="noopener">{I['pin']} Get directions</a>
      </div>
    </div>
    <div class="loc-card" data-reveal>
      <div class="map-frame" style="border-radius:0;border:0;box-shadow:none"><iframe src="{MAP2}" title="Map — United Electrical Surplus, Buford GA" loading="lazy" style="height:300px"></iframe></div>
      <div class="loc-body">
        <span class="loc-tag">Buford location</span>
        <h3>Buford, Georgia</h3>
        <address>{BIZ['addr2']}</address>
        <div class="loc-meta">
          <span>{I['clock']} By appointment &mdash; call ahead</span>
          <span>{I['phone']} <a href="tel:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a></span>
        </div>
        <a class="btn btn-pine" href="https://maps.google.com/maps?q=1901+Peachtree+Industrial+Blvd,+Buford,+GA+30518" target="_blank" rel="noopener">{I['pin']} Get directions</a>
      </div>
    </div>
  </div>
</section>

<section class="band-dark skyline-band" style="padding-bottom:clamp(170px,24vw,300px)">
  {SKYLINE}
  <div class="wrap">
    <div class="section-head" data-reveal>
      <div class="kicker">Growing fast</div>
      <h2>New markets on the board</h2>
      <p class="lead">The buying operation already travels. These are the cities and states where
      United Electrical Surplus is planting flags next.</p>
    </div>
    <div class="chip-row" data-reveal>
      <span class="chip">{I['pin']} Dallas, TX</span>
      <span class="chip">{I['pin']} Houston, TX</span>
      <span class="chip">{I['pin']} Charlotte, NC</span>
      <span class="chip">{I['pin']} Oklahoma City, OK</span>
      <span class="chip">{I['pin']} New Orleans, LA</span>
      <span class="chip">{I['pin']} Baton Rouge, LA</span>
      <span class="chip">{I['bolt']} Georgia</span>
      <span class="chip">{I['bolt']} Tennessee</span>
      <span class="chip">{I['bolt']} Alabama</span>
      <span class="chip">{I['bolt']} Florida</span>
      <span class="chip">{I['bolt']} Texas</span>
      <span class="chip">{I['bolt']} Oklahoma</span>
      <span class="chip">{I['bolt']} Louisiana</span>
      <span class="chip">{I['bolt']} North Carolina</span>
    </div>
  </div>
</section>

<div class="google-band"><div class="wrap" data-reveal>
  <div class="g-score">
    <span class="g-num">5.0</span>
    <span><span class="g-stars">{I['star']}{I['star']}{I['star']}{I['star']}{I['star']}</span>
    <span class="g-label">Rated on Google</span></span>
  </div>
  <div class="g-actions">
    <a class="btn btn-pine" href="{BIZ['google_page']}" target="_blank" rel="noopener">{I['google']} Open our Google page</a>
    <a class="btn btn-ghost" href="{BIZ['google_page']}" target="_blank" rel="noopener">Leave a review</a>
  </div>
</div></div>
""" + cta_band(
    "Not near a location? Doesn&rsquo;t matter.",
    "The trucks travel and freight goes everywhere. Wherever the equipment sits, the offer stands.",
)

# ================================================================ ABOUT
about_body = page_hero(
    "About",
    "A family that&rsquo;s been buying metal for decades",
    "United Electrical Surplus is the electrical arm of a Gwinnett County family business — "
    "same yard, same handshake, sharper specialty.",
) + f"""
<section>
  <div class="wrap split">
    <div class="split-img" data-reveal><img src="assets/img/photos/warehouse-green.jpg" alt="United Electrical Surplus warehouse floor" loading="lazy"></div>
    <div data-reveal>
      <div class="kicker">The short version</div>
      <h2>Born on a scrap yard. Built for electrical.</h2>
      <p class="lead">The family has run metal through the same Lawrenceville yard for years &mdash;
      recycling, demolition, industrial buyouts. United Electrical Surplus grew out of a simple
      observation: the electrical gear coming across the scale was worth far more than its weight.</p>
      <p>So instead of shredding it, we built the business that pays what it&rsquo;s actually worth.
      Today the electrical side stands on its own &mdash; a stocked warehouse, a national buying
      operation, and customers on both sides of the counter: sellers who want top dollar and
      contractors who want name-brand gear without the distributor markup.</p>
      <ul class="checks">
        <li>{CHECK24}<span><b>Specialists, not generalists</b> &mdash; electrical is all we do here.</span></li>
        <li>{CHECK24}<span><b>Family-run</b> &mdash; you deal with an owner, not a purchasing portal.</span></li>
        <li>{CHECK24}<span><b>Straight numbers</b> &mdash; one honest offer, cash behind it.</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="tight band-dark">
  <div class="wrap">
    <div class="stat-row" data-reveal>
      <div class="stat"><b>2</b><span>Georgia locations</span></div>
      <div class="stat"><b>6+</b><span>Major brands stocked</span></div>
      <div class="stat"><b>40k lbs</b><span>Crane lift capability</span></div>
      <div class="stat"><b>5.0</b><span>Google rating</span></div>
    </div>
  </div>
</section>

<section style="background:var(--white)">
  <div class="wrap">
    <div class="section-head center" data-reveal>
      <div class="kicker">How we work</div>
      <h2>Three promises on every deal</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal><h3>The best number</h3><p>We pay more than anyone for surplus electrical &mdash; and if someone beats
      us, show us the paper and we&rsquo;ll beat them back.</p></div>
      <div class="step" data-reveal><h3>No homework for you</h3><p>No palletizing, no freight quotes, no waiting on a check. We pick up,
      we load, we pay on the spot.</p></div>
      <div class="step" data-reveal><h3>Gear you can trust</h3><p>On the selling side, everything is checked before it ships. A surplus
      price should never mean a surplus gamble.</p></div>
    </div>
  </div>
</section>
""" + cta_band(
    "Deal with people, not portals.",
    f"Call {BIZ['phone_disp']} and you&rsquo;re talking to the family that owns the place.",
)

# ================================================================ CONTACT
contact_body = page_hero(
    "Contact",
    "Talk to a buyer today",
    "Text photos for the fastest offer, call to check stock, or drop a line with the form — "
    "every message gets a same-day answer.",
) + f"""
<section class="tight">
  <div class="wrap info-grid">
    <div class="info-card" data-reveal>
      <h3>{I['phone']} Call or text</h3>
      <p><a href="tel:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a><br>
      Texted photos get the fastest offers.<br>{BIZ['hours']}</p>
    </div>
    <div class="info-card" data-reveal>
      <h3>{I['mail']} Email</h3>
      <p><a href="mailto:{BIZ['email']}">{BIZ['email']}</a><br>
      <a href="mailto:{BIZ['email2']}">{BIZ['email2']}</a></p>
    </div>
    <div class="info-card" data-reveal>
      <h3>{I['pin']} Visit</h3>
      <p>{BIZ['addr1']}<br>{BIZ['addr2']}<br>
      <a href="locations.html">Maps &amp; directions</a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div data-reveal>
      <div class="kicker">Message us</div>
      <h2>What can we price for you?</h2>
      <p class="lead">Selling, buying, or clearing a building &mdash; give us the short version here
      and we&rsquo;ll call you back with numbers.</p>
      <div class="chip-row light" style="margin-bottom:26px">
        <a class="chip" href="{BIZ['google_page']}" target="_blank" rel="noopener" style="text-decoration:none">{I['google']} Google Business Profile</a>
        <a class="chip" href="{BIZ['facebook']}" target="_blank" rel="noopener" style="text-decoration:none">{I['fb']} Facebook</a>
        <a class="chip" href="{BIZ['google_page']}" target="_blank" rel="noopener" style="text-decoration:none">{I['star']} Leave a Google review</a>
      </div>
      <div class="map-frame"><iframe src="{MAP1}" title="Map — United Electrical Surplus, Lawrenceville GA" loading="lazy"></iframe></div>
    </div>
    <div class="form-card" data-reveal>
      <form name="contact" method="POST" data-netlify="true" action="thank-you.html">
        <input type="hidden" name="form-name" value="contact">
        <input type="hidden" name="source" value="United Electrical Surplus demo — contact page">
        <div class="form-grid">
          <div><label for="c-name">Name</label><input id="c-name" name="name" type="text" required autocomplete="name"></div>
          <div><label for="c-phone">Phone</label><input id="c-phone" name="phone" type="tel" required autocomplete="tel"></div>
          <div class="full"><label for="c-email">Email (optional)</label><input id="c-email" name="email" type="email" autocomplete="email"></div>
          <div class="full"><label for="c-topic">I want to&hellip;</label>
            <select id="c-topic" name="topic">
              <option>Sell surplus equipment</option>
              <option>Buy equipment / check stock</option>
              <option>Schedule a pickup or site visit</option>
              <option>Something else</option>
            </select></div>
          <div class="full"><label for="c-msg">The details</label><textarea id="c-msg" name="details" required placeholder="Brands, quantities, part numbers, where it's located — whatever you know"></textarea></div>
          <div class="full"><button class="btn btn-gold" type="submit" style="width:100%">Send it</button></div>
        </div>
        <p class="form-note"><b>Demo note:</b> while this site is a preview, submissions go to
        60 Minute Sites so the owner can watch the leads come in &mdash; on the live site they go straight to the shop.</p>
      </form>
    </div>
  </div>
</section>
"""

# ================================================================ THANK YOU / 404
thanks_body = f"""
<section style="min-height:48vh;display:flex;align-items:center">
  <div class="wrap" style="text-align:center;max-width:640px">
    <div class="kicker" style="justify-content:center">Message received</div>
    <h1 style="font-size:clamp(2rem,4.5vw,3.2rem)">We&rsquo;re on it.</h1>
    <p class="lead" style="margin:0 auto 30px">Expect a same-day response during business hours.
    In a hurry? Text photos straight to <a href="sms:{BIZ['phone_tel']}">{BIZ['phone_disp']}</a>.</p>
    <a class="btn btn-pine" href="index.html">Back to the homepage</a>
  </div>
</section>
"""

e404_body = f"""
<section style="min-height:48vh;display:flex;align-items:center">
  <div class="wrap" style="text-align:center;max-width:640px">
    <div class="kicker" style="justify-content:center">404</div>
    <h1 style="font-size:clamp(2rem,4.5vw,3.2rem)">That page tripped the breaker.</h1>
    <p class="lead" style="margin:0 auto 30px">The link is dead, but the inventory isn&rsquo;t.</p>
    <a class="btn btn-gold" href="index.html">Back to the homepage</a>
  </div>
</section>
"""

# ================================================================ pages table
PAGES = [
    ("index.html", "United Electrical Surplus — We Pay More for Surplus Electrical Equipment",
     "Cash on the spot for surplus circuit breakers, panels, switchgear and transformers — Square D, Siemens, Eaton, ABB, GE. Lawrenceville & Buford GA, buying nationwide. 404-831-3600.",
     index_body, schema),
    ("sell.html", "Sell Surplus Electrical Equipment for Cash | United Electrical Surplus",
     "We pay more than anyone for surplus breakers, panelboards, switchgear, transformers, bus duct and motor controls. Text photos to 404-831-3600 for a same-day cash offer.",
     sell_body, ""),
    ("buy.html", "Buy Surplus Electrical Equipment | United Electrical Surplus",
     "Name-brand surplus electrical equipment — Square D breakers, panels, switchgear, transformers, wire — tested, guaranteed and shipped nationwide from Lawrenceville, GA.",
     buy_body, ""),
    ("pickup.html", "Equipment Pickup & Logistics | United Electrical Surplus",
     "Tractors, trailers and crane lifts past 40,000 lbs. We pick up surplus electrical equipment on your site and pay cash on the spot. 404-831-3600.",
     pickup_body, ""),
    ("locations.html", "Locations & Service Area | United Electrical Surplus",
     "Two Georgia locations — Lawrenceville HQ and Buford — with expansion underway across Texas, Louisiana, Oklahoma, the Carolinas and the Southeast.",
     locations_body, ""),
    ("about.html", "About Us | United Electrical Surplus",
     "The electrical arm of a Lawrenceville family metals business: specialist buyers, a stocked warehouse and one honest cash offer at a time.",
     about_body, ""),
    ("contact.html", "Contact | United Electrical Surplus",
     "Call or text 404-831-3600, email info@unitedelectricalsurplus.com, or send the form — every message gets a same-day answer.",
     contact_body, ""),
    ("thank-you.html", "Thanks — Message Received | United Electrical Surplus",
     "Your message is in. Expect a same-day response from United Electrical Surplus.",
     thanks_body, ""),
    ("404.html", "Page Not Found | United Electrical Surplus",
     "That page doesn't exist — but the surplus electrical inventory does.",
     e404_body, ""),
]


def build():
    for fname, title, desc, body, extra in PAGES:
        html = (head(title, desc, fname) + extra + chrome_top(fname) + body + chrome_footer())
        with open(os.path.join(ROOT, fname), "w") as f:
            f.write(html)
        print("wrote", fname)

    # sitemap
    urls = "\n".join(
        f"  <url><loc>{BIZ['domain']}/{p[0]}</loc></url>"
        for p in PAGES if p[0] not in ("404.html", "thank-you.html")
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                f"{urls}\n</urlset>\n")
    print("wrote sitemap.xml")


if __name__ == "__main__":
    build()
