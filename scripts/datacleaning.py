import pandas as pd
import os
df=pd.read_csv("data/raw/02_nav_history.csv")
print(df.head())
print("-"*40)
print(df.info())
print("-"*40)
print(df.describe())
print("-"*40)
print(df.shape)
print("-"*40)
print(f"Columns:{df.columns}")
print("-"*40)
print(f"NULL values :{df.isnull().sum()}")
print("-"*40)
print(f"Duplicates:{df.duplicated().sum()}")
print("-"*40)
df['date']=pd.to_datetime(df["date"]) 
print(df.dtypes)
print("-"*40)
df=df.sort_values(["amfi_code","date"])
print("-"*40)
print((df["nav"]<=0).sum())
print("-"*40)
df.to_csv(
    "data/processed/clean_nav.csv",
    index=False
)