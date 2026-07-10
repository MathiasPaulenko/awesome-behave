"""Validate that README.md follows the awesome-list entry format.

Each list entry must match:
    - [Name](URL) - Short description ending with a period.

Exit code 1 if any violation is found.
"""

import re
import sys
from pathlib import Path

ENTRY_PATTERN = re.compile(
    r"^- \[.+?\]\(.+?\) - .+\.$"
)
BULLET_PATTERN = re.compile(r"^- ")


def validate_readme(path: Path) -> list[str]:
    errors: list[str] = []
    in_content_section = False
    current_section: str | None = None

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()

        if stripped.startswith("## ") and stripped != "## Contents":
            in_content_section = True
            current_section = stripped
            continue

        if not in_content_section:
            continue

        if stripped.startswith("### "):
            current_section = stripped
            continue

        if not BULLET_PATTERN.match(stripped):
            continue

        if stripped.startswith("- [") and "](#" in stripped:
            continue

        if stripped.startswith("- ["):
            if not ENTRY_PATTERN.match(stripped):
                errors.append(
                    f"Line {lineno} ({current_section}): entry does not match format "
                    f"'- [Name](URL) - Description.':\n  {stripped}"
                )
        elif stripped.startswith("- ["):
            errors.append(
                f"Line {lineno} ({current_section}): malformed entry:\n  {stripped}"
            )

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <README.md>")
        return 1

    readme_path = Path(sys.argv[1])
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1

    errors = validate_readme(readme_path)

    if errors:
        print(f"\n{len(errors)} format violation(s) found:\n")
        for err in errors:
            print(f"  - {err}\n")
        return 1

    print("All entries follow the awesome-list format.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
