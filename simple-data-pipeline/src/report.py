from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def main(db_path: str = "data/warehouse.db"):
    eng = create_engine(f"sqlite:///{db_path}", future=True)
    # daily revenue
    q = """
        SELECT order_date, SUM(line_revenue) AS revenue
        FROM fact_sales
        GROUP BY order_date
        ORDER BY order_date
    """
    df = pd.read_sql(q, eng, parse_dates=["order_date"])
    # Save CSV
    Path("reports").mkdir(exist_ok=True, parents=True)
    out_csv = Path("reports/daily_revenue.csv")
    df.to_csv(out_csv, index=False)
    # Plot (no custom colors per style guide)
    plt.figure()
    plt.plot(df["order_date"], df["revenue"])  # default styling
    plt.title("Daily Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    out_png = Path("reports/daily_revenue.png")
    plt.tight_layout()
    plt.savefig(out_png)
    print(f"Wrote {out_csv} and {out_png}")

if __name__ == "__main__":
    main()