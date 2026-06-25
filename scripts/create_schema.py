import sqlite3
import os

os.makedirs("database", exist_ok=True)

db_path = os.path.abspath("database/mutual_funds.db")
print("Database path:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Connected successfully!")

# ==========================
# CREATE TABLES HERE
# ==========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_fund (
    fund_key INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
)
""")

# Add the other CREATE TABLE statements here

conn.commit()
conn.close()

print("Schema created successfully!")