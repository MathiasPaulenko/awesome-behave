"""Generate a static, searchable HTML site from README.md.

Parses the awesome-list markdown and produces a single-page HTML with:
- Live search/filter by name or description
- Category sidebar navigation
- Resource count per section
- Dark/light theme toggle

Usage: python scripts/generate_site.py README.md --output site/index.html
"""

import re
import sys
import html
from pathlib import Path
from datetime import datetime

ENTRY_PATTERN = re.compile(r"^- \[(.+?)\]\((.+?)\) - (.+)$")
SECTION_PATTERN = re.compile(r"^(#{2,3})\s+(.+)$")
BOLD_TEXT_PATTERN = re.compile(r"\*(.+?)\*")

TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Awesome Behave</title>
<meta name="description" content="A curated list of awesome resources, tools, libraries, and projects for Behave — BDD, Python style.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐍</text></svg>">
<style>
:root {{
  --bg: #0d1117;
  --bg-card: #161b22;
  --bg-hover: #1c2128;
  --border: #30363d;
  --text: #e6edf3;
  --text-muted: #8b949e;
  --accent: #58a6ff;
  --accent-bg: rgba(88, 166, 255, 0.1);
  --sidebar-bg: #161b22;
  --search-bg: #0d1117;
}}
[data-theme="light"] {{
  --bg: #ffffff;
  --bg-card: #f6f8fa;
  --bg-hover: #eaeef2;
  --border: #d0d7de;
  --text: #1f2328;
  --text-muted: #656d76;
  --accent: #0969da;
  --accent-bg: rgba(9, 105, 218, 0.1);
  --sidebar-bg: #f6f8fa;
  --search-bg: #ffffff;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
}}
.layout {{ display: flex; min-height: 100vh; }}
.sidebar {{
  width: 280px;
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border);
  padding: 24px 16px;
  position: sticky;
  top: 0;
  height: 100vh;
  overflow-y: auto;
  flex-shrink: 0;
}}
.sidebar h2 {{ font-size: 1.1rem; margin-bottom: 16px; }}
.sidebar nav a {{
  display: block;
  padding: 6px 12px;
  color: var(--text-muted);
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: all 0.15s;
}}
.sidebar nav a:hover {{ color: var(--accent); background: var(--accent-bg); }}
.sidebar nav a .count {{ float: right; opacity: 0.6; font-size: 0.8rem; }}
.main {{ flex: 1; padding: 40px; max-width: 900px; }}
.header {{ margin-bottom: 32px; }}
.header h1 {{ font-size: 2rem; margin-bottom: 8px; }}
.header p {{ color: var(--text-muted); }}
.badges {{ margin-bottom: 16px; }}
.badges img {{ margin-right: 4px; }}
.search-bar {{
  position: sticky;
  top: 0;
  background: var(--bg);
  padding: 16px 0;
  z-index: 10;
  margin-bottom: 24px;
}}
.search-bar input {{
  width: 100%;
  padding: 12px 16px;
  font-size: 1rem;
  background: var(--search-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  outline: none;
  transition: border-color 0.15s;
}}
.search-bar input:focus {{ border-color: var(--accent); }}
.theme-toggle {{
  position: fixed;
  top: 16px;
  right: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 12px;
  cursor: pointer;
  font-size: 1.2rem;
  z-index: 100;
}}
.section {{ margin-bottom: 40px; }}
.section h2 {{
  font-size: 1.5rem;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}}
.section h3 {{
  font-size: 1.1rem;
  margin: 24px 0 12px;
  color: var(--text-muted);
}}
.entry {{
  display: block;
  padding: 12px 16px;
  margin-bottom: 8px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 8px;
  text-decoration: none;
  color: var(--text);
  transition: all 0.15s;
}}
.entry:hover {{
  background: var(--bg-hover);
  border-color: var(--accent);
  transform: translateX(2px);
}}
.entry strong {{ color: var(--accent); }}
.entry .desc {{ color: var(--text-muted); font-size: 0.9rem; }}
.no-results {{
  text-align: center;
  padding: 40px;
  color: var(--text-muted);
  display: none;
}}
.footer {{
  margin-top: 48px;
  padding-top: 24px;
  border-top: 1px solid var(--border);
  color: var(--text-muted);
  font-size: 0.85rem;
}}
@media (max-width: 768px) {{
  .layout {{ flex-direction: column; }}
  .sidebar {{ width: 100%; height: auto; position: relative; }}
  .main {{ padding: 20px; }}
}}
</style>
</head>
<body>
<div class="theme-toggle" onclick="toggleTheme()">🌙</div>
<div class="layout">
  <aside class="sidebar">
    <h2>📂 Sections</h2>
    <nav id="nav">
{nav_links}
    </nav>
  </aside>
  <main class="main">
    <div class="header">
      <div class="badges">
        <img src="https://awesome.re/badge.svg" alt="Awesome">
        <img src="https://img.shields.io/badge/resources-{total}-blue" alt="Resources">
        <img src="https://img.shields.io/badge/license-CC--BY--SA%204.0-green" alt="License">
      </div>
      <h1>Awesome Behave</h1>
      <p>A curated list of awesome resources, tools, libraries, and projects for <a href="https://github.com/behave/behave">Behave</a> — BDD, Python style.</p>
    </div>
    <div class="search-bar">
      <input type="text" id="search" placeholder="Search resources..." oninput="filterEntries()">
    </div>
    <div class="no-results" id="noResults">No resources found matching your search.</div>
{sections}
    <div class="footer">
      <p>Generated from <a href="https://github.com/MathiasPaulenko/awesome-behave/blob/main/README.md">README.md</a> on {date}</p>
      <p>Contributions welcome — see <a href="https://github.com/MathiasPaulenko/awesome-behave/blob/main/CONTRIBUTING.md">contributing guidelines</a>.</p>
    </div>
  </main>
</div>
<script>
function toggleTheme() {{
  const html = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  if (html.dataset.theme === 'dark') {{
    html.dataset.theme = 'light';
    toggle.textContent = '☀️';
    localStorage.setItem('theme', 'light');
  }} else {{
    html.dataset.theme = 'dark';
    toggle.textContent = '🌙';
    localStorage.setItem('theme', 'dark');
  }}
}}
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {{
  document.documentElement.dataset.theme = 'light';
  document.querySelector('.theme-toggle').textContent = '☀️';
}}
function filterEntries() {{
  const query = document.getElementById('search').value.toLowerCase();
  const entries = document.querySelectorAll('.entry');
  let visible = 0;
  entries.forEach(e => {{
    const text = e.textContent.toLowerCase();
    if (text.includes(query)) {{
      e.style.display = '';
      visible++;
    }} else {{
      e.style.display = 'none';
    }}
  }});
  document.getElementById('noResults').style.display = visible === 0 ? 'block' : 'none';
  document.querySelectorAll('.section').forEach(s => {{
    const visibleEntries = s.querySelectorAll('.entry:not([style*="display: none"])');
    s.style.display = visibleEntries.length === 0 ? 'none' : '';
  }});
}}
</script>
</body>
</html>
"""


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text)
    return text


def parse_readme(path: Path) -> tuple[list[tuple[str, str, int]], list[tuple[str, str, list[tuple[str, str, str]]]]]:
    """Parse README.md into sections and entries."""
    nav_items = []
    sections = []
    current_section = None
    current_subsection = None
    current_entries = []

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        section_match = SECTION_PATTERN.match(stripped)
        if section_match:
            if current_section:
                if current_subsection:
                    current_entries.append(("subsection_end", current_subsection, ""))
                sections.append((current_section, current_entries))

            level = len(section_match.group(1))
            title = section_match.group(2).strip()

            if title == "Contents":
                current_section = None
                continue

            current_section = title
            current_subsection = None
            current_entries = []
            continue

        entry_match = ENTRY_PATTERN.match(stripped)
        if entry_match and current_section:
            name, url, desc = entry_match.groups()
            desc = BOLD_TEXT_PATTERN.sub(r"<em>\1</em>", html.escape(desc))
            current_entries.append(("entry", html.escape(name), html.escape(url), desc))
            continue

        if stripped.startswith("### ") and current_section:
            if current_subsection:
                current_entries.append(("subsection_end", current_subsection, ""))
            sub = stripped.lstrip("# ").strip()
            current_subsection = sub
            current_entries.append(("subsection_start", sub, slugify(sub)))

    if current_section:
        if current_subsection:
            current_entries.append(("subsection_end", current_subsection, ""))
        sections.append((current_section, current_entries))

    for title, entries in sections:
        count = sum(1 for e in entries if e[0] == "entry")
        if count > 0:
            nav_items.append((title, slugify(title), count))

    return nav_items, sections


def generate_site(readme_path: Path) -> str:
    nav_items, sections = parse_readme(readme_path)

    total = sum(count for _, _, count in nav_items)

    nav_links = []
    for title, slug, count in nav_items:
        nav_links.append(f'      <a href="#{slug}">{html.escape(title)} <span class="count">{count}</span></a>')
    nav_html = "\n".join(nav_links)

    sections_html = []
    for title, entries in sections:
        slug = slugify(title)
        count = sum(1 for e in entries if e[0] == "entry")
        if count == 0:
            continue

        sections_html.append(f'    <div class="section" id="{slug}">')
        sections_html.append(f'      <h2>{html.escape(title)}</h2>')

        for entry in entries:
            if entry[0] == "subsection_start":
                sections_html.append(f'      <h3 id="{entry[2]}">{html.escape(entry[1])}</h3>')
            elif entry[0] == "subsection_end":
                continue
            elif entry[0] == "entry":
                _, name, url, desc = entry
                sections_html.append(
                    f'      <a class="entry" href="{url}" target="_blank" rel="noopener">'
                    f'<strong>{name}</strong> <span class="desc">— {desc}</span></a>'
                )

        sections_html.append("    </div>")

    return TEMPLATE.format(
        nav_links="\n".join(nav_links),
        total=total,
        sections="\n".join(sections_html),
        date=datetime.now().strftime("%Y-%m-%d"),
    )


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <README.md> [--output site/index.html]")
        return 1

    readme_path = Path(sys.argv[1])
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1

    output = generate_site(readme_path)

    out_path = Path("site/index.html")
    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            out_path = Path(sys.argv[idx + 1])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
    print(f"Site generated at {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
