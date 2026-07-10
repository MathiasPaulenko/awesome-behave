"""Generate stats summary for the awesome-behave list.

Outputs a markdown summary with:
- Total number of resources
- Resources per section
- Resources per type (GitHub, PyPI, other)

Usage: python scripts/generate_stats.py README.md [--output stats.md]
"""

import re
import sys
from pathlib import Path
from collections import Counter

ENTRY_PATTERN = re.compile(r"^- \[.+?\]\((.+?)\)")
SECTION_PATTERN = re.compile(r"^#{2,3} ")
GITHUB_PATTERN = re.compile(r"https://github\.com/")
PYPI_PATTERN = re.compile(r"https://pypi\.org/")


def generate_stats(path: Path) -> dict:
    stats = {
        "total": 0,
        "sections": {},
        "by_type": Counter(),
    }
    current_section = None

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if SECTION_PATTERN.match(stripped):
            if stripped == "## Contents":
                current_section = None
                continue
            current_section = stripped.lstrip("# ").strip()
            stats["sections"][current_section] = 0
            continue

        if current_section is None:
            continue

        match = ENTRY_PATTERN.match(stripped)
        if match:
            url = match.group(1)
            stats["total"] += 1
            stats["sections"][current_section] = stats["sections"].get(current_section, 0) + 1

            if GITHUB_PATTERN.match(url):
                stats["by_type"]["GitHub"] += 1
            elif PYPI_PATTERN.match(url):
                stats["by_type"]["PyPI"] += 1
            else:
                stats["by_type"]["Other"] += 1

    return stats


def format_stats(stats: dict) -> str:
    lines = [
        "# Awesome Behave — Stats\n",
        f"**Total resources:** {stats['total']}\n",
        "## By Section\n",
        "| Section | Resources |",
        "| --- | --- |",
    ]

    for section, count in sorted(stats["sections"].items(), key=lambda x: -x[1]):
        if count > 0:
            lines.append(f"| {section} | {count} |")

    lines.extend([
        "",
        "## By Type",
        "",
        "| Type | Resources |",
        "| --- | --- |",
    ])

    for type_name, count in sorted(stats["by_type"].items(), key=lambda x: -x[1]):
        lines.append(f"| {type_name} | {count} |")

    return "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <README.md> [--output stats.md]")
        return 1

    readme_path = Path(sys.argv[1])
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1

    stats = generate_stats(readme_path)
    output = format_stats(stats)

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            Path(sys.argv[idx + 1]).write_text(output, encoding="utf-8")
            print(f"Stats written to {sys.argv[idx + 1]}")
            return 0

    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
