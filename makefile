build:
	python3 -m pkgs.core --profile 16

black:
	isort pkgs/core.py
	black -l 79 pkgs/core.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf

.PHONY: build black clean
