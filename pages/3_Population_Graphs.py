import streamlit as st
import time
import numpy as np
import population
import menu

# set titles and headers
st.set_page_config(page_title="Population Graphs", page_icon="📈")
st.markdown("# Population Graphs")

# explanation of data
st.write(
    """This is a visualization of population difference across two locations. Choose two locations to compare and a year."""
)

# get user year and locations
year, location1, location2 = menu.menuPop()
# graph the population across regions
population.avgPop(location1, location2, year[0], year[1])

