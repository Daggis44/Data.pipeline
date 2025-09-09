from __future__ import annotations
from pathlib import Path
from typing import Tuple
import pandas as pd
from sqlalchemy import create_engine

def extract(csv_path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Basic cleaning and enrichment
    out = df.copy()
    # Ensure dtypes
    out['order_date'] = pd.to_datetime(out['order_date'], errors='coerce').dt.date
    out['quantity'] = pd.to_numeric(out['quantity'], errors='coerce').fillna(0).astype(int)
    out['unit_price'] = pd.to_numeric(out['unit_price'], errors='coerce').fillna(0.0)
    # New calculated columns
    out['line_revenue'] = out['quantity'] * out['unit_price']
    return out

def load_to_sqlite(df: pd.DataFrame, db_path: str | Path, table: str = 'fact_sales', if_exists: str = 'replace') -> None:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    eng = create_engine(f"sqlite:///{db_path}", future=True)
    df.to_sql(table, eng, if_exists=if_exists, index=False)

def run_pipeline(csv_path: str | Path, db_path: str | Path) -> None:
    raw = extract(csv_path)
    clean = transform(raw)
    load_to_sqlite(clean, db_path)