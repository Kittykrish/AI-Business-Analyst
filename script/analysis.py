import pandas as pd
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=AI_Business_Analyst;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

query = "SELECT * FROM Sales_1"

df = pd.read_sql_query(query, conn)

df["OrderDate"] = pd.to_datetime(df["Order_Date"])

df["Discount"] = pd.to_numeric(
    df["Discount"],
    errors="coerce"
)

df["Sales"] = pd.to_numeric(
    df["Sales"],
    errors="coerce"
)

df["Profit"] = pd.to_numeric(
    df["Profit"],
    errors="coerce"
)

print("="*60)
print("BUSINESS SUMMARY")
print("="*60)

print("Total Sales :", round(df["Sales"].sum(),2))
print("Total Profit :", round(df["Profit"].sum(),2))
print("Average Discount :", round(df["Discount"].mean(),2))
print("Orders :", len(df))
print("Unique Customers :", df["Customer_ID"].nunique())

print("\n")

category=df.groupby("Category")[["Sales","Profit"]].sum()

print(category)

print("\nTop States")

state_1=df.groupby("State")["Sales"].sum()

print(state_1.sort_values(ascending=False).head(10))

print("\nTop Customers")

customer=df.groupby("Customer_Name")["Sales"].sum()

print(customer.sort_values(ascending=False).head(10))

conn.close()