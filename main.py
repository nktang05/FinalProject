import streamlit as st
import pandas as pd
import sqlite3
import loadData



st.write("hello World")
print("hi")


#loadData.loadAllData()



conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = conn.cursor()


sql_query9 = "SELECT * from seriesID LIMIT 3"

# Execute the SQL query and load the results into a DataFrame
data9 = pd.read_sql(sql_query9, conn)

print(data9)
st.write(data9)

conn.commit()
conn.close()