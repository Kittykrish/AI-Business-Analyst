import pyodbc
import pandas as pd

conn = pyodbc.connect(

"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=localhost;"
"DATABASE=AI_Business_Analyst;"
"Trusted_Connection=yes;"
"TrustServerCertificate=yes;"

)

def run_query(sql):

    return pd.read_sql(sql, conn)