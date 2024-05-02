import streamlit as st
import pandas as pd
import sqlite3
import loadData
import menu


import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup


#loadData.loadAllData()
def locationString(location):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    if (location == "West" or location == "South" or location == "Northeast" or location == "Midwest"):
        # Query to retrieve the states in the specified region
        sql_query9 = """
            SELECT Name
            FROM states
            WHERE Region = ?
        """
    
        # Execute the SQL query to retrieve the states in the specified region
        cur.execute(sql_query9, (location,))
        region = cur.fetchall()
        
        # List of state names in the specified region
        states = [row[0] for row in region]
        
        # Convert the list of state names to a comma-separated string for the IN clause
        state_names_str = ', '.join([f"'{state}'" for state in states])
        return state_names_str

    else:
        return location

    # Close the connection
    conn.close()

    

def avgPop(location, yearStart = None, yearEnd = None):
    # Connect to the database
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    state_names_str = locationString(location)

    year_condition = ""
    if yearStart is not None and yearEnd is not None:
        year_condition = f"AND Year >= {yearStart} AND Year <= {yearEnd}"
    
    sql_query2 = f"""
        SELECT o.Year, AVG(population) AS avg_population
        FROM popData o
        JOIN states s ON o.Region = s.Name
        WHERE s.Name IN ({state_names_str}) {year_condition}
        GROUP BY o.Year
        """

    # Execute the SQL query and load the results into a DataFrame
    data2 = pd.read_sql_query(sql_query2, conn)
    
    # Print the results
    print(data2)
    
    # Close the connection
    conn.close()

    # Plot the data
    fig = plt.figure()
    plt.plot(data2['Year'], data2['avg_population'], label='Average Population')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f"Average Population in {location} from {yearStart} to {yearEnd}")

    # Add legend
    plt.legend()

    plt.tight_layout()  # Adjust layout to prevent clipping of x-axis labels
    st.pyplot(fig)


year, location = menu.menuPop()
myLoc = locationString(location)
avgPop(myLoc, year[0], year[1])