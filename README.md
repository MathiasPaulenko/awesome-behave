# Awesome Behave

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![CI](https://github.com/MathiasPaulenko/awesome-behave/actions/workflows/ci.yml/badge.svg)](https://github.com/MathiasPaulenko/awesome-behave/actions/workflows/ci.yml)
[![Last Commit](https://img.shields.io/github/last-commit/MathiasPaulenko/awesome-behave)](https://github.com/MathiasPaulenko/awesome-behave)
[![Resources](https://img.shields.io/badge/resources-66-blue)](https://github.com/MathiasPaulenko/awesome-behave)
[![Contributors](https://img.shields.io/github/contributors/MathiasPaulenko/awesome-behave)](https://github.com/MathiasPaulenko/awesome-behave/graphs/contributors)
[![License](https://img.shields.io/badge/license-CC--BY--SA%204.0-green)](LICENSE)
[![Stars](https://img.shields.io/github/stars/MathiasPaulenko/awesome-behave?style=social)](https://github.com/MathiasPaulenko/awesome-behave)

> A curated list of awesome resources, tools, libraries, and projects for
> [Behave](https://github.com/behave/behave) — BDD, Python style.

[Behave](https://github.com/behave/behave) is behavior-driven development (BDD), Python style. It uses tests written in a natural language style (Gherkin), backed up by Python code.

---

## Contents

- [Official Resources](#official-resources)
- [Formatters & Reporters](#formatters--reporters)
  - [Built-in](#built-in)
  - [Contributed](#contributed)
- [Integrations](#integrations)
  - [Web Frameworks](#web-frameworks)
  - [Browser Automation](#browser-automation)
  - [API Testing](#api-testing)
  - [Mobile Testing](#mobile-testing)
  - [Visual Testing](#visual-testing)
- [Parallel Execution](#parallel-execution)
- [Tooling](#tooling)
- [CI/CD Integrations](#cicd-integrations)
- [IDE & Editor Support](#ide--editor-support)
  - [IDE Plugins](#ide-plugins)
  - [Editor Plugins](#editor-plugins)
- [Learning Resources](#learning-resources)
  - [Tutorials & Guides](#tutorials--guides)
  - [Courses](#courses)
  - [Books](#books)
  - [Videos](#videos)
- [Community Projects & Examples](#community-projects--examples)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

---

## Official Resources

- [Behave](https://github.com/behave/behave) - Main repository. BDD, Python style.
- [Behave Documentation](https://behave.readthedocs.io/) - Official documentation and tutorial.
- [Behave Ecosystem](https://behave.readthedocs.io/en/stable/appendix.behave_ecosystem/) - Official listing of ecosystem tools, IDE plugins, and editor support.
- [Behave Examples & Tutorials](https://behave.github.io/behave.example/) - Progressive tutorials from first steps to advanced features.
- [Behave on PyPI](https://pypi.org/project/behave/) - Official PyPI package page.
- [Behave Organization](https://github.com/behave) - GitHub organization hosting behave, behave-django, and behave.example.
- [Formatters & Reporters Reference](https://behave.readthedocs.io/en/stable/appendix.formatters/) - Official documentation of built-in and contributed formatters.

## Formatters & Reporters

### Built-in

Behave ships with the following formatters: `json`, `json.pretty`, `plain`, `pretty`, `progress`, `progress2`, `progress3`, `rerun`, `sphinx.steps`, `steps`, `steps.bad`, `steps.catalog`, `steps.code`, `steps.doc`, `steps.usage`, `tags`, `tags.location`.

Built-in reporters: `junit` (JUnit XML output), `summary` (test run summary).

See the [official formatter docs](https://behave.readthedocs.io/en/stable/appendix.formatters/) for full details.

### Contributed

- [allure-behave](https://github.com/allure-framework/allure-python/tree/master/allure-behave) - Allure framework adapter for Behave. Generates rich HTML test reports with attachments, metadata, and test hierarchies.
- [behave-cucumber-formatter](https://pypi.org/project/behave-cucumber-formatter/) - Cucumber JSON formatter for pipeline integration with Xray and other Cucumber-compatible tools.
- [behave-html-formatter](https://github.com/behave-contrib/behave-html-formatter) - Simple HTML formatter for Behave test reports.
- [behave-html-pretty-formatter](https://github.com/behave-contrib/behave-html-pretty-formatter) - Pretty HTML formatter inspired by jest-html-reporter. Supports embedded screenshots, pseudo steps, and configurable summaries.
- [behave-modern-console-report](https://github.com/MathiasPaulenko/behave-modern-console-report) - Real-time console report formatter with colors, progress indicators, and execution summaries for local development and CI/CD.
- [behave-modern-html-report](https://github.com/MathiasPaulenko/behave-modern-html-report) - Modern interactive HTML report formatter with zero external dependencies.
- [behave-modern-json-report](https://github.com/MathiasPaulenko/behave-modern-json-report) - Modern structured JSON report formatter with schema-versioned output and Cucumber JSON compatibility for CI/CD integrations.
- [behave-modern-md-report](https://github.com/MathiasPaulenko/behave-modern-md-report) - Markdown report formatter that generates GitHub-friendly execution reports with summaries and statistics.
- [behave-teamcity](https://github.com/iljabauer/behave-teamcity) - Formatter for reporting Behave test results to JetBrains TeamCity CI via service messages.

## Integrations

### Web Frameworks

- [behave-django](https://github.com/behave/behave-django) - Official Django integration for Behave. Provides a `behave` management command and test runner integration.
- [Flask Test Integration](https://behave.readthedocs.io/en/stable/usecase_flask/) - Official guide for integrating Behave with Flask applications.

### Browser Automation

- [Playwright + Behave](https://qaskills.sh/blog/behave-python-bdd-complete-tutorial) - Growing pattern of wrapping Playwright Python in Behave step definitions for modern browser automation.
- [Selenium + Behave](https://github.com/soumyaevan/Python_Behave_Selenium_BDD) - Common integration pattern using Selenium WebDriver with Behave step definitions.

### API Testing

- [behave-restful](https://github.com/behave-restful/behave-restful) - BDD framework for testing REST APIs on top of Behave. Provides Gherkin language extensions for HTTP requests and response validation.
- [Requests + Behave](https://github.com/andrewdjackson/behavedemo) - Pattern using the `requests` library within Behave step definitions for API testing.

### Mobile Testing

- [appium-python-bdd](https://github.com/serhatbolsu/appium-python-bdd) - BDD test examples with Appium and Behave for mobile automation.
- [LambdaTest Behave + Appium](https://www.lambdatest.com/support/docs/behave-tutorial/) - Run Behave and Appium tests on LambdaTest cloud devices.

### Visual Testing

- [Applitools + Behave](https://github.com/umangbhatia786/Applitools-With-Behave) - Visual regression testing with Applitools, Selenium, and Behave.

## Parallel Execution

- [behave-parallel](https://github.com/hugeinc/behave-parallel) - Parallel execution support for Behave by feature or scenario using multiprocessing.
- [BehaveX](https://github.com/hrcorval/behavex) - Production-grade test orchestration wrapper for Behave with parallel execution, enterprise reporting, and scenario ordering support.

## Tooling

- [behave-format](https://github.com/MathiasPaulenko/behave-format) - Opinionated formatter for Behave `.feature` files. Like Black, but for Gherkin.
- [behave-lint](https://github.com/MathiasPaulenko/behave-lint) - Fast, opinionated, extensible linter for Gherkin `.feature` files and Behave test suites.
- [behave-model](https://github.com/MathiasPaulenko/behave-model) - Canonical object model for Behave projects with Gherkin v6 Rules, Tag Expression v2, and full Behave 1.3.x compatibility.

## CI/CD Integrations

- [Behave CI/CD Pipeline Guide](https://deepwiki.com/behave/behave/6.2-cicd-pipeline) - Comprehensive guide on integrating Behave into CI/CD pipelines (GitHub Actions, Tox, multi-environment testing).
- [GitLab CI + Behave + Pytest](https://surestride.hashnode.dev/cicd-pipeline-for-python-with-bdd-and-tdd-using-behave-pytest-and-gitlab-ci) - Complete CI/CD pipeline tutorial using Behave, pytest, pre-commit hooks, and GitLab CI.
- [JUnit XML Reporter](https://behave.readthedocs.io/en/stable/appendix.formatters/) - Built-in `junit` reporter for Jenkins and other CI systems that consume JUnit XML.
- [ParallelBehaveAllureFlow](https://github.com/ggkiokas/ParallelBehaveAllureFlow) - Reusable GitHub Actions workflow for parallel Behave execution with Allure report generation and retry mechanism.
- [Tox](https://tox.wiki) - Generic virtualenv management and test tool for running Behave across multiple Python environments in CI.

## IDE & Editor Support

### IDE Plugins

- [Cucumber Official (VS Code)](https://marketplace.visualstudio.com/items?itemName=CucumberOpen.cucumber-official) - Official VS Code extension for Cucumber with Gherkin and Behave support.
- [Cucumber-Eclipse](https://cucumber.github.io/cucumber-eclipse/) - Eclipse plugin with Gherkin editor support.
- [cuke4vs](https://github.com/henritersteeg/cuke4vs) - Visual Studio plugin with Gherkin editor support.
- [PyCharm BDD Support](https://blog.jetbrains.com/pycharm/2014/09/feature-spotlight-behavior-driven-development-in-pycharm/) - Built-in Behave and Gherkin support in PyCharm Professional edition.

### Editor Plugins

- [Behave Step Finder (Sublime Text)](https://packagecontrol.io/packages/Behave%20Step%20Finder) - Navigate to step definitions in Behave projects.
- [Cucumber (Sublime Text)](https://packagecontrol.io/packages/Cucumber) - Gherkin editor support with table formatting.
- [Gherkin Editor](https://www.gherkineditor.com/) - Online editor for writing `.feature` files.
- [NP++ Gherkin (Notepad++)](https://productive.me/develop/cucumbergherkin-syntax-highlighting-for-notepad) - Gherkin syntax highlighting for Notepad++.
- [vim-behave](https://github.com/rooprob/vim-behave) - Vim plugin: port of vim-cucumber to Python Behave.

## Learning Resources

### Tutorials & Guides

- [Behave Examples & Tutorials](https://behave.github.io/behave.example/) - 12 progressive tutorials covering first steps, parameters, scenario outlines, tags, data types, and multi-language features.
- [Behave Tutorial](https://behave.readthedocs.io/en/stable/tutorial/) - Official getting started guide covering feature files, step implementations, context, hooks, and tags.
- [Complete Behave BDD Tutorial 2026](https://qaskills.sh/blog/behave-python-bdd-complete-tutorial) - Hands-on tutorial covering installation, project structure, hooks, fixtures, reporting, parallel execution, and Playwright integration.

### Courses

- [BDD Automation: Behave with Python](https://www.udemy.com/course/bdd-with-behave/) - Behave with Selenium and Appium integration (Udemy).
- [Behavior-driven Development (BDD) with Behave and Python](https://www.pluralsight.com/courses/behavior-driven-development-bdd-behave-python) - Full course covering Gherkin, Behave features, web testing with Selenium, and CI reporting (Pluralsight).
- [Cucumber BDD with Python Behave and Selenium WebDriver 2024](https://www.udemy.com/course/bdd-testing-with-python/) - 19-hour course building a BDD framework with Selenium, API testing, and MySQL (Udemy).

### Books

- *BDD in Action* by John Ferguson Smart - Covers BDD principles with examples across multiple languages including Python/Behave.
- *The Cucumber Book* by Matt Wynne and Aslak Hellesøy - While focused on Cucumber/Ruby, the Gherkin and BDD principles apply directly to Behave.

### Videos

- [BDD with Python Behave](https://www.youtube.com/results?search_query=behave+python+bdd) - Community YouTube tutorials and conference talks on Behave.

## Community Projects & Examples

- [appium-python-bdd](https://github.com/serhatbolsu/appium-python-bdd) - BDD test examples with Appium and Behave for mobile testing.
- [Applitools-With-Behave](https://github.com/umangbhatia786/Applitools-With-Behave) - Sample framework integrating Selenium, Behave, and Applitools for visual testing.
- [behave-gui](https://github.com/behave-contrib/behave-gui) - GUI front-end for Behave test execution.
- [behavedemo](https://github.com/andrewdjackson/behavedemo) - Demo project using pyHamcrest matchers, Requests, and Selenium with Behave.
- [cookiecutter-example](https://github.com/MathiasPaulenko/cookiecutter-example) - Cookiecutter template for generating Behave BDD test automation projects with Selenium, Allure, and configurable options.
- [python-behave-examples](https://github.com/MathiasPaulenko/python-behave-examples) - Repository with practical examples of using the Behave library in Python.
- [Python-Behave-sample-project](https://github.com/crki76/Python-Behave-sample-project) - Sample BDD automation project with Page Object Model pattern.
- [Python_Behave_Selenium_BDD](https://github.com/soumyaevan/Python_Behave_Selenium_BDD) - BDD test automation framework with Selenium and Behave.
- [Python_Selenium_BDD_Framework](https://github.com/DipankarDandapat/Python_Selenium_BDD_Framework) - Comprehensive framework with Selenium for UI, Requests for API, and BehaveX for parallel execution.
- [try-behave](https://github.com/behave-contrib/try-behave) - Try Behave directly in the browser using Pyodide, no installation required.

## Related Awesome Lists

- [Awesome BDD](https://github.com/omergulen/awesome-bdd) - General BDD ecosystem resources across all languages.
- [Awesome Playwright](https://github.com/mxschmitt/awesome-playwright) - Curated list of Playwright tools and resources.
- [Awesome Python](https://github.com/vinta/awesome-python) - General curated list of Python frameworks, libraries, and software.
- [Awesome Python Testing](https://github.com/cleder/awesome-python-testing) - Collection of Python testing resources and frameworks.
- [Awesome Selenium](https://github.com/christian-bromann/awesome-selenium) - Curated list of Selenium tools and resources.

---

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.
