"""Builds app.html from app.src.html: inlines the SVG icon sprite and expands #I:name# / #I:name:class# markers.
Run: python build.py"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
src = (HERE / "app.src.html").read_text(encoding="utf-8")
sprite = (HERE / "icons.svg.html").read_text(encoding="utf-8")


def icon(m):
    name, cls = m.group(1), m.group(2)
    return f'<svg class="ico{" " + cls if cls else ""}" aria-hidden="true"><use href="#i-{name}"/></svg>'


out = src.replace("<!--ICONS-->", sprite)
out = re.sub(r"#I:([a-z-]+)(?::([a-z0-9-]+))?#", icon, out)
(HERE / "app.html").write_text(out, encoding="utf-8")
print("built app.html", len(out) // 1024, "KB")
