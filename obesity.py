import menu


import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import streamlit as st

def obesityTable(year1, year2):

    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    ## Your code here

    # Construct SQL queries with placeholders for years
    sql_query2 = f"SELECT AVG(data_value) AS '{year1}', LocationDesc FROM obesity_health WHERE YearEnd = ? AND class = 'Obesity / Weight Status' GROUP BY LocationDesc Order By LocationDesc ASC"
    sql_query3 = f"SELECT AVG(data_value) AS '{year2}', LocationDesc FROM obesity_health WHERE YearEnd = ? AND class = 'Obesity / Weight Status' GROUP BY LocationDesc Order By LocationDesc ASC"

    # Execute the SQL queries with the years as parameters
    data2 = pd.read_sql_query(sql_query2, conn, params=(year1,))
    data3 = pd.read_sql_query(sql_query3, conn, params=(year2,))

    conn.commit()
    conn.close()

    fig = plt.figure()
    plt.plot(data2['LocationDesc'], data2[str(year1)], marker='o', linestyle='-', label=str(year1))
    plt.plot(data3['LocationDesc'], data3[str(year2)], marker='o', linestyle='-', label=str(year2))

    # Adding labels and title
    plt.xlabel('State')
    plt.ylabel('Percentage')
    plt.title(f"Obesity Rates by State {year1} vs {year2}")
    plt.legend()

    # Rotating x-axis labels for better readability
    plt.xticks(rotation=90)

    # Display the plot
    plt.tight_layout()  # Adjust layout to prevent clipping of x-axis labels
    st.pyplot(fig)

year1, year2 = menu.menuObesity()
obesityTable(year1, year2)