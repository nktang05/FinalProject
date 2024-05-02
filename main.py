import streamlit as st
import pandas as pd
import sqlite3
import loadData
import menu
import grocery
import obesity
import population


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
food = grocery.grocery(selected_key, seriesDict)

obe = obesity.obesityRegion(selectRegion)

pop = population.singlePop(selectRegion)

fig, ax = plt.subplots()

line1, = ax.plot(food['Year'], food['Price'], linestyle = "--", color = "blue", label='Price')
ax.set_xlabel('Years')
ax.set_ylabel('Data1')

#ax2 = ax.twinx()
#line2,  = ax2.plot(obe['Year'], obe['Avg_Obesity_Rate'], label='Obesity Rate', color = "red")
#ax2.set_ylabel('Data2')

ax3 = ax.twinx()
line3, = ax3.plot(pop["Year"], pop['avg_population'], label = 'Population', color = "green")

# plot food and obesity
#ax2.legend(handles=[line1, line2])

# plot food and population
ax.legend(handles=[line1, line3])

# plot obesity and population
#ax3.legend(handles=[line2, line3])

plt.tight_layout()
plt.title('2 plots')

st.pyplot(fig)

