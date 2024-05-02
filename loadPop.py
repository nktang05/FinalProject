import requests
import pandas as pd
import sqlite3


# method to get population data as population
def get_pop_data():
    # get api data

    key = "d57dfb3474ecd922cc1c04161f67290ae9f3c25d"
    url2019 = f" https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=state:*&key={key}"
    url2018 = f" https://api.census.gov/data/2018/pep/population?get=GEONAME,POP&for=state:*&key={key}"
    url2017 = f" https://api.census.gov/data/2017/pep/population?get=GEONAME,POP&for=state:*&key={key}"
    url2016 = f" https://api.census.gov/data/2016/pep/population?get=GEONAME,POP&for=state:*&key={key}"
    url2015 = f" https://api.census.gov/data/2015/pep/population?get=GEONAME,POP&for=state:*&key={key}"
    url2014 = f" https://api.census.gov/data/2014/pep/natstprc?get=STNAME,POP&for=state:*&DATE_=6&key={key}"
    url2013 = f" https://api.census.gov/data/2013/pep/natstprc?get=STNAME,POP&for=state:*&DATE_=6&key={key}"
    urlxlsx = "https://www2.census.gov/programs-surveys/popest/tables/2020-2023/state/totals/NST-EST2023-POP.xlsx"

    #2019
    r_data2019 = requests.get(url2019).json()
    df_2019 = pd.DataFrame(r_data2019[1:], columns=r_data2019[0])
    df_2019.drop(['state'], axis=1, inplace=True)
    df_2019['POP'].apply(lambda x: int(x))
    df_2019.rename(columns = {'NAME': 'Region', 'POP':2019}, inplace = True)
    df_2019.set_index('Region')

    #2018
    r_data2018 = requests.get(url2018).json()
    df_2018 = pd.DataFrame(r_data2018[1:], columns=r_data2018[0])
    df_2018.drop(['state'], axis=1, inplace=True)
    df_2018['POP'].apply(lambda x: int(x))
    df_2018.rename(columns = {'GEONAME': 'Region', 'POP':2018}, inplace = True)
    df_2018.set_index('Region')

    #2017
    r_data2017 = requests.get(url2017).json()
    df_2017 = pd.DataFrame(r_data2017[1:], columns=r_data2017[0])
    df_2017.drop(['state'], axis=1, inplace=True)
    df_2017['POP'].apply(lambda x: int(x))
    df_2017.rename(columns = {'GEONAME': 'Region', 'POP':2017}, inplace = True)
    df_2017.set_index('Region')

    #2016
    r_data2016 = requests.get(url2016).json()
    df_2016 = pd.DataFrame(r_data2016[1:], columns=r_data2016[0])
    df_2016.drop(['state'], axis=1, inplace=True)
    df_2016['POP'].apply(lambda x: int(x))
    df_2016.rename(columns = {'GEONAME': 'Region', 'POP':2016}, inplace = True)
    df_2016.set_index('Region')

    #2015
    r_data2015 = requests.get(url2015).json()
    df_2015 = pd.DataFrame(r_data2015[1:], columns=r_data2015[0])
    df_2015.drop(['state'], axis=1, inplace=True)
    df_2015['POP'].apply(lambda x: int(x))
    df_2015['GEONAME'] = df_2015['GEONAME'].apply(lambda x: x.split(',')[0])
    df_2015.rename(columns = {'GEONAME': 'Region', 'POP':2015}, inplace = True)
    df_2015.set_index('Region')

    #2014
    r_data2014 = requests.get(url2014).json()
    df_2014 = pd.DataFrame(r_data2014[1:], columns=r_data2014[0])
    df_2014.drop('DATE_', axis = 1, inplace = True)
    df_2014.drop(['state'], axis=1, inplace=True)
    df_2014['POP'].apply(lambda x: int(x))
    df_2014['STNAME'] = df_2014['STNAME'].apply(lambda x: x.replace('Puerto Rico Commonwealth', 'Puerto Rico'))
    df_2014.rename(columns = {'STNAME': 'Region', 'POP':2014}, inplace = True)
    df_2014.set_index('Region')

    #2013
    r_data2013 = requests.get(url2013).json()
    df_2013 = pd.DataFrame(r_data2013[1:], columns=r_data2013[0])
    df_2013.drop(['state'], axis=1, inplace=True)
    df_2013.drop('DATE_', axis = 1, inplace = True)
    df_2013['POP'].apply(lambda x: int(x))
    df_2013['STNAME'] = df_2013['STNAME'].apply(lambda x: x.replace('Puerto Rico Commonwealth', 'Puerto Rico'))
    df_2013.rename(columns = {'STNAME': 'Region', 'POP':2013}, inplace = True)
    df_2013.set_index('Region')

    df1 = pd.read_excel(urlxlsx, header = 3, nrows = 58)

    df1.rename(columns = {df1.columns[0]:'Region', df1.columns[1]:'Base'}, inplace = True)
    df1.dropna(inplace=True)
    df1.drop('Base', axis=1, inplace=True)
    df1['Region'] = df1['Region'].apply(lambda x: x.replace('.', ''))
    df1.set_index('Region')

    df1[2020] = df1[2020].apply(lambda x: int(x))
    df1[2021] = df1[2021].apply(lambda x: int(x))
    df1[2022] = df1[2022].apply(lambda x: int(x))
    df1[2023] = df1[2023].apply(lambda x: int(x))

    data = pd.merge(df_2013, df_2014)
    data = pd.merge(data, df_2015)
    data = pd.merge(data, df_2016)
    data = pd.merge(data, df_2017)
    data = pd.merge(data, df_2018)
    data = pd.merge(data, df_2019)
    data = pd.merge(data, df1)

    def feed_api_data(data, table_name):
        conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        cur = conn.cursor()

        
        # set to sql table
        data.to_sql(table_name, conn, if_exists='replace')

        ### Your code ends here ###
        
        cur.execute(f'SELECT * FROM {table_name} LIMIT 2')
        return_val = cur.fetchall()
        print(return_val)

        conn.commit()
        conn.close()

    feed_api_data(data, "population")

def transpose():
    conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()

    ## Your code here

    cur.execute('''
    CREATE TABLE IF NOT EXISTS popData (
        Region TEXT,
        Year TEXT,
        Population INTEGER
        );
        ''')

    cur.execute('''
        INSERT INTO popData (Region, Year, Population)
        SELECT
            Region,
            2013 AS Year,
            [2013] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2014 AS Year,
            [2014] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2015 AS Year,
            [2015] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2016 AS Year,
            [2016] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2017 AS Year,
            [2017] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2018 AS Year,
            [2018] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2019 AS Year,
            [2019] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2020 AS Year,
            [2020] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2021 AS Year,
            [2021] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2022 AS Year,
            [2022] AS Population
        FROM
            population
        UNION ALL
        SELECT
            Region,
            2023 AS Year,
            [2023] AS Population
        FROM
            population;
    ''')

    conn.commit()
    conn.close()

#transpose()