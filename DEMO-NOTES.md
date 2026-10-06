# United Electrical Surplus — demo notes

**Client:** Vinnie (Gus's son) · United Electrical Surplus — buys/sells electrical, NOT a scrap/recycling guy
**Phone:** 404-831-3600 ← CONFIRMED the real number (4048303600 was a typo in the intake notes)
**Emails:** info@unitedelectricalsurplus.com + unitedelectricalsurplus@yahoo.com
**Existing site:** unitedelectricalsurplus.com (WordPress/Elementor — the one he wants to leave)
**HQ:** 621 Hurricane Shoals Rd NW, Lawrenceville, GA 30046 (same yard as his dad's United Recycling)
**Second location:** 1901 Peachtree Industrial Blvd, Buford, GA 30518
**Hours:** ALWAYS OPEN — even Sundays (Corban 10/6; matches the GMB "Open 24 hours").
The old site's Mon–Sat 8–6 is wrong.

## The brief (from Corban's notes, 10/6)

- Very classy, huge upgrade from the current site. Design pulls from HIS OWN LOGO
  (green + gold shield — `assets/img/logo.jpg`, white knockout `logo-white.png`).
- "They're paying more than anyone else for electrical equipment" — that is the headline
  everywhere, with cash-on-the-spot messaging (he said: cash, money, Square D breakers).
- Square D front of every brand list.
- Tractors + trailers, they go out and pick it up, large equipment → `pickup.html`.
- Huge cranes, 40,000 lbs+ capability → trust bar + pickup page.
- Both office locations + ALL the expansion states/cities on his site (and Ann's):
  Dallas, Houston, Charlotte, Oklahoma City, New Orleans, Baton Rouge + GA, TN, AL, FL, TX,
  OK, LA, NC → `locations.html` + homepage service-area band.
- Pictures taken from his current website → `assets/img/photos/` (downloaded from his
  WP media library).
- Google page + review links: GMB listing confirmed, 5.0 rating —
  https://maps.google.com/?cid=3954105873428335092 (used for both "find us" and "review" buttons).
- Forms: Netlify forms (`cash-offer` on sell.html, `contact` on contact.html), deliver to
  60MS while it's a demo (demo note shown under each form).

## Later notes applied (Corban, 10/6 afternoon)

- "Square D PowerPact" is the breaker Gus kept talking about — named on index, sell and buy pages.
- Always open, even Sundays → hours updated sitewide + schema.
- More colors → teal + copper accents added alongside the green/gold.
- Atlanta green-and-gold background → stylized Atlanta skyline (SVG) on the homepage
  service-area band and the locations expansion band.
- (678) 548-1941 = note for Corban only (it's what the GMB listing shows) — NOT on the site.

## OPEN ITEMS

0. **"404.831.3699"** appeared in a 10/6 note. The site uses 404-831-3600, which Corban
   confirmed in caps ("4048313600 IS THE REAL NUMBER") and which matches the current website.
   If 3699 is actually a second line (power pack/breaker desk?), it's one string in
   `_generator/build.py`.

1. **Facebook page URL.** Could not find it from the number on the open web, and FB search
   needs a login. The Facebook buttons currently point at a Facebook SEARCH for the business
   name (works, but is a stand-in). Get the real page link from Vinnie — it's one string in
   `_generator/build.py` (`BIZ["facebook"]`) + rebuild.
2. **GMB phone mismatch.** His Google listing shows (678) 548-1941; his site says 404-831-3600.
   Corban confirmed 404-831-3600 is real. The GMB should probably be updated — SEO task.
3. **GMB hours mismatch.** Listing says Open 24 hours, site says Mon–Sat 8–6.
4. **Review deep-link.** Both Google buttons open the Maps listing (CID link). If we want the
   one-tap "write a review" dialog we need the ChIJ place ID — grab it from the GMB dashboard
   once he shares access.
5. **About-page family angle.** Written as "electrical arm of the family metals business" —
   confirm Vinnie wants the scrap-yard connection mentioned at all.
6. **Buford hours** are "by appointment — call ahead" as a placeholder.
7. **Testimonials** from his current site were NOT carried over (they look templated:
   "saved 40% on breakers", Houston/Atlanta names). Get real ones or pull Google reviews.
8. **Send him the link to his phone + his dad's website and they'll go over it** (Corban's
   note 10/6 10:51 AM).

## Build

Static, no dependencies. Edit `_generator/build.py`, then:

    python3 _generator/build.py

Everything (copy, contacts, nav, icons) lives in that one file; the HTML at the root is
generated output but is committed so Netlify can serve the repo as-is.

## At launch

Delete the demo bar div in `chrome_top()`, the `.footer-demo` block in `chrome_footer()`,
section 5 of `assets/js/main.js`, and the `.demo-bar`/`.demo-modal` CSS; rebuild.
