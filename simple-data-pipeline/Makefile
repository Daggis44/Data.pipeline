.PHONY: install run test report

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
	python -m src.cli run --csv sample_data/sales.csv --db data/warehouse.db

report:
	python -m src.report --db data/warehouse.db

test:
	pytest -q