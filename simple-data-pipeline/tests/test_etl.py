from pathlib import Path
import pandas as pd
from src.etl import extract, transform

def test_transform_adds_line_revenue(tmp_path: Path):
    df = pd.DataFrame({
        'order_id': [1],
        'order_date': ['2025-01-01'],
        'customer_id': [10],
        'product_id': [5],
        'quantity': [2],
        'unit_price': [3.5],
        'country': ['NO'],
    })
    out = transform(df)
    assert 'line_revenue' in out.columns
    assert float(out['line_revenue'].iloc[0]) == 7.0