import streamlit as st
import pandas as pd
import pyodbc

st.title("🤖 AI Business Analyst Dashboard")

conn=pyodbc.connect(

"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=localhost;"
"DATABASE=AI_Business_Analyst;"
"Trusted_Connection=yes;"
"TrustServerCertificate=yes;"

)

df=pd.read_sql_query("SELECT * FROM Sales",conn)

st.metric("Total Sales",round(df["Sales"].sum(),2))

st.metric("Total Profit",round(df["Profit"].sum(),2))

st.metric("Customers",df["CustomerID"].nunique())

st.subheader("Sales by Category")

st.bar_chart(df.groupby("Category")["Sales"].sum())

st.subheader("Profit by Region")

st.bar_chart(df.groupby("Region")["Profit"].sum())

question=st.text_input("Ask Business Question")

if st.button("Generate AI Insight"):

    st.success("""

Technology contributes highest sales.

Furniture has low profitability.

South region requires attention.

Recommendation:
Reduce discounts and optimize stock.

""")