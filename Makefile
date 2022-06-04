MODULE = .
LIBS        = $(MODULE)
PYTHON      = poetry run python
PRECOMMIT   = poetry run pre-commit



.PHONY: clean fmt lint test init shell run-stack down-stack scrape


pyproject.toml:
	@touch $@

poetry.lock: pyproject.toml
	@poetry env use "$(shell which python)"
	@poetry install
	@touch $@

init: poetry.lock .git/hooks/pre-commit

shell: poetry.lock
	@poetry shell
