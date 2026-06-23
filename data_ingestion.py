import pandas as pd
import os
Data_path="data/raw"
files=os.listdir(Data_path)
for file in files:
    if file.endswith(".csv"):
        file_path=os.path.join(Data_path,file)
        df=pd.read_csv(file_path)
        print(f"First 5 rows:{df.head()}")
        print(f"Shape:{df.shape}")
        print(f"Columns:{df.columns.tolist()}")
        print(f"Missing Values:{df.isnull().sum()}")
        print(f"Duplicates:{df.duplicated().sum()}")
