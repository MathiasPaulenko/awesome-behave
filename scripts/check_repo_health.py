"""Check health of all resources listed in README.md.

Verifies:
- GitHub repos are not archived
- GitHub repo URLs are accessible
- PyPI package URLs are accessible

Outputs a markdown report to health-report.md if any issues are found.
Exit code 0 always (issues are reported, not fatal).
"""

import re
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

GITHUB_REPO_PATTERN = re.compile(r"https://github\.com/([^/]+/[^/)\s]+)")
PYPI_PATTERN = re.compile(r"https://pypi\.org/project/([^/)\s]+)/")


def extract_urls(path: Path) -> list[tuple[int, str, str]]:
    """Extract all GitHub and PyPI URLs from README.md with line numbers."""
    urls = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for match in GITHUB_REPO_PATTERN.finditer(line):
            repo = match.group(1).rstrip("/")
            urls.append((lineno, f"https://github.com/{repo}", "github"))
        for match in PYPI_PATTERN.finditer(line):
            pkg = match.group(1).rstrip("/")
            urls.append((lineno, f"https://pypi.org/project/{pkg}/", "pypi"))
    return urls


def check_github_repo(repo: str) -> tuple[bool, str]:
    """Check if a GitHub repo is archived or inaccessible via API."""
    api_url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(api_url, headers={
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "awesome-behave-health-check",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
            if data.get("archived", False):
                return False, "Repository is archived"
            return True, "OK"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "Repository not found (404)"
        if e.code == 403:
            return True, "Rate limited (skipping)"
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, f"Error: {e}"


def check_pypi_package(pkg: str) -> tuple[bool, str]:
    """Check if a PyPI package page is accessible."""
    url = f"https://pypi.org/pypi/{pkg}/json"
    req = urllib.request.Request(url, headers={
        "User-Agent": "awesome-behave-health-check",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return True, "OK"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "Package not found on PyPI (404)"
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, f"Error: {e}"


def main() -> int:
    readme_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
    if not readme_path.exists():
        print(f"Error: {readme_path} not found")
        return 1

    urls = extract_urls(readme_path)
    seen: set[str] = set()
    issues: list[str] = []

    print(f"Checking {len(urls)} URLs...")
    for lineno, url, url_type in urls:
        if url in seen:
            continue
        seen.add(url)

        if url_type == "github":
            repo = url.replace("https://github.com/", "")
            ok, msg = check_github_repo(repo)
        else:
            pkg = url.replace("https://pypi.org/project/", "").rstrip("/")
            ok, msg = check_pypi_package(pkg)

        status = "OK" if ok else "FAIL"
        print(f"  [{status}] Line {lineno}: {url} - {msg}")

        if not ok:
            issues.append(f"- Line {lineno}: [{url}]({url}) - {msg}")

    if issues:
        report_path = Path("health-report.md")
        report_path.write_text(
            "# Resource Health Check Report\n\n"
            f"Found **{len(issues)}** issue(s):\n\n"
            + "\n".join(issues)
            + "\n\n---\n"
            "This report was generated automatically by the `Resource Health Check` workflow.\n",
            encoding="utf-8",
        )
        print(f"\n{len(issues)} issue(s) found. Report written to health-report.md")
    else:
        print("\nAll resources are healthy.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
