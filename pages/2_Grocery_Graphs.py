import streamlit as st
import time
import numpy as np
import grocery
import menu

st.set_page_config(page_title="Grocery Demo", page_icon="📈")

st.markdown("# Grocery Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)


selectFood, selectRegion = menu.menugrocery()


seriesDict = grocery.getSeriesId(selectFood, selectRegion)

if not seriesDict:
    st.write("Please pick another food type. Recommended foods are beef, chicken, bread")

else:
    optionsList = list(seriesDict.values())
    option = st.selectbox(
    'What option would you like?',
    optionsList)


    selected_key = next(key for key, value in seriesDict.items() if value == option)
    food = grocery.grocery(selected_key, seriesDict)

    grocery.groceryBox(food, selected_key, seriesDict)