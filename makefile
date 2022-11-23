install:
	poetry install
gendiff:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
coverage:
	poetry run pytest --cov
lint:
	poetry run flake8 gendiff
pytest:
	poetry run pytest