/* United Electrical Surplus — site behaviour.
   Sections 1-4 are the real site. Section 5 is demo-only and gets deleted
   at launch (see DEMO-NOTES.md). */
(function () {
  "use strict";

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ------------------------------------------------- 1. sticky header */
  var header = $(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ------------------------------------------------- 2. mobile nav */
  var burger = $(".nav-burger");
  var nav = $(".main-nav");
  if (burger && nav) {
    burger.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$("a", nav).forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
    document.addEventListener("click", function (e) {
      if (!nav.contains(e.target) && e.target !== burger) {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ------------------------------------------------- 3. reveal on scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    $$("[data-reveal]").forEach(function (el) { io.observe(el); });
  } else {
    $$("[data-reveal]").forEach(function (el) { el.classList.add("in"); });
  }

  /* ------------------------------------------------- 4. gallery lightbox */
  $$("[data-lightbox]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var box = document.createElement("div");
      box.className = "lightbox";
      var img = document.createElement("img");
      img.src = a.getAttribute("href");
      img.alt = a.querySelector("img") ? a.querySelector("img").alt : "";
      box.appendChild(img);
      box.addEventListener("click", function () { box.remove(); });
      document.addEventListener("keydown", function esc(ev) {
        if (ev.key === "Escape") { box.remove(); document.removeEventListener("keydown", esc); }
      });
      document.body.appendChild(box);
    });
  });

  /* ------------------------------------------------- 5. DEMO modal — delete at launch */
  var openers = $$("[data-demo-open]");
  if (openers.length) {
    var modal = null;
    var closeModal = function () {
      if (!modal) return;
      modal.classList.remove("is-on");
      setTimeout(function () { if (modal) { modal.remove(); modal = null; } }, 220);
    };
    var openModal = function () {
      if (modal) return;
      modal = document.createElement("div");
      modal.className = "demo-modal";
      modal.innerHTML =
        '<div class="dm-card" role="dialog" aria-modal="true" aria-label="About this demo">' +
        '<button type="button" class="dm-close" aria-label="Close">' +
        '<svg viewBox="0 0 16 16"><path d="M2.146 2.854a.5.5 0 1 1 .708-.708L8 7.293l5.146-5.147a.5.5 0 0 1 .708.708L8.707 8l5.147 5.146a.5.5 0 0 1-.708.708L8 8.707l-5.146 5.147a.5.5 0 0 1-.708-.708L7.293 8z"/></svg></button>' +
        "<h2>This is a design preview</h2>" +
        "<p>This site is a free, no-strings concept built for United Electrical Surplus by " +
        '<a href="https://60minutesites.com" target="_blank" rel="noopener">60 Minute Sites</a>. ' +
        "Nothing is final &mdash; every photo, headline, price point and page can be changed, and the photography " +
        "was pulled from the current unitedelectricalsurplus.com so you can see your own inventory in the new design.</p>" +
        "<p>While it&rsquo;s a demo, the contact forms deliver to 60 Minute Sites rather than to the shop, " +
        "and the Facebook link is a stand-in until the page link is confirmed. " +
        "When it goes live, everything points at you.</p>" +
        '<p class="dm-foot">Questions? <a href="https://60minutesites.com" target="_blank" rel="noopener">60minutesites.com</a></p>' +
        "</div>";
      modal.addEventListener("click", function (e) { if (e.target === modal) closeModal(); });
      modal.querySelector(".dm-close").addEventListener("click", closeModal);
      document.addEventListener("keydown", function esc(ev) {
        if (ev.key === "Escape") { closeModal(); document.removeEventListener("keydown", esc); }
      });
      document.body.appendChild(modal);
      requestAnimationFrame(function () { modal.classList.add("is-on"); });
    };
    openers.forEach(function (b) { b.addEventListener("click", openModal); });
  }
})();
