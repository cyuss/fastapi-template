# Project Template for Rest API
A projet template created by [`Cookiecutter`](https://github.com/cookiecutter/cookiecutter) to automate projects creation for REST API development.

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Project Template for Rest API](#project-template-for-rest-api)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
    - [Cookiecutter](#cookiecutter)
    - [Poetry](#poetry)
    - [Devmoji](#devmoji)
  - [Get Started](#get-started)
  - [Conventional commits](#conventional-commits)

<!-- /TOC -->

## Project Structure
First of all, we illustrate the project structure by describing each file and directory created in this template.

```
.
├── CHANGELOG.md                     # autogenerated file by devmoji
├── data
├── docker-compose.yml
├── Dockerfile
├── docs                             # documentation and examples
├── Makefile                         # predefined command lines
├── models                           # serialized ML/DL models
├── notebooks                        # all notebooks for data exploration
├── pytest.ini                       # pytest config file
├── README.md
├── tests                            # unit and ML tests
│  ├── __init__.py
│  ├── conftest.py                   # conftest file for pytest
│  ├── test_api                      # api unit tests
│  │  ├── __init__.py
│  │  └── test_webservice.py
│  └── test_ml                       # ML tests
│     └── __init__.py
├── TODO.org                         # todo list in org mode file
├── tox.ini                          # tox config file
└── {{ cookiecutter.project_slug }}  # project subdirectory (main dir)
   ├── __init__.py
   ├── core                          # api config directory
   │  ├── __init__.py
   │  ├── event_handlers.py          # event handlers config (e.g: api start)
   │  ├── middlewares.py             # middlewares config (e.g: request_id)
   │  ├── settings.py                # api settings, global variables... etc
   │  └── setup_logger.py            # logger configuration (e.g: log format)
   ├── db                            # database communication functions
   │  └── __init__.py
   ├── main.py                       # main file to start the API
   ├── routes                        # routes dir
   │  ├── __init__.py                # global routes store
   │  ├── hello_route.py             # default route created
   │  └── schemas.py                 # schemas for input/output validation
   └── utils                         # utility functions
      └── __init__.py
```

## Prerequisites
To generate a new project from this template, first you should install the following packages:

### Cookiecutter
[`Cookiecutter`](https://github.com/cookiecutter/cookiecutter) is a command-line utility that creates projects from templates. You can install it using `pip`:

```shell
pip install cookiecutter
```
Or, using Homebrew (Mac OS X only):
```shell
brew install cookiecutter
```

### Poetry
To make dependencies installation easier, we use [`Poetry`](https://github.com/python-poetry/poetry) as a dependency manager. You can install it using `pip`:

```shell
pip install poetry
```

Or, using Homebrew (Mac OS X only):
```shell
brew install poetry
```

### Devmoji
> [Devmoji](https://github.com/folke/devmoji) is a command line tool that adds color 🌈 to conventional commits, using emojis inspired by Gitmoji 😜.
> Some of the things Devmoji can do:
>   - **emojify:** convert input between diferent emoji formats unicode, shortcode and devmoji. devmoji are easy to remember aliases like: :test:, :refactor:, :docs:, :security instead of hard to remember emoji codes
>   - **git commit:** install a prepare-commit-msg commit hook to ✨ automagically emojify and lints your commit message
>   - **git log:** emojify and colorify the output of git log even for projects not using emojis

You can install `devmoji` using `npm` or `yarn`:
```shell
npm install -g devmoji
yarn global add devmoji
```

## Get Started
To initiate a new project using this template, you can simply use:
```shell
cookiecutter https://github.com/cyuss/fastapi-template.git
```

Then you need to setup python environment and install some dependencies. For that, you can use the predefined commands in `Makefile`.

```
AVAILABLE COMMANDS
 bake                           Init a poetry env and installing some useful packages (run this first).
                                Install poetry with `pip install poetry`.
 build_docker                   Build a Docker container based on Dockerfile.
 clean                          Delete unwanted files.
 clean_docker                   Stop and delete the container.
 coverage                       Launch coverage tests.
 dcup                           Build Docker compose.
 devmoji                        Init devmoji (add emojis to commit messages).
                                Install it with `npm install -g devmoji`.
 reqs                           Generate a requirements.txt file.
 reqs_dev                       Generate a requirements_dev.txt file.
 run_docker                     Run the built Docker container.
 start                          Start the API locally.
 test                           Run unit tests.
 tox                            Run tox.
 update_deps                    Update dependencies.
```

First command to execute is:
```zsh
make bake
```

It inits a `poetry` environment and install following dependencies used for this workflow:
- fastapi, uvicorn, requests (web framework tools for building API with Python),
- loguru (logging library),
- pytest, pytest-cov, tox (for unit/ml tests)

Once everything is installed, you can now start building your API.
To get fancy and organized commit messages, you should setup `devmoji` with:
```zsh
make devmoji
```

It configs `devmoji` as a `prepare-commit` hook in `git` without using a third-party package. `devmoji` automatically add emojis corresponding to commit type (cf. [Conventional commits](#conventional-commits))

**P.S:** this step is optional, you can ignore it if you wanna keep traditional commit messages.

## Conventional commits
To keep the commit history explicit, clean and organized, it's interesting to follow a set of rules that define a lightweight convention on top of commit messages. Inspired by [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/), a commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The `<type>` describes the commit type and takes the following values:

```
- ✨   :feat:          feat: a new feature
- 🐛   :fix:           fix: a bug fix
- 📚️   :docs:          docs: documentation only changes
- 🎨   :style:         style: changes that do not affect the meaning of the code
                       (white-space, formatting, missing semi-colons, etc)
- ♻️    :refactor:      refactor: a code change that neither fixes a bug nor adds a feature
- ⚡️    :perf:          perf: a code change that improves performance
- 🚨   :test:          test: adding missing or correcting existing tests
- 🔧   :chore:         chore: changes to the build process or auxiliary tools and
                       libraries such as documentation generation
- 🚀   :chore-release: chore(release): code deployment or publishing to external repositories
- 🔗   :chore-deps:    chore(deps): add or delete dependencies
- 📦️   :build:         build: changes related to build processes
- 👷   :ci:            ci: updates to the continuous integration system
- ⚙️    :config:        config: Changing configuration files.
- 🔒️   :security:      security: Fixing security issues.
```

**P.S:** If `devmoji` is configued (using the `makefile` command), it adds an emojy to every commit message according to its type.
