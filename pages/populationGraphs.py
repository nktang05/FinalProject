import streamlit as st
import time
import numpy as np
import population
import menu

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

year, location1, location2 = menu.menuPop()
population.avgPop(location1, location2, year[0], year[1])

progress_bar = st.sidebar.progress(0)