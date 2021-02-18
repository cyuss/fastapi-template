# Makefile

.DEFAULT_GOAL := help

help:
	@echo "AVAILABLE COMMANDS"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf " \033[36m%-30s\033[0m %s\n", $$1, $$2}'

devmoji: ## Init devmoji (add emojies to commit messages).
	@cp .git/hooks/prepare-commit-msg.sample .git/hooks/prepare-commit-msg
	@echo "#!/bin/sh\n\nCOMMIT_MSG_FILE=\$$1\nCOMMIT_MSG=\$$(cat \$$COMMIT_MSG_FILE)\n\necho \"\$${COMMIT_MSG}\" | devmoji > \$$1" > .git/hooks/prepare-commit-msg

clean: ## Delete unwanted files.
	@rm -rf `find . -name __pycache__`
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
	@echo "Your repo is clean! 🧹👌🏼✨"
