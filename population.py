import menu
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import streamlit as st

# method to return states from region
def locationString(location):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    # check if a region and get states
    if (location == "West" or location == "South" or location == "Northeast" or location == "Midwest"):
        # Query to retrieve the states in the specified region
        sql_query9 = """
            SELECT Name
            FROM states
            WHERE Region = ?
        """

        # Execute the SQL query with parameters
        cur.execute(sql_query9, (location,))
        region = cur.fetchall()
        
        # List of state names in the specified region
        states = [row[0] for row in region]
        
        # Convert the list of state names
        state_names_str = ', '.join([f"'{state}'" for state in states])
        return state_names_str
        # Close the connection
        conn.close()

    else:
        return f"'{location}'"

# method to get population data and make graph
def avgPop(location1, location2, yearStart = None, yearEnd = None):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    # get states
    state_names_str1 = locationString(location1)
    state_names_str2 = locationString(location2)

    # set conditional 
    year_condition = ""
    if yearStart is not None and yearEnd is not None:
        year_condition = f"AND Year >= {yearStart} AND Year <= {yearEnd}"
    
    # query data
    sql_query2 = f"""
        SELECT o.Year, AVG(population) AS avg_population
        FROM popData o
        JOIN states s ON o.Region = s.Name
        WHERE s.Name IN ({state_names_str1}) {year_condition}
        GROUP BY o.Year
        """

    # Execute the SQL query and load the results into a DataFrame
    data2 = pd.read_sql_query(sql_query2, conn)

    # query data
    sql_query3 = f"""
        SELECT o.Year, AVG(population) AS avg_population
        FROM popData o
        JOIN states s ON o.Region = s.Name
        WHERE s.Name IN ({state_names_str2}) {year_condition}
        GROUP BY o.Year
        """

    # Execute the SQL query and load the results into a DataFrame
    data3 = pd.read_sql_query(sql_query3, conn)
    
    # Close the connection
    conn.close()

    # Plot the data
    fig = plt.figure()
    plt.plot(data2['Year'], data2['avg_population'], label=location1)
    plt.plot(data3['Year'], data3['avg_population'], label=location2)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f"Population in {location1} vs {location2} from {yearStart} to {yearEnd}")

    # Add legend
    plt.legend()

    plt.tight_layout()  # Adjust layout to prevent clipping of x-axis labels
    st.pyplot(fig)

   # method to get population data of one region and multiple years and graph 
def singlePop(location1, yearStart = None, yearEnd = None):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    # get state names from region
    state_names_str1 = locationString(location1)

    # get year condition
    year_condition = ""
    if yearStart is not None and yearEnd is not None:
        year_condition = f"AND Year >= {yearStart} AND Year <= {yearEnd}"
    
    # query data
    sql_query2 = f"""
        SELECT o.Year, AVG(population) AS avg_population
        FROM popData o
        JOIN states s ON o.Region = s.Name
        WHERE s.Name IN ({state_names_str1}) {year_condition}
        GROUP BY o.Year
        """

    # Execute the SQL query 
    data2 = pd.read_sql_query(sql_query2, conn)
    
    data2['Year'] = data2['Year'].astype(int)
    
    # Close the connection
    conn.close()

    return(data2)

