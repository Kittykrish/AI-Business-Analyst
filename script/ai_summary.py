import pandas as pd
import pyodbc
from openai import OpenAI

client=OpenAI(api_key="YOUR_API_KEY")

conn=pyodbc.connect(

"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=localhost;"
"DATABASE=AI_Business_Analyst;"
"Trusted_Connection=yes;"
"TrustServerCertificate=yes;"

)

df=pd.read_sql_query("SELECT * FROM Sales",conn)

category=df.groupby("Category")[["Sales","Profit"]].sum()

summary=f"""

Total Sales:
{df['Sales'].sum()}

Total Profit:
{df['Profit'].sum()}

Top Category:
{category['Sales'].idxmax()}

Lowest Profit Category:
{category['Profit'].idxmin()}

"""

response=client.chat.completions.create(

model="gpt-4o-mini",

messages=[

{"role":"system",
"content":"You are an expert Business Analyst."},

{"role":"user",
"content":summary}

]

)

print(response.choices[0].message.content)

conn.close()