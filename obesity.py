import menu
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import streamlit as st

# method to graph obesity data and compare
def obesityTable(year1, year2):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    # Cuery data
    sql_query2 = f"SELECT AVG(data_value) AS '{year1}', LocationDesc FROM obesity_health WHERE YearEnd = ? AND class = 'Obesity / Weight Status' GROUP BY LocationDesc Order By LocationDesc ASC"
    sql_query3 = f"SELECT AVG(data_value) AS '{year2}', LocationDesc FROM obesity_health WHERE YearEnd = ? AND class = 'Obesity / Weight Status' GROUP BY LocationDesc Order By LocationDesc ASC"

    # Execute the SQL queries with the years as parameters
    data2 = pd.read_sql_query(sql_query2, conn, params=(year1,))
    data3 = pd.read_sql_query(sql_query3, conn, params=(year2,))

    conn.commit()
    conn.close()

    # plot figure
    fig = plt.figure()
    plt.plot(data2['LocationDesc'], data2[str(year1)], marker='o', linestyle="", label=str(year1))
    plt.plot(data3['LocationDesc'], data3[str(year2)], marker='o', linestyle="", label=str(year2))

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

# method to get region from states
def locationString(location):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    # query the state names fron user data
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

# method to compare regions of obesity rates
def obesityRegionCompare(location1, location2, yearStart = None, yearEnd = None):
    # Connect to the database
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()

    # get string of states in region
    state_names_str1 = locationString(location1)
    state_names_str2 = locationString(location2)

    # Condition for years
    year_condition = ""
    if yearStart is not None and yearEnd is not None:
        year_condition = f"AND YearEnd >= {yearStart} AND YearEnd <= {yearEnd}"

    # query to get obesity data using join of tables
    sql_query2 = f"""
        SELECT YearEnd AS Year, AVG(data_value) AS Avg_Obesity_Rate
        FROM obesity_health o
        JOIN states s ON o.locationDesc = s.Name
        WHERE s.Name IN ({state_names_str1}) AND o.class = 'Obesity / Weight Status' {year_condition}
        GROUP BY YearEnd
    """
    
    # Execute the SQL query
    data2 = pd.read_sql(sql_query2, conn)

    #SQL query for next set of data
    sql_query3 = f"""
        SELECT YearEnd AS Year, AVG(data_value) AS Avg_Obesity_Rate
        FROM obesity_health o
        JOIN states s ON o.locationDesc = s.Name
        WHERE s.Name IN ({state_names_str2}) AND o.class = 'Obesity / Weight Status' {year_condition}
        GROUP BY YearEnd
    """
    
    # Execute the SQL query and load the results into a DataFrame
    data3 = pd.read_sql(sql_query3, conn)
    
    # Plot the data
    fig = plt.figure()
    plt.plot(data2['Year'], data2['Avg_Obesity_Rate'], label=location1)
    plt.plot(data3['Year'], data3['Avg_Obesity_Rate'], label=location2)

    plt.xlabel('Year')
    plt.ylabel('Obestiy Rate')
    plt.title(f"Average Obesity Rated in {location1} vs {location2} from {yearStart} to {yearEnd}")

    plt.legend()
    plt.tight_layout() 
    st.pyplot(fig)

    # Close the connection
    conn.close()

# method to get obesity by yers
def obesityRegion(location1, yearStart = None, yearEnd = None):
    # Connect to the database
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()

    # method to get location
    state_names_str1 = locationString(location1)

    # Condition for filtering years
    year_condition = ""
    if yearStart is not None and yearEnd is not None:
        year_condition = f"AND YearEnd >= {yearStart} AND YearEnd <= {yearEnd}"

    # SQL query 
    sql_query2 = f"""
        SELECT YearEnd AS Year, AVG(data_value) AS Avg_Obesity_Rate
        FROM obesity_health o
        JOIN states s ON o.locationDesc = s.Name
        WHERE s.Name IN ({state_names_str1}) AND o.class = 'Obesity / Weight Status' {year_condition}
        GROUP BY YearEnd
    """
    
    # Execute the SQL query and load the results into a DataFrame
    data2 = pd.read_sql(sql_query2, conn)

    return data2