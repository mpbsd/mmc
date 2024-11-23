build:
	python3 -m pkgs.main

black:
	isort pkgs/main.py
	black -l 79 pkgs/main.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf

.PHONY: build black clean
