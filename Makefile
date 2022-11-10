install:  #  create environment variables and dependencies
	poetry install

gendiff:  # run application
	poetry run gendiff

build:
	poetry build

publish:		
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

start-tests:
	poetry run pytest

test-coverage:
	run pytest --cov=gendiff tests/ --cov-report xml


