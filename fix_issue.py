import pandas as pd
import pyodbc

# Read Excel
df = pd.read_excel("data/sales.xlsx")
print(df.dtypes)