import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd


# method for series data as table seriesId
def get_series_data():
    # webscraping data
    url = "https://beta.bls.gov/dataQuery/find?fq=survey:[ap]"
    r = requests.get(url)
    r.content
    soup = BeautifulSoup(r.content, 'lxml')
    itemsx = soup.find('body').find_all('div', {'class': 'dq-result-item'})
    itemlist = ['Series Title', 'Series ID', 'Survey Name', 'Measure Data Type', 'Area', 'Item']
    data = []
    
    # iterate through page data and append to list
    for item in itemsx:
        dat = {}
        rows = item.find('table').find('tbody').find_all('tr')
        for row in rows:
            dat[row.find('th').contents[0]] = row.find('td').contents[0]
        data.append(dat)

    maxpage = 100
    page = 1
    data = []
    stop = False
    url = 'https://beta.bls.gov/dataQuery/find?fq=survey:[ap]'

    # check if there is another page to webscrape
    while (page < maxpage) and (stop is False):
        
        # webscrape
        r = requests.get(url)
        r.content
        soup = BeautifulSoup(r.content, 'lxml')
        itemsx = soup.find('body').find_all('div', {'class': 'dq-result-item'})
        
        for item in itemsx:
            dat = {}
            rows = item.find('table').find('tbody').find_all('tr')
            for row in rows:
                dat[row.find('th').contents[0]] = row.find('td').contents[0]
            data.append(dat)

        nextx = soup.find('body').find('div', {'class':'dq-next-page'}).find('a', {'id':'nextlink'})
        if nextx is None:
            stop = True
        else:
            url = 'https://beta.bls.gov/dataQuery/' + nextx['href']
        page += 1

    # method to feed the data into the sql database
    def feed_web_data(table_name):
        conn = sqlite3.connect('tang.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        cur = conn.cursor()

        maxpage = 100
        page = 1
        data = []
        stop = False
        url = 'https://beta.bls.gov/dataQuery/find?fq=survey:[ap]'

        # check if there is another page to webscrape
        while (page < maxpage) and (stop is False):
            # webscrape
            r = requests.get(url)
            r.content
            soup = BeautifulSoup(r.content, 'lxml')
            
            itemsx = soup.find('body').find_all('div', {'class': 'dq-result-item'})
            
            # set data to list
            for item in itemsx:
                dat = {}
                rows = item.find('table').find('tbody').find_all('tr')
                for row in rows:
                    dat[row.find('th').contents[0]] = row.find('td').contents[0]
                data.append(dat)

            nextx = soup.find('body').find('div', {'class':'dq-next-page'}).find('a', {'id':'nextlink'})
            if nextx is None:
                stop = True
            else:
                url = 'https://beta.bls.gov/dataQuery/' + nextx['href']
            page += 1


        df = pd.DataFrame(data)

        # set to sql table
        df.to_sql(table_name, conn, if_exists='replace')

        conn.commit()
        conn.close()

    feed_web_data("seriesID")