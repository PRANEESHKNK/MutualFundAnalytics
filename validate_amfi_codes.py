import pandas as pd
import os
fd=pd.read_csv("data/raw/01_fund_master.csv")
nv=pd.read_csv("data/raw/02_nav_history.csv")
f_code=set(fd["amfi_code"])
n_code=set(nv["amfi_code"])
missing_codes = f_code-n_code
extra_codes = n_code-f_code
print("AMFI CODE VALIDATION REPORT")
print("--------------------")
print(f"\nFund_Master Code:{len(f_code)}")
print(missing_codes)
print(f"\nNAV_Code:{len(n_code)}")
print(extra_codes)