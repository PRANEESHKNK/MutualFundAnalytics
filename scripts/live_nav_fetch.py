import pandas as pd
import os
import requests
url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data=response.json()
print(data["meta"]["scheme_name"])#meta-Details About the Fund and schema_name -  find scheme_name.
print(data["data"])#Stores Data
df=pd.DataFrame(data["data"])   
print(df.head())
df.to_csv("data/raw/hdfc_top100_live_nav.csv", index=False)
