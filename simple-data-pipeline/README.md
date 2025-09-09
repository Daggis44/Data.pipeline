


## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt

# 1) Run the pipeline on the demo CSV (creates data/warehouse.db)
python -m src.cli run --csv sample_data/sales.csv --db data/warehouse.db

# 2) Generate a small report (CSV + PNG in reports/)
python -m src.report --db data/warehouse.db
```

## Project Layout
```
src/
  etl.py     # extract/transform/load functions
  cli.py     # Typer CLI: run pipeline
  report.py  # reads from SQLite and writes daily revenue CSV + plot
tests/
  test_etl.py
sample_data/sales.csv
data/                 # output database here (ignored by git)
reports/              # generated report files go here
```

