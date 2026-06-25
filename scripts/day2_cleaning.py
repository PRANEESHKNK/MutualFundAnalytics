import pandas as pd
print("="*40)
print("---CLEANING NAV_HISTORY---")
df=pd.read_csv("data/raw/02_nav_history.csv")
df["date"]=pd.to_datetime(df["date"])
df=df.sort_values(["amfi_code","date"])
df=df.drop_duplicates()
df["nav"]=df.groupby("amfi_code")["nav"].ffill()
df=df[df["nav"]>0]
print(df.head())
print("="*40)
print("----Cleaning Investor Transaction----")

it=pd.read_csv("data/raw/08_investor_transactions.csv")
it["transaction_date"]=pd.to_datetime(it["transaction_date"])
it["transaction_type"]=(it["transaction_type"].str.strip().str.upper())
mapping={
    "SIP":"SIP",
    "SYSTEMATIC":"SIP",
    "LUMP SUM":"LUMPSUM",
    "REDEMPTION":"REDEMPTION",
    "REDEEM":"REDEMPTION"
}
it["transaction_type"]=it["transaction_type"].replace(mapping)
it=it[it["amount_inr"]>0]
valid=["YES","NO","PENDING"]
it["kyc_status"]=(it["kyc_status"].str.upper())
invalid=it[~it["kyc_status"].isin(valid)]
print("Invalid KYC - ",invalid)
print("="*40)
print("----Cleaning Scheme_Performance----")
sp=pd.read_csv("data/raw/07_scheme_performance.csv")

cols=["return_1yr_pct",
"return_3yr_pct",
"return_5yr_pct"]
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for c in cols:
    sp[c] = pd.to_numeric(sp[c], errors="coerce")
anomalies=sp[sp[cols].isna().any(axis=1)]
expense_outliers = sp[(sp["expense_ratio_pct"]<0.1) | (sp["expense_ratio_pct"]>2.5)]
print(anomalies)
print(expense_outliers)
print("="*40)

import os

os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)
it.to_csv("data/processed/investor_transactions_cleaned.csv", index=False)
sp.to_csv("data/processed/scheme_performance_cleaned.csv", index=False)
print("All cleaned datasets saved successfully!")