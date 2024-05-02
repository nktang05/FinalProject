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
    page_title="Hello Welcome to data",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")
