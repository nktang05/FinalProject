import streamlit as st
import time
import numpy as np
import grocery
import menu

# set titles and headers
st.set_page_config(page_title="Grocery Demo", page_icon="📈")
st.markdown("# Grocery Demo")

# explanation of data
st.write(
    """This is a visualization tool to look at prices of food and how they change over time. Please type a type of food ex. beef, chicken, candy, bread. If the food is not the database of available foods please type another food. Select a region of the US as well. 
    This graph shows the min, max, and average of the food for each year of data available."""
)

# run method to get user food and region
selectFood, selectRegion = menu.menugrocery()
# run method to get the possible series for chosen food and put id and label into dict
seriesDict = grocery.getSeriesId(selectFood, selectRegion)

# if user food is not in the data request another type
if not seriesDict:
    st.write("Please pick another food type. Recommended foods are beef, chicken, bread")

else:
    # put food labels into list and present to user
    optionsList = list(seriesDict.values())
    option = st.selectbox(
    'What option would you like?',
    optionsList)
    # get the series id fron the label
    selected_key = next(key for key, value in seriesDict.items() if value == option)
    # get data frame of grocery prices
    food = grocery.grocery(selected_key, seriesDict)
    # graph visualization
    grocery.groceryBox(food, selected_key, seriesDict)