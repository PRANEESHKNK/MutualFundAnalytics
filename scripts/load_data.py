import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///database/mutual_funds.db")

# Read cleaned datasets
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
it = pd.read_csv("data/processed/investor_transactions_cleaned.csv")
sp = pd.read_csv("data/processed/scheme_performance_cleaned.csv")

# Read fund master (raw)
fd = pd.read_csv("data/raw/01_fund_master.csv")

# Load into SQLite
fd.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
it.to_sql("fact_transactions", engine, if_exists="replace", index=False)
sp.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All datasets loaded successfully!")
from sqlalchemy import text

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

with engine.connect() as conn:
    for table in tables:
        count = conn.execute(text(f"SELECT COUNT(*) FROM {table}")).scalar()
        print(f"{table}: {count} rows")