#!/usr/bin/env python3
"""Round-trip the editable copy of this site.

  python3 _copy/copytool.py export [group]   page(s) -> _copy/*.md
  python3 _copy/copytool.py apply  [group]   _copy/*.md -> page(s)
  python3 _copy/copytool.py check  [group]   verify the two are in sync

Groups: "site" (hero and intro copy across the site), "ai-safety" (the
/ai-safety landing page), or omit for both.

Most editable strings live in an HTML element carrying data-copy="ID". One
lives in _config.yml. This script is the only thing that should move text
between the pages and the copy files, so the IDs cannot drift out of alignment.

Jekyll ignores any directory whose name starts with "_", so nothing here is
published.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY_DIR = ROOT / "_copy"

GROUPS = {
    "site": COPY_DIR / "site-copy.md",
    "ai-safety": COPY_DIR / "ai-safety-copy.md",
}

# id -> (group, file, band, where it appears, editing note)
# file is a page path, or "_config.yml:<key>" for a YAML value.
S = {}


def slot(sid, group, f, band, where, note):
    S[sid] = (group, f, band, where, note)


# ─── site: homepage hero ─────────────────────────────────────────────────
G, F, B = "site", "index.html", "Homepage · Hero"
slot("HOME-EYEBROW", G, F, B, "Small gold uppercase line above your name", "Short. Uppercased by CSS. Currently carries the 'Available 2027' signal.")
slot("HOME-TAGLINE", G, F, B, "Italic serif line under your name", "One or two sentences. The first thing that reads as a positioning statement.")
slot("HOME-BIO", G, F, B, "The main hero paragraph", "The most-read copy on the site. <strong> is bright white; links are gold.")
slot("HOME-CATEGORIES", G, F, B, "Grey keyword line under the bio", "Separated by &middot;. These are SEO keywords as much as description.")

B = "Homepage · Cards"
slot("HOME-CARD-RESEARCH", G, F, B, "Description inside the wide Research card", "2-3 sentences.")
slot("HOME-CARD-AISAFETY", G, F, B, "Description inside the Youth AI Safety card", "2 sentences. Links to /ai-safety.")

# ─── site: about ─────────────────────────────────────────────────────────
F, B = "aboutme.md", "About · Header"
slot("ABOUT-SUBTITLE", G, F, B, "Grey line under the 'About Me' heading", "Separated by &middot;. Three short phrases.")
B = "About · Intro"
slot("ABOUT-INTRO-1", G, F, B, "First paragraph, beside your headshot", "Your research statement in your own voice.")
slot("ABOUT-INTRO-2", G, F, B, "Second paragraph, beside your headshot", "The children's-privacy-as-throughline argument. Links to /ai-safety.")
B = "About · Body"
slot("ABOUT-CREDENTIALS", G, F, B, "Paragraph about the MLS and publication venues", "Credentials and affiliations.")
slot("ABOUT-CLOSING", G, F, B, "Final paragraph, the availability and contact pitch", "Carries the 2027 timeline and the roles you want.")

# ─── site: research ──────────────────────────────────────────────────────
F, B = "research.md", "Research · Header"
slot("RESEARCH-SUBTITLE", G, F, B, "Grey line under the 'Research' heading", "Sets up the three-question structure.")
B = "Research · Panel intros"
slot("RESEARCH-INTRO-RESEARCHERS", G, F, B, "Boxed intro on the 'For Researchers' tab", "The program statement. Links to /ai-safety.")
slot("RESEARCH-INTRO-PRACTITIONERS", G, F, B, "Boxed intro on the 'For Practitioners' tab", "Aimed at policy and industry readers.")
B = "Research · Pillar descriptions"
slot("RESEARCH-PILLAR-1-DESC", G, F, B, "Body of the 'Who Controls...' pillar card", "Long.")
slot("RESEARCH-PILLAR-2-DESC", G, F, B, "Body of the 'How Institutions Govern...' pillar card", "Long.")
slot("RESEARCH-PILLAR-3-DESC", G, F, B, "Body of the 'When Young People Want...' pillar card", "Long. The pillar that exists nowhere else on the site.")
B = "Research · Practitioner accordion"
slot("RESEARCH-Q-1", G, F, B, "Clickable question, Pillar 1 card", "Phrased as a question.")
slot("RESEARCH-Q-3", G, F, B, "Clickable question, Pillar 3 card", "Phrased as a question.")
slot("RESEARCH-Q-4", G, F, B, "Clickable question, Related/scams card", "Phrased as a question.")
slot("RESEARCH-SOWHAT-3", G, F, B, "'Why it matters' text inside the Pillar 3 card", "The youth-preferences argument.")

# ─── site: press, CV, shared ─────────────────────────────────────────────
F, B = "press.md", "Press"
slot("PRESS-SUBTITLE", G, F, B, "Grey line under the 'Press & Media' heading", "Very short.")
slot("PRESS-INTRO", G, F, B, "First paragraph", "What your press coverage has been about.")
slot("PRESS-CONTACT", G, F, B, "Second paragraph, the media-inquiry pitch", "Lists the topics you will speak on.")

F, B = "CV.md", "CV"
slot("CV-ROLE", G, F, B, "Grey line under your name at the top of the CV", "Three short phrases split by &middot;. This is your one-line self-description.")

F, B = "_includes/shared-cta.html", "Shared"
slot("SHARED-CTA", G, F, B, "The call-to-action box that appears at the bottom of research, about, press and /ai-safety", "One sentence. Appears on 4+ pages, so it is the most repeated copy on the site.")

F, B = "_config.yml:description", "Shared"
slot("CONFIG-DESCRIPTION", G, F, B, "The site-wide meta description, used on the homepage and in search results", "Under ~300 characters. Plain text only, no HTML.")

# ─── /ai-safety ──────────────────────────────────────────────────────────
G, F = "ai-safety", "ai-safety.md"
B = "Band 1 · Hero"
slot("AS-HERO-EYEBROW", G, F, B, "Small gold uppercase line above the headline", "2-5 words. Uppercased by CSS, so type it in normal case.")
slot("AS-HERO-H1", G, F, B, "The big serif headline, largest text on the page", "Under ~10 words. <em>word</em> renders gold italic. This is the page's H1 and its main SEO signal.")
slot("AS-HERO-P1", G, F, B, "First lede paragraph under the headline", "2-3 sentences. This is the claim; the rest of the page defends it.")
slot("AS-HERO-P2", G, F, B, "Second lede paragraph", "Names the three pillars. <strong> renders bright white.")
slot("AS-HERO-BYLINE", G, F, B, "Credential card beside your headshot", "Keep to 2 lines. <br> is the line break. Contains a link to youthaisafety.com.")

B = "Band 2 · The argument"
slot("AS-ARG-LABEL", G, F, B, "Small uppercase section label", "2-5 words. Uppercased by CSS.")
slot("AS-ARG-SUBLABEL", G, F, B, "Italic grey line under the label", "One sentence.")
for i, n in ((1, "01"), (2, "02"), (3, "03")):
    slot(f"AS-CLAIM-{i}-TITLE", G, F, B, f"Heading for numbered claim {n}", "Under ~7 words. Renders as an H2.")
    slot(f"AS-CLAIM-{i}-BODY", G, F, B, f"Body for claim {n}", "2-3 sentences.")

B = "Band 3 · Pillars"
slot("AS-PILLARS-LABEL", G, F, B, "Small uppercase section label", "2-5 words.")
slot("AS-PILLARS-SUBLABEL", G, F, B, "Italic grey line under the label", "One sentence.")
_pnote = {1: "2-3 sentences. Summary only; the depth lives on /research.",
          2: "2-3 sentences.",
          3: "2-3 sentences. This is the pillar that exists nowhere else on the site."}
for i in (1, 2, 3):
    slot(f"AS-PILLAR-{i}-KICKER", G, F, B, f"Gold kicker above pillar {i}", "Short. Uppercased by CSS.")
    slot(f"AS-PILLAR-{i}-TITLE", G, F, B, f"Pillar {i} heading", "Must match the pillar name on /research. Renders as an H2.")
    slot(f"AS-PILLAR-{i}-BODY", G, F, B, f"Pillar {i} summary", _pnote[i])
    slot(f"AS-PILLAR-{i}-LINK", G, F, B, f"Link text at the end of pillar {i}'s chip row", "Points to /research.")

B = "Band 4 · Workshop series"
slot("AS-WORKSHOP-KICKER", G, F, B, "Gold kicker at the top of the boxed block", "Short. Uppercased by CSS.")
slot("AS-WORKSHOP-TITLE", G, F, B, "Heading of the boxed block", "Renders as an H2.")
slot("AS-WORKSHOP-BODY", G, F, B, "Paragraph inside the box", "2-3 sentences.")
slot("AS-WORKSHOP-LINK-1", G, F, B, "Label on the CHI '26 button", "Fits on one line beside the badge.")
slot("AS-WORKSHOP-LINK-2", G, F, B, "Label on the ASSETS '26 button", "Fits on one line beside the badge.")
slot("AS-WORKSHOP-HUB", G, F, B, "Small grey line under the buttons", "Contains the link to youthaisafety.com.")

B = "Band 5 · Who this is for"
slot("AS-AUDIENCE-LABEL", G, F, B, "Small uppercase section label", "Short.")
slot("AS-AUDIENCE-SUBLABEL", G, F, B, "Italic grey line under the label", "One sentence.")
_aud = {1: ("AI labs", "Links to your email."), 2: ("policymakers", "Links to /research."),
        3: ("journalists", "Links to /press.")}
for i in (1, 2, 3):
    who, link = _aud[i]
    slot(f"AS-AUD-{i}-KICKER", G, F, B, f"Gold kicker, card {i} of 3 ({who})", "Names the audience. Uppercased by CSS.")
    slot(f"AS-AUD-{i}-BODY", G, F, B, f"Card {i} body", "2-3 sentences. Keep the three cards close in length so they sit level.")
    slot(f"AS-AUD-{i}-LINK", G, F, B, f"Card {i} call to action", link)

B = "Band 6 · Selected record"
slot("AS-RECORD-LABEL", G, F, B, "Small uppercase section label", "Short.")
for i in (1, 2, 3, 4):
    slot(f"AS-RECORD-{i}-NUM", G, F, B, f"Gold serif line, column {i} of 4", "1-3 words. Long text wraps badly.")
    slot(f"AS-RECORD-{i}-LABEL", G, F, B, f"Grey caption under column {i}", "Two short lines split by <br>.")


HEADER = """<!--
  EDITABLE COPY — {group}
  ========================================================================
  Generated from the site's pages and written back into them.

  HOW TO EDIT
    Change only the text BELOW each "TEXT:" line. Leave the ## [ID] headers,
    the WHERE: lines and the NOTE: lines alone. Blocks may be any length.
    Delete a whole block if its text should stay as it is.

  WHAT YOU CAN PUT IN THE TEXT
    Plain text, plus these inline tags, which the pages already style:
      <strong>...</strong>   bright white emphasis
      <em>...</em>           gold italic
      <a href="...">...</a>  a link
      <br>                   a line break
      &middot;  &rarr;  &ndash;  &amp;   punctuation entities
    CONFIG-DESCRIPTION is the one exception: plain text only, no tags.

  ROUND-TRIP
    python3 _copy/copytool.py apply {group}
    python3 _copy/copytool.py check {group}
-->

"""


# ─── extraction ───────────────────────────────────────────────────────────
class Extractor(HTMLParser):
    """Collect the inner HTML of every element carrying data-copy."""

    VOID = {"br", "img", "meta", "link", "hr", "input", "source", "area"}

    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.found = {}
        self.spans = {}
        self._stack = []
        self._depth = 0

    def _offset(self):
        line, col = self.getpos()
        return self._line_starts[line - 1] + col

    def feed(self, data):
        self._line_starts = [0]
        for i, ch in enumerate(data):
            if ch == "\n":
                self._line_starts.append(i + 1)
        super().feed(data)

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self._depth += 1
        cid = dict(attrs).get("data-copy")
        if cid:
            start = self.src.index(">", self._offset()) + 1
            self._stack.append((tag, cid, start, self._depth))

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self._stack and self._stack[-1][0] == tag and self._stack[-1][3] == self._depth:
            _, cid, start, _ = self._stack.pop()
            end = self._offset()
            self.found[cid] = self.src[start:end]
            self.spans[cid] = (start, end)
        self._depth -= 1


def tidy(s):
    s = re.sub(r"\s*\n\s*", " ", s)
    return re.sub(r"[ \t]{2,}", " ", s).strip()


def read_yaml_slot(spec):
    fname, key = spec.split(":", 1)
    src = (ROOT / fname).read_text(encoding="utf-8")
    m = re.search(rf'^{re.escape(key)}:[ \t]*"(.*)"[ \t]*$', src, re.M)
    if not m:
        sys.exit(f"{fname}: could not find a quoted '{key}:' value")
    return m.group(1)


def write_yaml_slot(spec, value):
    fname, key = spec.split(":", 1)
    path = ROOT / fname
    src = path.read_text(encoding="utf-8")
    new = re.sub(rf'^{re.escape(key)}:[ \t]*".*"[ \t]*$',
                 f'{key}: "{value}"', src, count=1, flags=re.M)
    path.write_text(new, encoding="utf-8")


_page_cache = {}


def page_data(fname):
    if fname not in _page_cache:
        src = (ROOT / fname).read_text(encoding="utf-8")
        ex = Extractor(src)
        ex.feed(src)
        ex.close()
        _page_cache[fname] = (src, ex.found, ex.spans)
    return _page_cache[fname]


def current_text(sid):
    _, f, _, _, _ = S[sid]
    if ":" in f and f.endswith(tuple(k.split(":")[-1] for k in [f])) and f.startswith("_config"):
        return read_yaml_slot(f)
    _, found, _ = page_data(f)
    if sid not in found:
        return None
    return tidy(found[sid])


# ─── copy-file parsing ────────────────────────────────────────────────────
def parse_copy(path):
    if not path.exists():
        sys.exit(f"missing {path}")
    text = path.read_text(encoding="utf-8")
    blocks, cur, body = {}, None, None

    def close():
        nonlocal cur, body
        if cur and body is not None:
            blocks[cur] = "\n".join(body).strip()
        body = None

    for line in text.splitlines():
        m = re.match(r"^##\s*\[([A-Z0-9-]+)\]\s*$", line)
        if m:
            close()
            cur = m.group(1)
            continue
        if body is not None and (re.match(r"^-{3,}\s*$", line) or re.match(r"^#\s", line)):
            close()
            cur = None
            continue
        if cur is None:
            continue
        if body is None:
            if line.strip() == "TEXT:":
                body = []
            continue
        body.append(line)
    close()
    return {k: v.strip() for k, v in blocks.items()}


def ids_for(group):
    return [i for i in S if S[i][0] == group]


# ─── commands ─────────────────────────────────────────────────────────────
def cmd_export(groups):
    for g in groups:
        out = [HEADER.format(group=g)]
        band = None
        n = 0
        for sid in ids_for(g):
            _, f, b, where, note = S[sid]
            cur = current_text(sid)
            if cur is None:
                sys.exit(f"{sid}: no data-copy=\"{sid}\" found in {f}")
            if b != band:
                band = b
                out.append(f"\n# {b}\n")
            out.append(f"## [{sid}]")
            out.append(f"WHERE: {where}")
            out.append(f"FILE:  {f}")
            out.append(f"NOTE:  {note}")
            out.append("TEXT:")
            out.append(cur)
            out.append("")
            out.append("---")
            out.append("")
            n += 1
        GROUPS[g].parent.mkdir(exist_ok=True)
        GROUPS[g].write_text("\n".join(out), encoding="utf-8")
        print(f"exported {n} blocks -> {GROUPS[g].relative_to(ROOT)}")


def cmd_apply(groups):
    total = []
    for g in groups:
        edits = parse_copy(GROUPS[g])
        unknown = set(edits) - set(ids_for(g))
        if unknown:
            sys.exit(f"{GROUPS[g].name} has unknown IDs: {sorted(unknown)}")

        # group HTML edits by file so offsets stay valid
        by_file = {}
        for sid, new in edits.items():
            new = new.strip()
            if not new:
                continue
            cur = current_text(sid)
            if cur == new:
                continue
            _, f, _, _, _ = S[sid]
            by_file.setdefault(f, []).append((sid, new))

        for f, items in by_file.items():
            if f.startswith("_config"):
                for sid, new in items:
                    if "<" in new:
                        sys.exit(f"{sid}: the config description must be plain text, no HTML")
                    write_yaml_slot(f, new)
                    total.append(sid)
                continue
            src, found, spans = page_data(f)
            for sid, new in sorted(items, key=lambda t: spans[t[0]][0], reverse=True):
                start, end = spans[sid]
                line_start = src.rfind("\n", 0, start) + 1
                indent = " " * (len(src[line_start:]) - len(src[line_start:].lstrip()) + 2)
                if len(new) + len(indent) > 110:
                    lines, line = [], ""
                    for word in new.split(" "):
                        if line and len(line) + len(word) + 1 > 104:
                            lines.append(line)
                            line = ""
                        line = f"{line} {word}".strip()
                    lines.append(line)
                    body = "\n".join(indent + l for l in lines)
                    new_src = "\n" + body + "\n" + indent[:-2]
                else:
                    new_src = new
                src = src[:start] + new_src + src[end:]
                total.append(sid)
            (ROOT / f).write_text(src, encoding="utf-8")
            _page_cache.pop(f, None)

    if not total:
        print("no changes: the pages already match the copy files")
        return
    print(f"applied {len(total)} change(s):")
    for sid in sorted(total):
        _, f, b, where, _ = S[sid]
        print(f"  {sid}\n      {f} — {b} — {where}")


def cmd_check(groups):
    problems = []
    for g in groups:
        edits = parse_copy(GROUPS[g])
        for sid in ids_for(g):
            cur = current_text(sid)
            if cur is None:
                problems.append(f"{sid}: not found in {S[sid][1]}")
            elif sid not in edits:
                problems.append(f"{sid}: missing from {GROUPS[g].name}")
            elif cur != edits[sid].strip():
                problems.append(f"{sid}: page and copy file differ")
        for sid in set(edits) - set(ids_for(g)):
            problems.append(f"{sid}: in {GROUPS[g].name} but not registered")
    # every data-copy in every referenced page must be registered
    for f in {S[i][1] for i in S if not S[i][1].startswith("_config")}:
        _, found, _ = page_data(f)
        for sid in set(found) - set(S):
            problems.append(f"{sid}: data-copy in {f} with no registered slot")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    n = sum(len(ids_for(g)) for g in groups)
    print(f"in sync: {n} copy blocks match across {len(groups)} group(s)")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    which = sys.argv[2:] or list(GROUPS)
    bad = [g for g in which if g not in GROUPS]
    if bad:
        sys.exit(f"unknown group(s) {bad}; choose from {list(GROUPS)}")
    fn = {"export": cmd_export, "apply": cmd_apply, "check": cmd_check}.get(cmd)
    if not fn:
        sys.exit("usage: copytool.py [export|apply|check] [site|ai-safety]")
    fn(which)
