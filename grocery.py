import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import menu
import streamlit as st



def getSeriesId(userItem = 'beef', location = 'Northeast'):
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
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return result_dict



def grocery(userSeriesId, result_dict):
    url = f"https://data.bls.gov/timeseries/{userSeriesId}?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
    food = result_dict[userSeriesId]

    r = requests.get(url)
     #r.content
    soup = BeautifulSoup(r.content, 'html.parser')
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

    df_table = df_table[df_table['Price'] != '\xa0']
    df_table['Price'] = df_table['Price'].astype(float)

    return df_table
                



def groceryBox(table, seriesId, result_dict):
    
    # Replace empty strings with NaN
    table['Price'].replace('', pd.NA, inplace=True)
    
    # Convert 'Price' column from string to numeric
    table['Price'] = pd.to_numeric(table['Price'], errors='coerce')
    
    # Sort the data frame by 'Year'
    table_sorted = table.sort_values(by='Year')
    
    
    # Plot box-and-whisker for max and min prices
    fig = plt.figure(figsize=(10, 6))
    
    # Box-and-whisker plot
    sns.boxplot(x='Year', y='Price', data=table_sorted, whis=[0, 100])
    plt.title('Box-and-Whisker Plot for Prices of ' + result_dict[seriesId])
    plt.xlabel('Year')
    plt.ylabel('Price')
    
    plt.tight_layout()
    plt.show()
    st.pyplot(fig)


selectFood, selectRegion = menu.menugrocery()
seriesDict = getSeriesId(selectFood, selectRegion)
optionsList = list(seriesDict.values())
option = st.selectbox(
    'What option would you like?',
    optionsList)
selected_key = next(key for key, value in seriesDict.items() if value == option)
df_table = grocery(selected_key, seriesDict)
groceryBox(df_table, selected_key, seriesDict)

