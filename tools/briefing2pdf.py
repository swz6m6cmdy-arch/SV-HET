#!/usr/bin/env python3
"""Wandelt eine Briefing-Ausgabe (Markdown) in ein druckfertiges PDF.

Aufruf:  python3 tools/briefing2pdf.py briefings/2026-09-17-*.md [weitere.md ...]
Ausgabe: neben der Quelldatei bzw. nach --out-dir.
"""
import argparse
import pathlib
import re
import sys
import unicodedata

import markdown
from weasyprint import HTML

# Emoji werden von den installierten Schriften nicht gedeckt und wuerden als
# Leerkaesten erscheinen. Ersatz durch typografisch vorhandene Zeichen.
EMOJI = {
    "⚠️": "▲ ",   # Warnung  -> gefuelltes Dreieck
    "⚠": "▲ ",
    "\U0001f449": "→ ",     # Zeigefinger -> Pfeil
    "\U0001f4d0": "≈ ",     # Geodreieck -> ungefaehr
    "⏰": "",                # Wecker -> entfaellt
    "✅": "✓ ",
    "\U0001f4c4": "",
}

CSS = """
@page {
  size: A4;
  margin: 20mm 18mm 20mm 18mm;
  @top-right {
    content: string(doctitle);
    font-family: "Liberation Sans", sans-serif;
    font-size: 7.5pt; color: #6b6b6b;
  }
  @bottom-left {
    content: "Kommunalbriefing Sachsen-Anhalt";
    font-family: "Liberation Sans", sans-serif;
    font-size: 7.5pt; color: #6b6b6b;
  }
  @bottom-right {
    content: "Seite " counter(page) " von " counter(pages);
    font-family: "Liberation Sans", sans-serif;
    font-size: 7.5pt; color: #6b6b6b;
  }
}
@page :first { @top-right { content: normal; } }

body {
  font-family: "Liberation Serif", serif;
  font-size: 10.5pt; line-height: 1.45; color: #1a1a1a;
  hyphens: auto; -weasy-hyphens: auto;
}
h1 {
  string-set: doctitle content();
  font-family: "Liberation Sans", sans-serif;
  font-size: 19pt; line-height: 1.2; margin: 0 0 2mm 0;
  color: #0f2b46; border-bottom: 2.4pt solid #0f2b46; padding-bottom: 3mm;
}
h2 {
  font-family: "Liberation Sans", sans-serif;
  font-size: 13pt; color: #0f2b46; margin: 9mm 0 3mm 0;
  padding-bottom: 1.4mm; border-bottom: 0.5pt solid #b9c6d2;
  break-after: avoid; break-inside: avoid;
}
h3 {
  font-family: "Liberation Sans", sans-serif;
  font-size: 11pt; color: #21486b; margin: 6mm 0 2mm 0;
  break-after: avoid; break-inside: avoid;
}
h4 { font-family: "Liberation Sans", sans-serif; font-size: 10pt; margin: 4mm 0 1.5mm 0; break-after: avoid; }
p { margin: 0 0 2.6mm 0; text-align: justify; }
ul, ol { margin: 0 0 3mm 0; padding-left: 6mm; }
li { margin-bottom: 1.2mm; }
strong { color: #0b2136; }
em { color: #333; }

/* Kopfzeilenblock der Ausgabe */
.meta { font-family: "Liberation Sans", sans-serif; font-size: 9pt; color: #3d3d3d; margin-bottom: 4mm; }

blockquote {
  margin: 3mm 0; padding: 2.5mm 4mm;
  border-left: 2.5pt solid #b08900; background: #fdf6e3;
  font-size: 9.5pt; break-inside: avoid;
}
blockquote p { margin: 0; text-align: left; }

table {
  width: 100%; border-collapse: collapse; margin: 3mm 0 4mm 0;
  font-size: 9pt; break-inside: avoid;
}
th {
  background: #0f2b46; color: #fff; font-family: "Liberation Sans", sans-serif;
  text-align: left; padding: 1.8mm 2.2mm; font-size: 8.5pt;
}
td { padding: 1.6mm 2.2mm; border-bottom: 0.4pt solid #ccd6e0; vertical-align: top; }
tr:nth-child(even) td { background: #f4f7fa; }

hr { border: none; border-top: 0.4pt solid #ccd6e0; margin: 6mm 0; }

code { font-family: "Liberation Mono", monospace; font-size: 8.8pt; background: #eef2f6; padding: 0 0.7mm; }
a { color: #14456e; text-decoration: none; }

/* Quellenverzeichnis: lange URLs muessen umbrechen duerfen */
.sources { font-size: 8pt; line-height: 1.35; hyphens: none; -weasy-hyphens: none; }
.sources ul { padding-left: 4mm; margin-bottom: 2.5mm; }
.sources li, .sources p {
  margin-bottom: 1mm; text-align: left;
  word-break: break-all; overflow-wrap: anywhere;
}
.sources h2 { break-before: page; }
"""


def clean(text: str) -> str:
    for src, dst in EMOJI.items():
        text = text.replace(src, dst)
    # verbliebene Emoji (Symbol-other) entfernen, damit keine Leerkaesten entstehen
    return "".join(
        c for c in text
        if not (unicodedata.category(c) == "So" and ord(c) > 0x2BFF) and c != "️"
    )


LIST_RE = re.compile(r"^(?P<prev>(?!\s*$)(?![-*+] )(?!\d+\. )(?!\s*\|).+)\n(?P<item>[-*+] |\d+\. )", re.M)
URL_RE = re.compile(r"(?<![(\[\"'>=])(https?://[^\s<>\"')\]]+)")


def preprocess(text: str) -> str:
    """Glaettet Markdown-Eigenheiten, die python-markdown anders liest als GitHub."""
    # GitHub laesst eine Liste einen Absatz unterbrechen, python-markdown nicht.
    prev = None
    while prev != text:
        prev = text
        text = LIST_RE.sub(lambda m: m.group("prev") + "\n\n" + m.group("item"), text)
    return text


def linkify(html: str) -> str:
    """Blanke URLs im Fliesstext anklickbar machen, Attribute unangetastet lassen."""
    out, pos = [], 0
    for tag in re.finditer(r"<[^>]+>", html):
        out.append(URL_RE.sub(r'<a href="\1">\1</a>', html[pos:tag.start()]))
        out.append(tag.group(0))
        pos = tag.end()
    out.append(URL_RE.sub(r'<a href="\1">\1</a>', html[pos:]))
    return "".join(out)


def convert(md_path: pathlib.Path, out_dir: pathlib.Path | None) -> pathlib.Path:
    raw = preprocess(clean(md_path.read_text(encoding="utf-8")))
    body = linkify(markdown.markdown(raw, extensions=["tables", "attr_list", "sane_lists"]))

    # Metazeilen des Kopfs und Quellenblock gesondert auszeichnen
    body = re.sub(
        r"(<h2[^>]*>[^<]*Quellennachweis.*)$",
        r'<div class="sources">\1</div>',
        body, flags=re.S,
    )
    html = (
        '<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">'
        f"<title>{md_path.stem}</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )

    target_dir = out_dir or md_path.parent
    target_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = target_dir / (md_path.stem + ".pdf")
    HTML(string=html, base_url=str(md_path.parent)).write_pdf(str(pdf_path))
    return pdf_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Briefing-Markdown nach PDF wandeln.")
    ap.add_argument("files", nargs="+", type=pathlib.Path)
    ap.add_argument("--out-dir", type=pathlib.Path, default=None)
    args = ap.parse_args()

    rc = 0
    for f in args.files:
        if not f.is_file():
            print(f"nicht gefunden: {f}", file=sys.stderr)
            rc = 1
            continue
        pdf = convert(f, args.out_dir)
        print(f"{f}  ->  {pdf}  ({pdf.stat().st_size // 1024} KB)")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
