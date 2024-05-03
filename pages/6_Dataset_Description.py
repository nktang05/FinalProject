import streamlit as st
import numpy as np


st.set_page_config(page_title="Dataset Descriptions", page_icon="📈")
st.markdown("# Dataset Descriptions")

st.write(
    """ **Grocery Data Souce- From the US Bureau of Labor Statistcs**

        URL for website:
        https://www.bls.gov


        API fot Downloading for Times Series by Series ID:
        https://beta.bls.gov/dataQuery/find


        This website is scrapable. It contains the data for prices of different groceries over periods of time. I can also sort it by area of the US for example west, south, midwest etc. The different grocery options are sorted by a Series ID. Using the seriesID I go back into the website and get the specific grocery p[rice data for food with that seriesID. I wrote multiple functions to get user input of food, find seriesIDs with use food in the label, let user pick which seriesID they want and then return it in a data frame to be used
    """ )

st.write("""
         **Population Data Source- US Census**

        URL for website or API: https://www.census.gov/data/developers/data-sets.html
        (If API, link to API docs) (example. I will be using more years than this one):
        https://api.census.gov/data/2021/pep/population
         
        The US Census has API’s for each year and state and the corresponding population.
        The data I will be utilizing from this data set is the population for each state over various
        years. Its used to track population growth over time depending on locations. 
         
         """)

st.write("""
        **State Region DataSet**
         
         self generated
         
        This is a bonus data csv file. It has a list of states and what region, north, south etc they are a part of so a user can input a state and i can query for the region to be spit out.
"""
)

st.write("""
        **Obesity Data Set- CDC**
        
        URL for website to scrape or download, or API:
        https://nccd.cdc.gov/dnpao_dtm/rdPage.aspx
         
        Csv file that has obesity/weight status that can be sorted by stated and year.
""")