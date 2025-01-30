build:
	python3 -m pkgs.core --profile 12 --semester 2025_1

black:
	isort pkgs/core.py
	black -l 79 pkgs/core.py

clean:
	find . -type d -name __pycache__    | xargs rm -rf
	find . -type f -name sorted.txt     | xargs rm -rf
	find . -type f -name suggestion.txt | xargs rm -rf

.PHONY: build black clean
