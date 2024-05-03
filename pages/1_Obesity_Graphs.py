import streamlit as st
import time
import numpy as np
import obesity
import menu

# set titles and headers
st.set_page_config(page_title="Obesity Graph", page_icon="📈")
st.markdown("# Obesity Groph")

# explanation of data
st.write(
    """This visualization shows obesity rates across the US over time. Choose years that you want to compare."""
)

# run method to show obesity nationwide over time
# allow user to pick which years to compare
year1, year2 = menu.menuObesity()
obesity.obesityTable(year1, year2)

# explanation of data
st.write(
    """This visualization shows obesity rates of different regions. Pick the year and which regions you want to compare."""
)

# run method to show differences in regions or stats
# allow people to pick a year and pick regions to compare
year, region1, region2 = menu.menuObestiyRegion()
obesity.obesityRegionCompare(region1, region2, year[0], year[1])