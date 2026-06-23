import pandas as pd
import os
fd=pd.read_csv("data/raw/01_fund_master.csv")
print(fd["fund_house"].unique()) #Unique Fund_house
print("---------------")
print(fd["category"].unique())
print("---------------")
print(fd["sub_category"].unique())
print("---------------")
print(fd["risk_category"].unique())
print("---------------")
