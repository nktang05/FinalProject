import streamlit as st
import numpy as np
import union


st.set_page_config(page_title="Union Demo", page_icon="📈")

st.markdown("# Union Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)
union.unionGraphs()