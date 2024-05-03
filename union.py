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

# method to get multivariable graphs
def unionGraphs():
    # get which type of graph from user
    graph = menu.menuUnion()
    # get food and region from user
    selectFood, selectRegion = menu.menugrocery()
    # get seriesID dictionary
    seriesDict = grocery.getSeriesId(selectFood, selectRegion)
    
    # check if a valid food choice
    if not seriesDict:
        st.write("Please pick another food type. Recommended foods are beef, chicken, bread")

    else:
        # run methods to get food pricing data froam of grocery prices
        optionsList = list(seriesDict.values())
        option = st.selectbox(
        'What option would you like?',
        optionsList)
        selected_key = next(key for key, value in seriesDict.items() if value == option)
        food = grocery.grocery(selected_key, seriesDict)

    # get obesity data 
    obe = obesity.obesityRegion(selectRegion)
    # get population data
    pop = population.singlePop(selectRegion)

    # average the food prices retrievd
    food_price_avg = food.groupby("Year")['Price'].mean()

    # make figure
    fig, ax = plt.subplots()

    # check which  type of graph and set appropriate lines of data
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
    plt.title(f" {graph} over time" )

    st.pyplot(fig)