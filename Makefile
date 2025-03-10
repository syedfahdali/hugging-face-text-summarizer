install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=hello --cov=greeting \
		--cov=smath --cov=web tests
	python -m pytest --nbval notebook.ipynb

debug:
	python -m pytest -vv --pdb

one-test:
	python -m pytest -vv tests/test-greeting.py::test_my_name4