import streamlit as st
import time
import numpy as np
import obesity
import menu

st.set_page_config(page_title="Obesity Demo", page_icon="📈")

st.markdown("# Obestiy Demo")
#st.sidebar.header("Obesity Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

year1, year2 = menu.menuObesity()
obesity.obesityTable(year1, year2)

st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

year, region1, region2 = menu.menuObestiyRegion()
obesity.obesityRegionCompare(region1, region2, year[0], year[1])