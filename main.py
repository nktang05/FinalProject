import streamlit as st
import pandas as pd
import sqlite3
import loadData
import matplotlib.pyplot as plt



st.write("hello World")
print("hi")


#loadData.loadAllData()



conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

## Your code here

sql_query2 = "SELECT  AVG(data_value) AS '2014', LocationDesc from obesity_health where YearEnd = 2014 and class = 'Obesity / Weight Status'  Group by LocationDesc"

# Execute the SQL query and load the results into a DataFrame
data2 = pd.read_sql(sql_query2, conn)

print(data2)

sql_query3 = "SELECT  AVG(data_value) AS '2017', LocationDesc from obesity_health where YearEnd = 2017 and class = 'Obesity / Weight Status'  Group by LocationDesc"

# Execute the SQL query and load the results into a DataFrame
data3 = pd.read_sql(sql_query3, conn)

print(data3)

conn.commit()
conn.close()

fig = plt.figure()
plt.plot(data2['LocationDesc'], data2['2014'], marker='o', linestyle='-', label='2014')
plt.plot(data3['LocationDesc'], data3['2017'], marker='o', linestyle='-', label='2017')

# Adding labels and title
plt.xlabel('State')
plt.ylabel('Percentage')
plt.title('Obesity Rates by State 2014 vs 2017')
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=90)

# Display the plot
plt.tight_layout()  # Adjust layout to prevent clipping of x-axis labels
st.pyplot(fig)

