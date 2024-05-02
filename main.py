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
        # Query to retrieve the states in the West region
        sql_query9 = """
            SELECT Name
            FROM states
            WHERE Region = ?
        """
    
        # Execute the SQL query to retrieve the states in the West region
        region = pd.read_sql(sql_query9, conn, params=(location,))
        
        # List of state names in the West region
        states = region['Name'].tolist()
        
        # Convert the list of state names to a comma-separated string for the IN clause
        state_names_str = ', '.join([f"'{state}'" for state in states])

    else:
        state_names_str = f"'{location}'"

    # Close the connection
    conn.close()

    return state_names_str

# to compare regions
def obesityRegion(location1, location2, yearStart = None, yearEnd = None):
    # Connect to the database
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()

    state_names_str1 = locationString(location1)
    state_names_str2 = locationString(location2)

    # Condition for filtering years
    year_condition = ""
    if yearStart is not None and yearEnd is not None:
        year_condition = f"AND YearEnd >= {yearStart} AND YearEnd <= {yearEnd}"

    # SQL query to calculate the average data value for each year in the West region
    sql_query2 = f"""
        SELECT YearEnd AS Year, AVG(data_value) AS Avg_Obesity_Rate
        FROM obesity_health o
        JOIN states s ON o.locationDesc = s.Name
        WHERE s.Name IN ({state_names_str1}) AND o.class = 'Obesity / Weight Status' {year_condition}
        GROUP BY YearEnd
    """
    
    # Execute the SQL query and load the results into a DataFrame
    data2 = pd.read_sql(sql_query2, conn)

    #SQL query to calculate the average data value for each year in the West region
    sql_query3 = f"""
        SELECT YearEnd AS Year, AVG(data_value) AS Avg_Obesity_Rate
        FROM obesity_health o
        JOIN states s ON o.locationDesc = s.Name
        WHERE s.Name IN ({state_names_str2}) AND o.class = 'Obesity / Weight Status' {year_condition}
        GROUP BY YearEnd
    """
    
    # Execute the SQL query and load the results into a DataFrame
    data3 = pd.read_sql(sql_query3, conn)
    
    # Print the results
    print(data2)

    st.write("test")
    
    # Plot the data
    fig = plt.figure()
    plt.plot(data2['Year'], data2['Avg_Obesity_Rate'], label=location1)
    plt.plot(data3['Year'], data3['Avg_Obesity_Rate'], label=location2)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Obestiy Rate')
    plt.title(f"Average Obesity Rated in {location1} vs {location2} from {yearStart} to {yearEnd}")

    # Add legend
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent clipping of x-axis labels
    st.pyplot(fig)

    # Close the connection
    conn.close()

year, region1, region2 = menu.menuObestiyRegion()
obesityRegion(region1, region2, year[0], year[1])
