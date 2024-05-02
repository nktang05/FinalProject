import streamlit as st



def menugrocery():
    foodType = ["beef", "chicken", "bread", "apples"]
    region = ["Northeast", "West", "South", "Midwest"]

    selectFood = st.selectbox(
        'Select a item?',
        foodType)
    st.write("Your chosen food item", selectFood)

    selectRegion = st.selectbox(
        'Select a region?',
        region)
    st.write("Your chosen region", selectRegion)
    
    return selectFood, selectRegion

def menuObesity():
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

    selectYear1 = st.selectbox(
        'Select a year to compare?',
        years)
    st.write("Your chosen year", selectYear1)

    selectYear2 = st.selectbox(
        'Select a second year to compare?',
        years)
    st.write("Your chosen year", selectYear2)
    
    return selectYear1, selectYear2
