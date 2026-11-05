UV ?= uv

.PHONY: lock test

lock:
	$(UV) lock

test:
	$(UV) run --locked yamllint --strict -c tests/yamllint.yaml blueprints/ .github/workflows/
