import streamlit as st
import pandas as pd
# import pyodbc
import google.generativeai as genai

#Put API Key Here To Get Output

genai.configure(api_key="Your API Key")

model = genai.GenerativeModel("gemini-2.5-flash")

df=pd.read_excel("data/sales.xlsx")


st.set_page_config(
    page_title="AI Business Analyst",
    layout="wide"
)

st.title("AI Business Analyst Dashboard")


# conn = pyodbc.connect(

# "DRIVER={ODBC Driver 17 for SQL Server};"
# "SERVER=localhost;"
# "DATABASE=AI_Business_Analyst;"
# "Trusted_Connection=yes;"
# "TrustServerCertificate=yes;"

# )

# df = pd.read_sql_query("SELECT * FROM Sales_1", conn)



col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${df['Sales'].sum():,.2f}"
)

col2.metric(
    "Total Profit",
    f"${df['Profit'].sum():,.2f}"
)

col3.metric(
    "Orders",
    len(df)
)

col4.metric(
    "Customers",
    df["Customer_ID"].nunique()
)

st.divider()



c1,c2 = st.columns(2)

with c1:

    st.subheader("Sales by Category")

    st.bar_chart(
        df.groupby("Category")["Sales"].sum()
    )

with c2:

    st.subheader("Profit by Region")

    st.bar_chart(
        df.groupby("Region")["Profit"].sum()
    )

st.divider()



st.subheader("Ask AI Business Analyst")

question = st.text_input(
    "Example: Which category is performing best?"
)

if st.button("Generate AI Insight"):

    summary = f"""

Total Sales:
{df['Sales'].sum()}

Total Profit:
{df['Profit'].sum()}

Orders:
{len(df)}

Customers:
{df['Customer_ID'].nunique()}

Category Sales:

{df.groupby("Category")["Sales"].sum()}

Category Profit:

{df.groupby("Category")["Profit"].sum()}

Region Sales:

{df.groupby("Region")["Sales"].sum()}

Region Profit:

{df.groupby("Region")["Profit"].sum()}

"""

    prompt = f"""

You are a Senior Business Analyst.

Using the business summary below,
answer the user's question.

Business Summary:

{summary}

Question:

{question}

Provide:

1. Executive Summary

2. Key Findings

3. Recommendation

"""

    response = model.generate_content(prompt)

    st.success(response.text)

# conn.close()
