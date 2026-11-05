UV ?= uv
UV_RUN = $(UV) run --locked --python 3.14

.PHONY: lock lint test

lock:
	$(UV) lock

lint:
	$(UV_RUN) yamllint --strict -c tests/yamllint.yaml blueprints/ .github/workflows/

test: lint
	$(UV_RUN) pytest
