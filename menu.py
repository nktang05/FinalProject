import streamlit as st

# method to get user grocery requests
def menugrocery():
    # list of possible regions
    region = ["Northeast", "West", "South", "Midwest"]

    # get use region
    selectRegion = st.selectbox(
        'Select a region?',
        region, placeholder = "Northeast")
    st.write("Your chosen region", selectRegion)

    # get user food
    selectFood = st.text_input('Select Food Type', 'beef')
    st.write("Your chosen food item is", selectFood)

    selectFood.strip()

    return selectFood, selectRegion

# method to get user obesity requests
def menuObesity():
    # list of year options
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

    # get user year 1
    selectYear1 = st.selectbox(
        'Select a year to compare?',
        years)
    st.write("Your chosen year", selectYear1)

    # get user year 2
    selectYear2 = st.selectbox(
        'Select a second year to compare?',
        years)
    st.write("Your chosen year", selectYear2)
    
    return selectYear1, selectYear2

# mthod to get population user input
def menuPop():
    # valid year options
    year = st.slider('Select a range of years',
    2013, 2023, (2013, 2023))
    # valid region options
    region = ["Northeast", "West", "South", "Midwest", 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'National', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
   
    # ger user region 1
    selectRegion1 = st.selectbox('Select the first region or state', region)
    st.write("You selected:", selectRegion1)
    # get user  region 2
    selectRegion2 = st.selectbox('Select the second region or state', region)
    st.write("You selected:", selectRegion2)

    return year, selectRegion1, selectRegion2

# method to get obesity user input
def menuObestiyRegion():
    # valuid year options
    year = st.slider('Select a range of years',
    2011, 2022, (2011, 2022))

    # valid region population
    region = ["Northeast", "West", "South", "Midwest", 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'National', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
   
    # get user region 1
    selectRegion1 = st.selectbox('Select the first region or state', region)
    st.write("You selected:", selectRegion1)

    # get user region 2
    selectRegion2 = st.selectbox('Select the second region or state', region)
    st.write("You selected:", selectRegion2)

    return year, selectRegion1, selectRegion2

# method to get combined graph user input
def menuUnion():
    # optional choices
    choice = ["Food Prices and Obesity Rates", "Food Prices and Population", "Population and Obesity Rates"]
    # let user pick graph
    graph = st.selectbox('Select your comparison graph', choice)
    st.write("You selected:", graph)

    return graph