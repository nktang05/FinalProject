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



def getSeriesId(userItem, location):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    
    # Use proper string formatting for the user input and location
    sql_query10 = f"""
         SELECT `Series ID`, `Series Title`
        FROM seriesID
        WHERE item LIKE ? AND Area = ?
    """
    
    # Execute the SQL query with the user input as a parameter
    cur.execute(sql_query10, ('%' + userItem + '%', location))
    
    # Fetch the results
    results = cur.fetchall()
    
    # Execute the SQL query and load the results into a DataFrame
    data10 = pd.DataFrame(results, columns=['Series ID', 'Series Title'])
    
    result_dict = {row[0]: row[1] for row in results}
    
    print(data10)
    
    print(result_dict)
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return result_dict



def feed_data(df, table_name):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    
    ### Write Your code here ###
    
    # set to sql table
    df.to_sql(table_name, conn, if_exists='replace')

    ### Your code ends here ###
    
    cur.execute(f'SELECT * FROM {table_name} LIMIT 2')
    return_val = cur.fetchall()
    print(return_val)

    conn.commit()
    conn.close()


def grocery(userSeriesId, result_dict):
    url = f"https://data.bls.gov/timeseries/{userSeriesId}?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
    food = result_dict[userSeriesId]

    r = requests.get(url)
     #r.content
    soup = BeautifulSoup(r.content, 'lxml')
    t1 = soup.find('table', {"id":"table0"})
    headerx = t1.find('thead').find('tr').find_all('th')
    header = [x.contents[0] for x in headerx]

    table = []
    index = []
    rows = t1.find('tbody').find_all('tr')
    for row in rows:
        datax = row.find_all('td')
        indexx = row.find('th')
        data = [x.contents[0] for x in datax]
        index.append(int(indexx.contents[0]))
        table.append(data)

    df = pd.DataFrame(data = table, index = index, columns = header[1:])

    df_table = pd.DataFrame(columns = ["Year", "Month", "Price"])

    for index, row in df.iterrows():
        for col in df.columns:
            if row[col] is not None:
                df_table.loc[len(df_table)] = [index, col, row[col]]
                

    feed_data(df_table, userSeriesId)

def groceryTable(table, result_dict):
    # Connect to the database
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    
    # Execute the SQL query and load the results into a DataFrame
    sql_query2 = "SELECT * FROM {}".format(table)
    data2 = pd.read_sql(sql_query2, conn)
    
    # Close the connection
    conn.close()
    
    
    
    # Replace empty strings with NaN
    data2['Price'].replace('', pd.NA, inplace=True)
    
    # Convert 'Price' column from string to numeric
    data2['Price'] = pd.to_numeric(data2['Price'], errors='coerce')
    
    # Sort the data frame by 'Year'
    data2_sorted = data2.sort_values(by='Year')
    
    
    # Plot box-and-whisker for max and min prices
    fig = plt.figure(figsize=(10, 6))
    
    # Box-and-whisker plot
    sns.boxplot(x='Year', y='Price', data=data2_sorted, whis=[0, 100])
    plt.title('Box-and-Whisker Plot for Prices of ' + result_dict[table])
    plt.xlabel('Year')
    plt.ylabel('Price')
    
    plt.tight_layout()
    st.pyplot(fig)


"""
selectFood, selectRegion = menu.menu()



seriesDict = getSeriesId(selectFood, selectRegion)

optionsList = list(seriesDict.values())

option = st.selectbox(
    'What option would you like?',
    optionsList)

selected_key = next(key for key, value in seriesDict.items() if value == option)

grocery(selected_key, seriesDict)
groceryTable(selected_key, seriesDict)
"""

selectFood, selectRegion = menu.menu()
seriesDict = getSeriesId(selectFood, selectRegion)
optionsList = list(seriesDict.values())
option = st.selectbox(
    'What option would you like?',
    optionsList)
selected_key = next(key for key, value in seriesDict.items() if value == option)
grocery(selected_key, seriesDict)
groceryTable(selected_key, seriesDict)