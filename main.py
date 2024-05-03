import streamlit as st
import pandas as pd
import sqlite3
import loadData
import menu
import grocery
import obesity
import population
import union


import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

#loadData.loadAllData()

st.set_page_config(
    page_title="DSCI510-FinalProject",
    page_icon="👋",
)

st.write("# DSCI510 Final Project- Nicole Tang")

st.write("""This site allows you to see if there are any possible correlations between obesity rates, population, and prices of food. These datasets can be sorted by state, region, and year. The following pages allow you to see individual visualizations of 
         obesity rates, population, and prices of food and you can see how they vary by state and year. Then you can see if how they correlate with each other and see graphs of the following data. Major gotchas include all three variables on average consistantly increasing over the years.
         """)
