#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renders index.html from content.py. No dependencies beyond the standard library.

    python3 build.py            # write index.html
    python3 build.py --serve    # write index.html, then serve on :8000
"""

import datetime
import html
import re
import sys

import content

OUT = "index.html"


# ---------------------------------------------------------------- text helpers

def md(text):
    """Tiny inline-Markdown renderer: links, bold, italic, code."""
    if not text:
        return ""
    out = html.escape(text.strip())
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", out)
    return out


def paragraphs(text):
    """Multi-paragraph block; lines starting with '- ' become a list."""
    if not text:
        return ""
    blocks, chunks = [], re.split(r"\n\s*\n", text.strip())
    for chunk in chunks:
        lines = [l.strip() for l in chunk.strip().splitlines()]
        if lines and lines[0].startswith("- "):
            items = []
            current = ""
            for line in lines:
                if line.startswith("- "):
                    if current:
                        items.append(current)
                    current = line[2:]
                else:
                    current += " " + line
            if current:
                items.append(current)
            blocks.append(
                "<ul>" + "".join("<li>%s</li>" % md(i) for i in items) + "</ul>"
            )
        else:
            blocks.append("<p>%s</p>" % md(" ".join(lines)))
    return "\n".join(blocks)


def fmt_date(iso):
    d = datetime.date(*[int(x) for x in iso.split("-")])
    return d, d.strftime("%b %-d"), d.strftime("%A, %B %-d, %Y")


def slug(s):
    """Stable anchor for a session: from its date if it has one, else its title."""
    if s.get("date"):
        d, _, _ = fmt_date(s["date"])
        return "lecture-" + d.strftime("%b-%d").lower()
    text = re.sub(r"[^a-z0-9]+", "-", s["title"].lower()).strip("-")
    return "topic-" + "-".join(text.split("-")[:5])


# ---------------------------------------------------------------- section HTML

def pretty_date(iso):
    """'2026-07' -> 'Jul 2026'; a bare '2026' passes through."""
    parts = iso.split("-")
    if len(parts) == 1:
        return parts[0]
    d = datetime.date(int(parts[0]), int(parts[1]), 1)
    return d.strftime("%b %Y")


def render_reading(key):
    """Reading list rows: date, then the title as the link. No authors."""
    r = content.READINGS[key]
    return (
        '<li><span class="refdate">%s</span>'
        '<a class="reftitle" href="%s">%s</a></li>'
        % (
            html.escape(pretty_date(r["date"])),
            html.escape(r["url"]),
            html.escape(r["title"]),
        )
    )


def render_session(s, n):
    sid = slug(s)
    off = "off" in s.get("tags", []) or "no class" in s.get("tags", [])

    # The left column shows a real date once one is set, and a week number until then.
    if s.get("date"):
        d, short, long_date = fmt_date(s["date"])
        marker = (
            '<time datetime="%s" title="%s">%s</time><span class="dow">%s</span>'
            % (s["date"], long_date, short, d.strftime("%a"))
        )
    else:
        marker = '<span class="wk">Week</span><span class="wknum">%d</span>' % n

    tags = "".join(
        '<span class="tag tag-%s">%s</span>'
        % (re.sub(r"[^a-z]", "", t.lower()), html.escape(t))
        for t in s.get("tags", [])
    )

    body = ['<div class="s-main">']
    body.append(
        '<h3 class="s-title">%s<a class="anchor" href="#%s" aria-label="Link to this session">#</a></h3>'
        % (md(s["title"]), sid)
    )
    if tags:
        body.append('<div class="tags">%s</div>' % tags)
    if s.get("summary"):
        body.append('<p class="s-summary">%s</p>' % md(s["summary"]))
    if s.get("readings"):
        body.append('<div class="s-readings"><h4>Readings</h4><ul class="reflist">')
        body.append("".join(render_reading(k) for k in s["readings"]))
        body.append("</ul></div>")
    if s.get("note"):
        body.append('<p class="s-note">%s</p>' % md(s["note"]))
    if s.get("links"):
        body.append(
            '<p class="s-links">%s</p>'
            % " · ".join(
                '<a href="%s">%s</a>' % (html.escape(u), html.escape(t))
                for t, u in s["links"]
            )
        )
    body.append("</div>")

    return (
        '<article class="session%s" id="%s">'
        '<div class="s-date">%s</div>\n%s\n</article>'
        % (" session-off" if off else "", sid, marker, "\n".join(body))
    )


def render_schedule():
    out, week = [], 0
    for u in content.UNITS:
        out.append('<section class="unit" id="unit-%d">' % u["num"])
        out.append(
            '<div class="unit-head"><span class="unit-num">Part %d</span>'
            '<h2 class="unit-title">%s</h2></div>' % (u["num"], md(u["title"]))
        )
        if u.get("blurb"):
            out.append('<p class="unit-blurb">%s</p>' % md(u["blurb"]))
        out.append('<div class="sessions">')
        for s in u["sessions"]:
            week += 1
            out.append(render_session(s, week))
        out.append("</div></section>")
    return "\n".join(out)


def render_bibliography():
    """Every reading in chronological order. Flip reverse=True for newest first."""
    keys = sorted(
        content.READINGS,
        key=lambda k: (content.READINGS[k]["date"], content.READINGS[k]["title"]),
        reverse=False,
    )
    return "".join(render_reading(k) for k in keys)


def render_facts():
    return "".join(
        '<div class="fact"><dt>%s</dt><dd>%s</dd></div>' % (html.escape(k), md(v))
        for k, v in content.FACTS
    )


def render_grading():
    return "".join(
        '<div class="grade-row"><div class="grade-pct">%s</div>'
        '<div class="grade-body"><h3>%s</h3><p>%s</p></div></div>'
        % (html.escape(pct), md(name), md(desc))
        for pct, name, desc in content.GRADING
    )


def render_speakers():
    if not content.SPEAKERS:
        return '<p class="tbd">%s</p>' % md(content.SPEAKERS_NOTE)
    rows = "".join(
        "<li><strong>%s</strong><span class=\"aff\">%s</span>"
        '<span class="when">%s</span></li>' % (md(n), md(a), md(w))
        for n, a, w in content.SPEAKERS
    )
    return '<p>%s</p><ul class="speakers">%s</ul>' % (
        md(content.SPEAKERS_NOTE),
        rows,
    )


def render_instructor():
    i = content.INSTRUCTOR
    links = ['<a href="mailto:%s">%s</a>' % (i["email"], html.escape(i["email"]))]
    if i.get("twitter"):
        handle = "@" + i["twitter"].rstrip("/").split("/")[-1]
        links.append('<a href="%s">%s</a>' % (html.escape(i["twitter"]), handle))
    if i.get("url"):
        links.append('<a href="%s">Homepage</a>' % html.escape(i["url"]))
    return (
        '<div class="instructor">'
        '<h3 class="who">%s</h3>'
        '<p class="who-links">%s</p>'
        "%s</div>"
        % (
            html.escape(i["name"]),
            " · ".join(links),
            paragraphs(i.get("bio", "")),
        )
    )


def render_notices():
    if not getattr(content, "NOTICES", None):
        return ""
    return '<div class="notices">%s</div>' % "".join(
        '<p class="notice">%s</p>' % md(n) for n in content.NOTICES
    )


# ---------------------------------------------------------------- page

def build():
    c = content.COURSE
    number = (" " + c["number"]) if c["number"] and c["number"] != "TBD" else ""
    page_title = "%s%s — %s" % (c["title"], number, c["term"])

    show = getattr(content, "SHOW", {})
    nav = [("About", "#about")]
    if show.get("outline"):
        nav.append(("Outline", "#outline"))
    if show.get("logistics"):
        nav.append(("Logistics", "#logistics"))
    if show.get("speakers"):
        nav.append(("Speakers", "#speakers"))
    if show.get("project"):
        nav.append(("Project", "#project"))
    nav += [("Readings", "#readings"), ("Instructor", "#instructor")]
    navhtml = "".join('<a href="%s">%s</a>' % (h, t) for t, h in nav)

    outline_section = ""
    if show.get("outline"):
        outline_section = """
  <section id="outline">
    <h2 class="rule">Course outline</h2>
    <p class="section-note">Four parts, roughly one topic per week. Meeting dates
    will be filled in once the schedule is set; the readings listed are the ones
    each topic is built around.</p>
    %s
  </section>
""" % render_schedule()

    logistics_section = ""
    if show.get("logistics"):
        logistics_section = """
  <section id="logistics">
    <h2 class="rule">Logistics</h2>
    <dl class="facts">%s</dl>

    <h3 class="sub">Prerequisites</h3>
    %s

    <h3 class="sub">Grading</h3>
    <div class="grading">%s</div>
  </section>
""" % (
            render_facts(),
            paragraphs(content.PREREQS),
            render_grading(),
        )

    speakers_section = ""
    if show.get("speakers"):
        speakers_section = """
  <section id="speakers">
    <h2 class="rule">Guest speakers</h2>
    %s
  </section>
""" % render_speakers()

    project_section = ""
    if show.get("project"):
        project_section = """
  <section id="project">
    <h2 class="rule">Final project</h2>
    %s
  </section>
""" % paragraphs(content.PROJECT)

    doc = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title}</title>
<meta name="description" content="{meta}">
<meta property="og:title" content="{title}{number} · {term}">
<meta property="og:description" content="{meta}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#127756;</text></svg>">
</head>
<body>

<header class="site-header">
  <div class="wrap">
    <p class="eyebrow">{institution} · {term}{numsep}</p>
    <h1>{title}</h1>
    <p class="tagline">{tagline}</p>
    <nav class="nav">{nav}</nav>
  </div>
</header>

<main class="wrap">

  {notices}

  <section id="about">
    <h2 class="rule">About the course</h2>
    {description}
    <p class="lead-in">Questions we will try to answer:</p>
    <ul class="questions">{questions}</ul>
  </section>

{outline_section}{logistics_section}{speakers_section}{project_section}
  <section id="readings">
    <h2 class="rule">Readings</h2>
    <p class="section-note">If any of the following looks interesting, this is the
    right class for you.</p>
    <ol class="bibliography">{bibliography}</ol>
  </section>

  <section id="instructor">
    <h2 class="rule">Instructor</h2>
    {instructor_block}
  </section>

</main>

<footer class="site-footer">
  <div class="wrap">
    <p>{title} · {institution} · {term}</p>
    <p>Taught by <a href="mailto:{email}">{instructor}</a>. Last updated {updated}.</p>
  </div>
</footer>

<script>
// Quick eased scroll for in-page nav links, so it reads as one continuous page
// rather than a jump-cut. Falls back to an instant jump if the visitor has asked
// for reduced motion.
(function () {{
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');

  function easeInOutCubic(t) {{
    return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }}

  document.addEventListener('click', function (e) {{
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;

    var link = e.target.closest('a[href^="#"]');
    if (!link) return;

    var id = link.getAttribute('href').slice(1);
    var target = id && document.getElementById(id);
    if (!target) return;

    e.preventDefault();

    var start = window.pageYOffset;
    var end = Math.min(
      target.getBoundingClientRect().top + start - 16,
      document.body.scrollHeight - window.innerHeight
    );
    var distance = end - start;

    var finished = false;
    function done() {{
      if (finished) return;
      finished = true;
      window.scrollTo(0, end);
      history.replaceState(null, '', '#' + id);
      target.setAttribute('tabindex', '-1');
      target.focus({{ preventScroll: true }});
    }}

    if (reduced.matches || Math.abs(distance) < 2) {{
      done();
      return;
    }}

    // Fast: 240ms minimum, scaling with distance but capped at 480ms.
    var duration = Math.min(480, Math.max(240, Math.abs(distance) * 0.25));
    var t0 = performance.now();

    // rAF is throttled in background tabs; this guarantees we land on target
    // even if the animation never gets to run.
    setTimeout(done, duration + 250);

    requestAnimationFrame(function step(now) {{
      if (finished) return;
      var p = Math.min(1, (now - t0) / duration);
      window.scrollTo(0, start + distance * easeInOutCubic(p));
      if (p < 1) requestAnimationFrame(step);
      else done();
    }});
  }});
}})();
</script>

</body>
</html>
""".format(
        page_title=html.escape(page_title),
        title=html.escape(c["title"]),
        number=html.escape(number),
        numsep=html.escape(" · " + c["number"]) if number else "",
        term=html.escape(c["term"]),
        institution=html.escape(c["institution"]),
        tagline=html.escape(c["tagline"]),
        meta=html.escape(c["meta_description"]),
        nav=navhtml,
        notices=render_notices(),
        description=paragraphs(content.DESCRIPTION),
        questions="".join("<li>%s</li>" % md(q) for q in content.QUESTIONS),
        outline_section=outline_section,
        logistics_section=logistics_section,
        speakers_section=speakers_section,
        project_section=project_section,
        bibliography=render_bibliography(),
        instructor_block=render_instructor(),
        instructor=html.escape(content.INSTRUCTOR["name"]),
        email=html.escape(content.INSTRUCTOR["email"]),
        updated=datetime.date.today().strftime("%B %-d, %Y"),
    )

    with open(OUT, "w") as f:
        f.write(doc)
    print("wrote %s (%d sessions)" % (
        OUT, sum(len(u["sessions"]) for u in content.UNITS)))


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import http.server, socketserver
        print("serving http://localhost:8000 — Ctrl-C to stop")
        socketserver.TCPServer.allow_reuse_address = True
        with socketserver.TCPServer(
            ("", 8000), http.server.SimpleHTTPRequestHandler
        ) as httpd:
            httpd.serve_forever()
