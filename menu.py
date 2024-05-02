import streamlit as st



def menu():
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

