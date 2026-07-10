# Contributing to Awesome Behave

First off, thanks for taking the time to contribute! This list thrives on community contributions.

## How to Contribute

1. **Fork** the repository.
2. **Add** your resource to the appropriate section in `README.md`.
3. **Ensure** alphabetical order within the section.
4. **Follow** the entry format (see below).
5. **Open** a pull request with a clear, descriptive title.

## Entry Format

Each entry must follow this format:

```markdown
- [Name](URL) - Short description ending with a period.
```

### Rules

- **Alphabetical order** within each section (ignore leading articles like "The").
- **Link text**: use the project's GitHub repo name or PyPI package name.
- **Description**: concise, factual, max ~100 characters. No marketing language.
- **URLs**: prefer GitHub repos over PyPI pages. Use PyPI only if there is no GitHub repo.
- **Archived projects**: append `(archived)` to the description.
- **Unmaintained projects**: append `(unmaintained)` if no commits in 2+ years.

### Example

```markdown
- [behave-html-formatter](https://github.com/behave-contrib/behave-html-formatter) - Simple HTML formatter for Behave test reports.
```

## Acceptance Criteria

- The resource must be **directly related to Behave** (not general BDD or other frameworks like pytest-bdd or lettuce).
- The resource must be **publicly accessible**.
- The resource must have a **stable URL** (GitHub repo, PyPI page, documentation site).
- The description must be **accurate and concise**.
- No **self-promotion** of commercial products without open-source components.

## Adding a New Section

If you believe a new section is needed:

1. Open an issue first to discuss it with maintainers.
2. If approved, add the section to both the **Contents** list and the body of `README.md`.
3. Follow the same formatting rules.

## Pull Request Process

1. Maintainers review PRs within **7 days**.
2. Resources are verified for relevance and accessibility.
3. Entries may be reorganized for better categorization.
4. Once approved, the PR is merged.

## Reporting Issues

- **Dead links**: open an issue with the section and broken URL.
- **Missing resources**: open an issue with the resource name, URL, and suggested section.
- **Categorization suggestions**: open an issue describing the proposed reorganization.

## Maintenance

Maintainers perform quarterly reviews to:

- Check for dead URLs and archived repositories.
- Verify PyPI packages are still installable.
- Remove resources unmaintained for 2+ years (unless still widely used).
- Update descriptions if project scope has changed.
