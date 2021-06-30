.PHONY: archive download test

archive:
	pipenv run python src/archive.py

download:
	pipenv run python src/download.py

test:
	pipenv run flake8 ./src
