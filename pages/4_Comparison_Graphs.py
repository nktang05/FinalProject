import streamlit as st
import numpy as np
import union

# set titles and headers
st.set_page_config(page_title="Union Graphs", page_icon="📈")
st.markdown("# Union Graphs")

# explanation of data
st.write(
    """This visualization tool helps show if there is any possible correlation between any of the three variables: population, obesity rates, and food prices. Pick the option of which variables you would like to compare. Pick your choice of regions and food choices."""
)

# run method to get graph
union.unionGraphs()