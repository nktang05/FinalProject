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

graph = menu.menuUnion()

selectFood, selectRegion = menu.menugrocery()

if selectFood is not None and selectRegion is not None:

    seriesDict = grocery.getSeriesId(selectFood, selectRegion)
    optionsList = list(seriesDict.values())
    option = st.selectbox(
        'What option would you like?',
        optionsList)
    
    if option is not None: 
        selected_key = next(key for key, value in seriesDict.items() if value == option)
        food = grocery.grocery(selected_key, seriesDict)

        obe = obesity.obesityRegion(selectRegion)

        print("Data2")
        pop = population.singlePop(selectRegion)

        food_price_avg = food.groupby("Year")['Price'].mean()

        print(food_price_avg.index)

        fig, ax = plt.subplots()

        if (graph == "Food Prices and Obesity Rates"):

            line1, = ax.plot(food_price_avg.index, food_price_avg, linestyle = "--", color = "blue", label='Price')
            ax.set_xlabel('Years')
            ax.set_ylabel('Food Prices')

            ax2 = ax.twinx()
            line2,  = ax2.plot(obe['Year'], obe['Avg_Obesity_Rate'], label='Obesity Rate', color = "red")
            ax2.set_ylabel('Obesity Rates')

        elif(graph == "Food Prices and Population"):

            line1, = ax.plot(food_price_avg.index, food_price_avg, linestyle = "--", color = "blue", label='Price')
            ax.set_xlabel('Years')
            ax.set_ylabel('Food Prices')

            ax2 = ax.twinx()
            line2,  = ax2.plot(pop["Year"], pop['avg_population'], label = 'Population', color = "green")
            ax2.set_ylabel('Population')

        elif(graph == "Population and Obesity Rates"):
            line1,  = ax.plot(obe['Year'], obe['Avg_Obesity_Rate'], label='Obesity Rate', color = "red")
            ax.set_xlabel('Years')
            ax.set_ylabel('Obesity Rates')

            ax2 = ax.twinx()
            line2,  = ax2.plot(pop["Year"], pop['avg_population'], label = 'Population', color = "green")
            ax2.set_ylabel('Population')


        #plot food and obesity
        ax2.legend(handles=[line1, line2])

        plt.tight_layout()
        plt.title('2 plots')

        st.pyplot(fig)

elif selectFood is None:
    st.write("select Food")

elif selectRegion is None:
    st.write("select region")

else:
    st.write("other error")