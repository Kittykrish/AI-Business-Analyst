import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn = pyodbc.connect(

"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=localhost;"
"DATABASE=AI_Business_Analyst;"
"Trusted_Connection=yes;"
"TrustServerCertificate=yes;"

)

df=pd.read_sql_query("SELECT * FROM Sales_1",conn)

df["OrderDate"]=pd.to_datetime(df["OrderDate"])

category=df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

category.plot(kind="bar")

plt.title("Sales by Category")

plt.ylabel("Sales")

plt.show()

df["Month"]=df["OrderDate"].dt.month_name()

monthly=df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10,5))

monthly.plot(marker="o")

plt.title("Monthly Sales")

plt.ylabel("Sales")

plt.grid()

plt.show()

region=df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))

region.plot(kind="bar")

plt.title("Profit by Region")

plt.show()

conn.close()