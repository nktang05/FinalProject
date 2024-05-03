import sqlite3
import pandas as pd
import openpyxl

# method to get state data
def get_state_data():
    # Get state data from excel
    statexlsx = "states.xlsx"
    df1 = pd.read_excel(statexlsx)
    df1.dropna(inplace=True)

    # feed data into sql database
    def feed_state_data(filename, table_name):
        conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        cur = conn.cursor()

        # get data
        data = pd.read_excel(filename)
        data.dropna(inplace=True)

        # set to sql table
        data.to_sql(table_name, conn, if_exists='replace')

        conn.commit()
        conn.close()

    feed_state_data(statexlsx, "states")
