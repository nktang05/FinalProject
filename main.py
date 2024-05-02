import streamlit as st
import loadData
import pandas as pd
import sqlite3
import loadObesity
import loadPop



st.write("hello World")
print("hi")


print("data loaded")

#loadPop.get_pop_data()

conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = conn.cursor()


sql_query9 = "SELECT * from population LIMIT 3"

# Execute the SQL query and load the results into a DataFrame
data9 = pd.read_sql(sql_query9, conn)

print(data9)
st.write(data9)

conn.commit()
conn.close()