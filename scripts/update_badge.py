"""Update the resources badge in README.md with the current resource count.

Usage: python scripts/update_badge.py README.md
"""

import re
import sys
from pathlib import Path
from generate_stats import generate_stats


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <README.md>")
        return 1

    readme_path = Path(sys.argv[1])
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1

    stats = generate_stats(readme_path)
    total = stats["total"]

    content = readme_path.read_text(encoding="utf-8")
    updated = re.sub(
        r"badge/resources-\d+-blue",
        f"badge/resources-{total}-blue",
        content,
    )

    if content == updated:
        print(f"Badge already up to date ({total} resources)")
        return 0

    readme_path.write_text(updated, encoding="utf-8")
    print(f"Badge updated to {total} resources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
