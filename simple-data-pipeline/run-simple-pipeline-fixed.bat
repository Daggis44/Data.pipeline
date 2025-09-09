@echo off
REM Simple Data Pipeline one-click runner (Windows) — FIXED
REM - Avoids Typer subcommand issue by calling Python directly.
REM Usage: place this file in the project root and double-click.

setlocal

if not exist .venv\Scripts\activate.bat (
  echo Creating virtual environment...
  py -3 -m venv .venv
)

call .venv\Scripts\activate.bat
echo Installing requirements...
pip install -r requirements.txt

echo Running pipeline (CSV -> SQLite)...
python -c "from src.etl import run_pipeline; run_pipeline('sample_data\\sales.csv','data\\warehouse.db')"

echo Generating report...
python -m src.report --db data\warehouse.db

echo Done. Outputs:
echo   - data\warehouse.db
echo   - reports\daily_revenue.csv
echo   - reports\daily_revenue.png
pause
