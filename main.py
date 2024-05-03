import streamlit as st

# method to load all data into the database. I uploaded it already so I am no longer running it and running it takes a long time
#loadData.loadAllData()

# set text headers and titles
st.set_page_config(
    page_title="DSCI510-FinalProject",
    page_icon="👋",
)

st.write("# DSCI510 Final Project- Nicole Tang")

st.write("""This site allows you to see if there are any possible correlations between obesity rates, population, and prices of food. These datasets can be sorted by state, region, and year. The following pages allow you to see individual visualizations of 
         obesity rates, population, and prices of food and you can see how they vary by state and year. Then you can see if how they correlate with each other and see graphs of the following data. Major gotchas include all three variables on average consistantly increasing over the years.
         """)
