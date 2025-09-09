import typer
from pathlib import Path
from .etl import run_pipeline

app = typer.Typer(help="Run a tiny CSV -> SQLite pipeline.")

@app.command()
def run(csv: str = typer.Option("sample_data/sales.csv", help="Path to input CSV"),
        db: str = typer.Option("data/warehouse.db", help="Path to SQLite database")):
    """Execute the end-to-end pipeline."""
    run_pipeline(Path(csv), Path(db))
    typer.echo(f"Loaded {csv} into {db}")

if __name__ == "__main__":
    app()