# Makefile

.DEFAULT_GOAL := help

docker_image_name = "{{ cookiecutter.project_slug }}"
docker_container_name = "{{ cookiecutter.project_slug }}"
repo_name = "{{ cookiecutter.project_slug }}"
version = "{{ cookiecutter.version }}"
port = {{ cookiecutter.port }}


help:
	@echo "AVAILABLE COMMANDS"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf " \033[36m%-30s\033[0m %s\n", $$1, $$2}'

bake: ## Init a poetry env and installing some useful packages (run this first). Install poetry with `pip install poetry`.
	@poetry add fastapi uvicorn loguru requests httpx python-dotenv
	@echo "Installing dev dependencies."
	@poetry add --group test pytest pytest-cov hypothesis pyinstrument
	@poetry add --group dev radon cloc black isort mypy fire ruff
	@echo "Installing documentation dependencies."
	@poetry add --group docs mkdocs-material mkdocs-minify-plugin mkdocs-redirects mkdocstrings mkdocs-autorefs
	@echo "Python 🐍 env set using Poetry 🎉"
	@git init .
	@echo "Coding time! ✨ 🚀"

release: ## Update version and quality code rank in Makefile, pyproject.tml and README files.
	poetry run python release.py $(v) $(q)

doc: ## Generate MkDocs documentation and serve.
	@poetry run mkdocs new .
	@poetry run mkdocs serve

devmoji: ## Init devmoji (add emojis to commit messages). Install it with `npm install -g devmoji`.
	@cp .git/hooks/prepare-commit-msg.sample .git/hooks/prepare-commit-msg
	@echo "#!/bin/sh\n\nCOMMIT_MSG_FILE=\$$1\nCOMMIT_MSG=\$$(cat \$$COMMIT_MSG_FILE)\n\necho \"\$${COMMIT_MSG}\" | devmoji > \$$1" > .git/hooks/prepare-commit-msg

update_deps: ## Update dependencies.
	@poetry update

start: ## Start the API locally.
	@poetry run uvicorn $(repo_name).main:app --host 0.0.0.0 --port $(port)

test: ## Run unit tests.
	@poetry run pytest --disable-pytest-warnings
	@echo "The tests pass! ✨ 🍰 ✨"

coverage: ## Run coverage tests.
	@poetry run pytest --cov=./$(repo_name) --disable-pytest-warnings
	@echo "The tests pass! ✨ 🍰 ✨"

lock: ## Generate `poetry.lock` file for dependencies.
	@poetry lock

reqs: ## Generate a requirements.txt file.
	@poetry export --without-hashes -f requirements.txt -o requirements.txt

cloc: ## Count blank lines, comment lines, and physical lines of source code.
	@poetry run cloc --exclude-dir .venv,.DS_Store --exclude-ext gif,pyc .

code_metrics: ## Compute various metrics from the source code (code quality).
	@poetry run radon cc mi hal ./$(repo_name) -a -na -s

format: ## Format the source code using black.
	@poetry run black $(repo_name)/
	@poetry run isort $(repo_name)/

format_check: ## Check what to change using black.
	@poetry run black --check $(repo_name)/

lint: ## Lint the source code using Ruff.
	@poetry run black .
	@poetry run ruff -e --fix .

isort: ## Sort the imports using isort.
	@poetry run isort $(repo_name)/

mypy: ## Run mypy for data type check
	@poetry run mypy $(repo_name)/

build_docker: ## Build a Docker container based on Dockerfile.
	@docker image build -t $(docker_image_name):$(version) .

run_docker: ## Run the built Docker container.
	@docker container run --name $(docker_container_name) -p $(port):$(port) $(docker_image_name):$(version)

clean_docker: ## Stop and delete the container.
	@docker container stop $(docker_container_name)
	@docker rm -f $(docker_container_name)

dcup: ## Build Docker compose.
	@docker compose up --build

clean: ## Delete unwanted files.
	@rm -rf `find . -name __pycache__`
	@rm -rf `find . -name .pytest_cache`
	@rm -rf `find . -name .ipynb_checkpoints`
	@rm -rf `find . -name .DS_Store`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -f `find . -type f -name '*~' `
	@rm -f `find . -type f -name '.*~' `
	@rm -rf `find . -type d -name '*.egg-info' `
	@rm -rf `find . -type d -name 'pip-wheel-metadata' `
	@rm -rf `find . -type d -name 'tmp*' `
	@rm -rf .DS_Store
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf htmlcov
	@rm -rf *.egg-info
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf generated
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
	@find . -name '*~'    -exec rm --force {} +
	@echo "Your repo is clean! 🧹 👌🏼 ✨"
