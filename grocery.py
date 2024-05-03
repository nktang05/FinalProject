import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt
import menu
import streamlit as st


# method to return a dictionary of seriesID:food label from the seriesID data base
# parameters- userItem- general food type to query, location
def getSeriesId(userItem, location):
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    
    # query seriesID and food label
    sql_query10 = f"""
         SELECT `Series ID`, `Series Title`
        FROM seriesID
        WHERE item LIKE ? AND Area = ?
    """
    
    # execute query with parameters
    cur.execute(sql_query10, ('%' + userItem + '%', location))
    results = cur.fetchall()
    
    # set into dataframe
    data10 = pd.DataFrame(results, columns=['Series ID', 'Series Title'])
    
    # return data into a dict
    result_dict = {row[0]: row[1] for row in results}
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

    return result_dict

# method to get specific grocery data from a seriesID and return the dataframe
# parameters- seriesID chosen from user, dict if ids and labels
def grocery(userSeriesId, result_dict):

    # get specific website using the seriesID
    url = f"https://data.bls.gov/timeseries/{userSeriesId}?amp%253bdata_tool=XGtable&output_view=data&include_graphs=true"
    # get specific food label from dict
    food = result_dict[userSeriesId]

    # webscrape the site and set data into ad dataframe
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    t1 = soup.find('table', {"id":"table0"})
    headerx = t1.find('thead').find('tr').find_all('th')
    header = [x.contents[0] for x in headerx]
    table = []
    index = []
    rows = t1.find('tbody').find_all('tr')
    # append data into lists
    for row in rows:
        datax = row.find_all('td')
        indexx = row.find('th')
        data = [x.contents[0] for x in datax]
        index.append(int(indexx.contents[0]))
        table.append(data)
    # append data to data frame
    df = pd.DataFrame(data = table, index = index, columns = header[1:])
    df_table = pd.DataFrame(columns = ["Year", "Month", "Price"])

    # reformat the columns in the data frame
    for index, row in df.iterrows():
        for col in df.columns:
            if row[col] is not None:
                df_table.loc[len(df_table)] = [index, col, row[col]]

    # make sure the prices are ints and set in dataframe
    df_table = df_table[df_table['Price'] != '\xa0']
    df_table['Price'] = df_table['Price'].astype(float)

    return df_table
                
# method to plot the grocery data into a box plot
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
    st.pyplot(fig)


