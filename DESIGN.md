# DESIGN.md — awesome-behave

> Curated list of awesome resources, tools, libraries, and projects for [Behave](https://github.com/behave/behave) — BDD, Python style.

## 1. Project Overview

### 1.1 Goal

Create a curated, community-driven resource collection (awesome-list) for the **Behave** BDD framework for Python, following the style and quality standards of lists like [awesome-playwright](https://github.com/mxschmitt/awesome-playwright), [awesome-selenium](https://github.com/christian-bromann/awesome-selenium), and [awesome-bdd](https://github.com/omergulen/awesome-bdd).

### 1.2 Scope

This list focuses **exclusively on Behave** (not general BDD or other Python BDD frameworks like pytest-bdd or lettuce). It covers:

- Core Behave project and documentation
- Formatters and reporters
- Integrations (web frameworks, browser automation, API testing, mobile)
- Parallel execution tools
- CI/CD integrations
- IDE and editor support
- Learning resources (tutorials, courses, books, videos)
- Community projects and examples
- Related awesome lists

### 1.3 Target Audience

- QA engineers and SDETs using Python
- Python developers adopting BDD
- Teams migrating from Cucumber (Ruby/JS/Java) to Behave
- Engineering managers evaluating BDD tools for Python

## 2. Repository Structure

```
awesome-behave/
├── README.md           # The awesome list itself (main content)
├── DESIGN.md           # This file — project design and context
├── CONTRIBUTING.md     # Guidelines for contributors
├── CODE_OF_CONDUCT.md  # Community code of conduct
└── LICENSE             # MIT license (or CC-BY-SA for content)
```

### 2.1 README.md Structure

The README will follow the standard awesome-list format:

```markdown
# Awesome Behave

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome resources, tools, libraries, and projects for
> [Behave](https://github.com/behave/behave) — BDD, Python style.

## Contents

- [Official Resources](#official-resources)
- [Formatters & Reporters](#formatters--reporters)
- [Integrations](#integrations)
  - [Web Frameworks](#web-frameworks)
  - [Browser Automation](#browser-automation)
  - [API Testing](#api-testing)
  - [Mobile Testing](#mobile-testing)
  - [Visual Testing](#visual-testing)
- [Parallel Execution](#parallel-execution)
- [CI/CD Integrations](#cicd-integrations)
- [IDE & Editor Support](#ide--editor-support)
- [Learning Resources](#learning-resources)
  - [Tutorials & Guides](#tutorials--guides)
  - [Courses](#courses)
  - [Books](#books)
  - [Videos](#videos)
- [Community Projects & Examples](#community-projects--examples)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)
```

## 3. Content Plan

### 3.1 Official Resources

| Resource | URL | Description |
|---|---|---|
| Behave GitHub | https://github.com/behave/behave | Main repository |
| Behave Docs | https://behave.readthedocs.io/ | Official documentation |
| Behave Examples | https://behave.github.io/behave.example/ | Tutorials and examples |
| Behave Organization | https://github.com/behave | GitHub org (behave, behave-django, behave.example) |
| PyPI | https://pypi.org/project/behave/ | Package on PyPI |
| Behave Ecosystem Docs | https://behave.readthedocs.io/en/stable/appendix.behave_ecosystem/ | Official ecosystem page |

### 3.2 Formatters & Reporters

#### Built-in Formatters

Behave includes: `json`, `json.pretty`, `plain`, `pretty`, `progress`, `progress2`, `progress3`, `rerun`, `sphinx.steps`, `steps`, `steps.bad`, `steps.catalog`, `steps.code`, `steps.doc`, `steps.usage`, `tags`, `tags.location`.

Built-in reporters: `junit` (JUnit XML), `summary`.

#### Contributed Formatters

| Name | PyPI | GitHub | Description |
|---|---|---|---|
| allure-behave | `allure-behave` | https://github.com/allure-framework/allure-python/tree/master/allure-behave | Allure framework adapter for Behave |
| behave-html-formatter | `behave-html-formatter` | https://github.com/behave-contrib/behave-html-formatter | Simple HTML formatter |
| behave-html-pretty-formatter | `behave-html-pretty-formatter` | https://github.com/behave-contrib/behave-html-pretty-formatter | Pretty HTML formatter inspired by jest-html-reporter |
| behave-teamcity | `behave-teamcity` | https://github.com/iljabauer/behave-teamcity | TeamCity CI formatter |
| behave-cucumber-formatter | `behave-cucumber-formatter` | https://pypi.org/project/behave-cucumber-formatter/ | Cucumber JSON formatter for Xray/pipeline integration |
| behave-modern-json-report | `behave-modern-json-report` | https://pypi.org/project/behave-modern-json-report/ | Modern structured JSON report + Cucumber JSON output |

### 3.3 Integrations

#### Web Frameworks

| Name | PyPI | GitHub | Description |
|---|---|---|---|
| behave-django | `behave-django` | https://github.com/behave/behave-django | Official Django integration for Behave |
| Flask integration | — | https://behave.readthedocs.io/en/stable/usecase_flask/ | Official Flask test integration guide |

#### Browser Automation

| Name | PyPI / URL | Description |
|---|---|---|
| Selenium + Behave | — | Common integration pattern; see community projects |
| Playwright + Behave | — | Growing pattern; Behave step definitions wrapping Playwright |
| Appium + Behave | — | Mobile automation with Behave |

#### API Testing

| Name | PyPI | GitHub | Description |
|---|---|---|---|
| behave-restful | `behave-restful` | https://github.com/behave-restful/behave-restful | BDD framework for REST API testing on top of Behave |
| Requests + Behave | — | Common pattern using `requests` library in step definitions |

#### Mobile Testing

| Name | GitHub | Description |
|---|---|---|
| appium-python-bdd | https://github.com/serhatbolsu/appium-python-bdd | Behave + Appium examples |
| LambdaTest Behave + Appium | https://github.com/topics/bdd-framework?l=python | Cloud-based parallel Behave + Appium |

#### Visual Testing

| Name | GitHub | Description |
|---|---|---|
| Applitools + Behave | https://github.com/umangbhatia786/Applitools-With-Behave | Visual testing with Applitools + Selenium + Behave |

### 3.4 Parallel Execution

| Name | PyPI | GitHub | Description |
|---|---|---|---|
| BehaveX | `behavex` | https://github.com/hrcorval/behavex | Production-grade parallel execution wrapper with enterprise reporting |
| behave-parallel | — | https://github.com/hugeinc/behave-parallel | Parallel execution by feature or scenario |

### 3.5 CI/CD Integrations

| Platform | Approach | Reference |
|---|---|---|
| GitHub Actions | Native `behave` command in workflow | https://deepwiki.com/behave/behave/6.2-cicd-pipeline |
| GitLab CI | Behave + pytest in pipeline | https://surestride.hashnode.dev/cicd-pipeline-for-python-with-bdd-and-tdd-using-behave-pytest-and-gitlab-ci |
| Jenkins | JUnit XML reporter + plugin | Built-in `junit` reporter |
| TeamCity | `behave-teamcity` formatter | https://github.com/iljabauer/behave-teamcity |
| ParallelBehaveAllureFlow | Reusable GitHub Actions workflow | https://github.com/ggkiokas/ParallelBehaveAllureFlow |
| Tox | Multi-environment testing | https://tox.wiki |

### 3.6 IDE & Editor Support

#### IDE Plugins

| IDE | Plugin | Description |
|---|---|---|
| PyCharm (Professional) | Built-in BDD support | Native Behave + Gherkin support since v4 |
| PyCharm / IntelliJ IDEA | Gherkin plugin | Gherkin syntax highlighting and step navigation |
| VS Code | Cucumber Official extension | Gherkin + Behave support |
| Eclipse | Cucumber-Eclipse | Gherkin editor support |
| Visual Studio | cuke4vs | Gherkin editor support |

#### Editor Plugins

| Editor | Plugin | Description |
|---|---|---|
| Vim | vim-behave | Port of vim-cucumber to Python Behave |
| Sublime Text | Cucumber (ST Bundle) | Gherkin editor support, table formatting |
| Sublime Text | Behave Step Finder | Navigate to steps in Behave |
| Notepad++ | NP++ gherkin | Gherkin syntax highlighting |
| Online | Gherkin Editor | Web-based `.feature` file editor |

### 3.7 Learning Resources

#### Tutorials & Guides

| Resource | URL | Description |
|---|---|---|
| Official Tutorial | https://behave.readthedocs.io/en/stable/tutorial/ | Getting started guide |
| Behave Examples & Tutorials | https://behave.github.io/behave.example/ | 12 progressive tutorials |
| QASkills Behave Tutorial | https://qaskills.sh/blog/behave-python-bdd-complete-tutorial | Complete 2026 hands-on tutorial |
| Behave Ecosystem | https://behave.readthedocs.io/en/stable/appendix.behave_ecosystem/ | Official ecosystem listing |

#### Courses

| Course | Platform | Description |
|---|---|---|
| BDD with Behave and Python | Pluralsight | Full course: Gherkin, Behave, Selenium integration, CI |
| Cucumber BDD with Python Behave and Selenium WebDriver | Udemy | 19h course: BDD framework, Selenium, API testing, MySQL |
| BDD Automation: Behave with Python | Udemy | Behave + Selenium + Appium |

#### Books

(To be populated — books covering Python BDD with Behave)

#### Videos

(To be populated — YouTube talks, conference presentations)

### 3.8 Community Projects & Examples

| Project | GitHub | Description |
|---|---|---|
| Python_Selenium_BDD_Framework | https://github.com/DipankarDandapat/Python_Selenium_BDD_Framework | Selenium + Requests + BehaveX framework |
| Python_Behave_Selenium_BDD | https://github.com/soumyaevan/Python_Behave_Selenium_BDD | BDD automation with Selenium + Behave |
| behavedemo | https://github.com/andrewdjackson/behavedemo | Demo with pyHamcrest, Requests, Selenium |
| Python-Behave-sample-project | https://github.com/crki76/Python-Behave-sample-project | Sample project with POM pattern |
| try-behave | https://github.com/behave-contrib/try-behave | Try Behave in the browser via Pyodide |
| behave-gui | https://github.com/behave-contrib/behave-gui | GUI front-end for Behave |

### 3.9 Related Awesome Lists

| List | URL | Description |
|---|---|---|
| Awesome BDD | https://github.com/omergulen/awesome-bdd | General BDD ecosystem resources |
| Awesome Python Testing | https://github.com/cleder/awesome-python-testing | Python testing resources |
| Awesome Python | https://github.com/vinta/awesome-python | General Python awesome list |
| Awesome Playwright | https://github.com/mxschmitt/awesome-playwright | Playwright resources |
| Awesome Selenium | https://github.com/christian-bromann/awesome-selenium | Selenium resources |

## 4. Formatting Rules

### 4.1 Entry Format

Each entry in the README follows this format:

```markdown
- [Name](URL) - Short description (one line, ending with period).
```

Rules:
- Alphabetical order within each section
- Use the project's PyPI name or GitHub repo name as the link text
- Descriptions must be concise (max ~100 characters)
- No marketing language — factual descriptions only
- Prefer linking to GitHub repos over PyPI pages (unless PyPI is the primary source)
- Mark archived or unmaintained projects with `(archived)` or `(unmaintained)`

### 4.2 Section Headers

- Use `##` for top-level sections
- Use `###` for subsections
- Every section must have a `## Contents` anchor entry at the top

### 4.3 Badge

Include the official awesome badge at the top:

```markdown
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
```

## 5. Contribution Guidelines

### 5.1 How to Contribute

1. Fork the repository
2. Add your resource to the appropriate section in `README.md`
3. Ensure alphabetical order within the section
4. Follow the entry format (see Section 4.1)
5. Open a pull request with a clear title

### 5.2 Acceptance Criteria

- The resource must be directly related to Behave (not general BDD or other frameworks)
- The resource must be publicly accessible
- The resource must have a stable URL (GitHub repo, PyPI page, documentation site)
- The description must be accurate and concise
- No self-promotion of commercial products without open-source components

### 5.3 Review Process

- Maintainers review PRs within 7 days
- Resources are verified for relevance and accessibility
- Entries may be reorganized for better categorization

## 6. Maintenance Plan

### 6.1 Regular Checks

- Quarterly review of all links (check for dead URLs, archived repos)
- Verify PyPI packages are still installable
- Update descriptions if project scope has changed
- Remove resources that have been unmaintained for 2+ years (unless still widely used)

### 6.2 Discovery

- Monitor GitHub topics: `behave`, `bdd-framework` (filtered by Python)
- Monitor PyPI search for `behave`
- Watch the behave-contrib GitHub organization
- Community submissions via PRs and issues

## 7. License

The list content will be licensed under **CC-BY-SA 4.0** (Creative Commons Attribution-ShareAlike), consistent with most awesome-lists. Code snippets, if any, will be under MIT.

## 8. Success Metrics

- Number of contributors
- Number of resources listed
- GitHub stars (indicates community value)
- Frequency of updates (active maintenance)
- Inclusion in [awesome.re](https://awesome.re) curated list
