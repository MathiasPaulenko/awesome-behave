"""Check that entries within each section of README.md are alphabetically ordered.

Entries are sorted by their link text (the name inside [Name](URL)),
ignoring leading articles ("The", "A", "An").

Exit code 1 if any section has out-of-order entries.
"""

import re
import sys
from pathlib import Path

ENTRY_PATTERN = re.compile(r"^- \[(.+?)\]\(.+?\)")
SECTION_HEADER_PATTERN = re.compile(r"^#{2,3} ")
LEADING_ARTICLES = {"the", "a", "an"}


def sort_key(name: str) -> str:
    words = name.split()
    while words and words[0].lower() in LEADING_ARTICLES:
        words.pop(0)
    return " ".join(words).lower()


def check_alphabetical(path: Path) -> list[str]:
    errors: list[str] = []
    current_section: str | None = None
    current_entries: list[tuple[int, str, str]] = []

    def flush_section() -> None:
        nonlocal current_entries
        if not current_section or not current_entries:
            current_entries = []
            return

        names = [(lineno, name, sort_key(name)) for lineno, name, _ in current_entries]
        sorted_names = sorted(names, key=lambda x: x[2])

        for (lineno, name, key), (_, sorted_name, sorted_key) in zip(names, sorted_names):
            if key != sorted_key:
                errors.append(
                    f"Line {lineno} ({current_section}): '{name}' is out of "
                    f"alphabetical order. Expected '{sorted_name}' at this position."
                )

        current_entries = []

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()

        if SECTION_HEADER_PATTERN.match(stripped):
            flush_section()
            current_section = stripped
            if current_section == "## Contents":
                current_section = None
            continue

        match = ENTRY_PATTERN.match(stripped)
        if match:
            current_entries.append((lineno, match.group(1), stripped))

    flush_section()
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <README.md>")
        return 1

    readme_path = Path(sys.argv[1])
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1

    errors = check_alphabetical(readme_path)

    if errors:
        print(f"\n{len(errors)} alphabetical order violation(s) found:\n")
        for err in errors:
            print(f"  - {err}\n")
        return 1

    print("All sections are in alphabetical order.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
