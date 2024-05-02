import pandas as pd
import sqlite3

def get_obesity_data():
    # import csv files

    file = "Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System_20240412.csv"
    df1 = pd.read_csv(file, header = 0, usecols=[1,3,5,7,10,16])
    df1.dropna(inplace=True)

    def feed_csv_data(filename, table_name):
        conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        cur = conn.cursor()
        df = pd.read_csv(filename)

        # make data fram
        df1 = pd.read_csv(filename, header = 0, usecols=[1,3,5,7,10,16])
        df1.dropna(inplace=True)

        # set to sql table
        df1.to_sql(table_name, conn, if_exists='replace')
        
        cur.execute(f'SELECT * FROM {table_name} LIMIT 2')
        return_val = cur.fetchall()
        print(return_val)

        conn.commit()
        conn.close()

    feed_csv_data(file, "obesity_health")