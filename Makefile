.venv:
	python -m venv .venv
	pipenv install

initDb: .venv
	pipenv run python init_db.py

check: .venv
	pipenv run pytest
