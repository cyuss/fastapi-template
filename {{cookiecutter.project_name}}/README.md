# {{cookiecutter.project_name}}

![py_version](https://img.shields.io/badge/python-^3.9-blue?style=for-the-badge&logo=python&logoColor=9cf) ![version](https://img.shields.io/badge/version-0.1.0-gree?style=for-the-badge&logo=semver) ![code quality](https://img.shields.io/badge/code_quality-A-51C62B?style=for-the-badge&logo=codeforces&logoColor=9cf)

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [{{cookiecutter.project\_name}}](#cookiecutterproject_name)
	- [Context](#context)
	- [Get started](#get-started)
		- [Init the project](#init-the-project)
		- [Development workflow](#development-workflow)
		- [Code quality](#code-quality)
		- [Documentation \& versioning](#documentation--versioning)
	- [Future improvements](#future-improvements)

<!-- /TOC -->

## Context

## Get started

### Init the project

A `Makefile` is set up with all the useful commands to use this API.

```text
AVAILABLE COMMANDS
 bake                           Init a poetry env and installing some useful packages (run this first).
                                Install poetry with `pip install poetry`.
 build_docker                   Build a Docker container based on Dockerfile.
 clean                          Delete unwanted files.
 clean_docker                   Stop and delete the container.
 cloc                           Count blank lines, comment lines, and physical lines of source code.
 code_metrics                   Compute various metrics from the source code (code quality).
 coverage                       Run coverage tests.
 dcup                           Build Docker compose.
 devmoji                        Init devmoji (add emojis to commit messages).
                                Install it with `npm install -g devmoji`.
 doc                            Generate MkDocs documentation and serve.
 format                         Format the source code using black.
 format_check                   Check what to change using black.
 isort                          Sort the imports using isort.
 lint                           Lint the source code using Ruff.
 lock                           Generate `poetry.lock` file for dependencies.
 mypy                           Run mypy for data type check
 release                        Update version and quality code rank in Makefile, pyproject.tml 
                                and README files.
 reqs                           Generate a requirements.txt file.
 run_docker                     Run the built Docker container.
 start                          Start the API locally.
 test                           Run unit tests.
 update_deps                    Update dependencies.
```

First, you need to init the environment by using the command `make bake` which sets up the python virtualenv using poetry, installing required dependencies and init the git repository.

**PS:** To add emojies to git commit messages, use `make devmoji`.

### Development workflow

During the development workflow, you can use these following commands:

- `make start`: to start the API on a defined host and port, then you can access the swagger through <https://{host}:{port}/docs> to test the defined routes.
- `make test`: launch `pytest` with the defined unit tests.
- `make coverage`: check the tests coverage.
- `make build_docker`: build a docker image based on the `Dockerfile` to test the project when contained.
- `make run_docker`: run and access the built container.
- `make clean_docker`: clean and delete the docker image.

To add a new route in the project, simply define it in `{{ cookiecutter.project_slug }}/routes`. Every route's inputs/outputs are defined in `schemas.py` file for data validation.

A `core/` folder is defined to regroup all the configuration and settings related files. Globa and environment variables and centralized in `settings.py` file for simplicity and better management.

If you decide to use `pip` for packages management instead of `poetry`, 2 commands are used for the switch:

- `make reqs`: generate a `requirements.txt` file for `pip`.
- `make reqs_dev`: generate a `requirements_dev.txt` for dev environment packages.

### Code quality

Few commands are defined to ensure a minimum quality code:

- `make format`: the most important command, it formats all the project using `black` and sorting the `import` statements.
- `make format_check`: preview the files and lines to format before formatting.
- `make isort`: sort `import` statements in every python file. this command is also called in `make format`.
- `make mypy`: type check in different functions/classes using `mypy`.
- `make cloc`: count blank lines, comment lines, and physical lines of source code.
- `make code_metrics`: compute various metrics from the source code.

All the packages used for ensuring a quality code are configured in the poetry configuration file, `pyproject.toml`. Every related configuration is defined by its own section.

> **Important:** It's highly recommended to use docstrings in every function/class when possible.

### Documentation & versioning

To keep a good documentation, it's very important to keep this `README` file always updated. You can also use `mkdocs` to generate documentation which could be deployed in `github pages`. `mkdocs` is recommended to use when you working a on big project that requires a very rich documentation where a simple `README` isn't enough.

To use `mkdocs`, you can run the following command `make doc` which build and launch the server for documentation.

Keeping the project's history is also very important to allow future improvements, for that a `CHANGELOG` file is defined listing every release dated and describing what was added, changed, removed... etc. It follows the following format:

```markdown
## [{version}] - yyyy-mm-dd
### { Added | Changed | Removed | Deprecated | Fixed | Security }
- to add
- to add
```

The release version follows the norms of [semantic versioning](https://semver.org/). Given a version number `MAJOR.MINOR.PATCH`, we increment the:

- MAJOR version when you make incompatible API changes,
- MINOR version when you add functionality in a backwards compatible manner.
- PATCH version when you make backwards compatible bug fixes.

**Important:** The version variable must be kept updated in three different files:

- `README` file, where a badge version is used,
- `Makefile`, where the version is used as a variable,
- `pyproject.toml`, a project's version is kept in poetry configuration file.

Some useful functions are used to keep these three files' version updated using `release.py` script, a command is defined using `make release {version} {code quality}`.

The git commit messages are organized by category to simplify the project's history. It follows the following format `<type>[optional scope]: <description>` where the commit type takes the following rules:

```text
- :feat:          feat: a new feature
- :fix:           fix: a bug fix
- :docs:          docs: documentation only changes
- :style:         style: changes that do not affect the meaning of the code
                  (white-space, formatting, missing semi-colons, etc)
- :refactor:      refactor: a code change that neither fixes a bug nor adds a feature
- :perf:          perf: a code change that improves performance
- :test:          test: adding missing or correcting existing tests
- :chore:         chore: changes to the build process or auxiliary tools and
                  libraries such as documentation generation
- :chore-release: chore(release): code deployment or publishing to external repositories
- :chore-deps:    chore(deps): add or delete dependencies
- :build:         build: changes related to build processes
- :ci:            ci: updates to the continuous integration system
- :config:        config: Changing configuration files.
- :security:      security: Fixing security issues.
```

## Future improvements
