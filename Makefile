.venv:
	python -m venv .venv
	pipenv install

check: .venv
	pipenv run python main.py