import streamlit as st



def menugrocery():
    #foodType = ["beef", "chicken", "bread", "apples", "candy", "sugar", "ice cream"]
    region = ["Northeast", "West", "South", "Midwest"]

    
    selectRegion = st.selectbox(
        'Select a region?',
        region, placeholder = "Northeast")
    st.write("Your chosen region", selectRegion)

    """
    selectFood = st.selectbox(
        'Select a item?',
        foodType, placeholder = "beef")
    st.write("Your chosen food item", selectFood)
    """
    
    selectFood = st.text_input('Select Food Type', 'beef')
    st.write("Your chosen food item is", selectFood)

    selectFood.strip()

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


def menuPop():
    year = st.slider('Select a range of years',
    2013, 2023, (2013, 2023))

    region = ["Northeast", "West", "South", "Midwest", 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'National', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
   
    selectRegion1 = st.selectbox('Select the first region or state', region)
    st.write("You selected:", selectRegion1)

    selectRegion2 = st.selectbox('Select the second region or state', region)
    st.write("You selected:", selectRegion2)

    return year, selectRegion1, selectRegion2

def menuObestiyRegion():

    year = st.slider('Select a range of years',
    2011, 2022, (2011, 2022))

    region = ["Northeast", "West", "South", "Midwest", 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'National', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
   
    selectRegion1 = st.selectbox('Select the first region or state', region)
    st.write("You selected:", selectRegion1)

    selectRegion2 = st.selectbox('Select the second region or state', region)
    st.write("You selected:", selectRegion2)

    return year, selectRegion1, selectRegion2

def menuUnion():
    choice = ["Food Prices and Obesity Rates", "Food Prices and Population", "Population and Obesity Rates"]
    graph = st.selectbox('Select your comparison graph', choice)
    st.write("You selected:", graph)

    return graph