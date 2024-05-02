import streamlit as st
import pandas as pd
import sqlite3
import loadData
import menu
import grocery
import obesity


import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

#loadData.loadAllData()


selectFood, selectRegion = menu.menugrocery()
seriesDict = grocery.getSeriesId(selectFood, selectRegion)
optionsList = list(seriesDict.values())
option = st.selectbox(
    'What option would you like?',
    optionsList)
selected_key = next(key for key, value in seriesDict.items() if value == option)
df_table = grocery.grocery(selected_key, seriesDict)

data1 = obesity.obesityRegion(selectRegion)

fig, ax = plt.subplots()

line1, = ax.plot(df_table['Year'], df_table['Price'], linestyle = "--", color = "blue", label='Price')
ax.set_xlabel('Years')
ax.set_ylabel('Data1')

ax2 = ax.twinx()
line2,  = ax2.plot(data1['Year'], data1['Avg_Obesity_Rate'], label='Obesity Rate', color = "red")
ax2.set_ylabel('Data2')

ax2.legend(handles=[line1, line2])
plt.title('2 plots')

st.pyplot(fig)