.PHONY: test

test:
	pipenv run flake8 ./src
