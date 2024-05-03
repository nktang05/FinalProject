import streamlit as st
import numpy as np

# set titles and headers
st.set_page_config(page_title="Short Question Responses", page_icon="📈")

st.markdown("# Short Question Responses")

# answer short answer questions
st.write(
    """Overall findings are that does appeat to be positive correlations between food prices and obesity rates, population and obesity rates, and food prices and population. The data looks the best when the food data lines up year wise with the rest of the data. However, sometimes the food data has data from the 1990's 
    but no other data in my database is from them. All variables for the most part increased over time so population has increased, food has increased, and obesity rates have also increased. Living is getting more expensive.""" )

st.write(
"**What did you set out to study?  (i.e. what was the point of your project?  This should be close to your Milestone 1 assignment, but if you switched gears or changed things, note it here.**"
)
st.write(
    """ I am hoping to uncover patterns in grocery prices and population size over time, and
see if they correlate with obesity rates. If groceries are more expensive, will rates of
obesity increase? Or, is there no correlation and prices of healthy vs unhealthy foods
are unrelated to obesity which means there's another main cause of obesity other than
accessibility to healthier food options in the grocery store. Maybe more physical activity
needs to be promoted and that could be seen in pre and post pandemic years. I also
want to see if changes in the population have an affect on the prices of food. Maybe
there has been no drastic change in the population yet the prices still increased. Overall findings show that all three have increased overtime. """
)

st.write(
"**What did you Discover/what were your conclusions (i.e. what were your findings?  Were your original assumptions confirmed, etc.?)**"
)
st.write(
    " My original assumptions of them being correlated was confirmed. All appear to be positively correlated and increase over time. There are some outlier year and sometimes there is less data points than prefered. However, more research and statistical analysis is necessary to dive deeper and learn more. "
)

st.write(
    "**What difficulties did you have in completing the project?**"
)
st.write(
    """ The hardest part was learning the different software/libraries whether it was streamlit, github, or vs code after using juypyter all year . There was definietly a learning curve. It was also hard to find an api that had data that was easy access and free. I have also never learned 
    html so the tags and webscraping was a bit difficult.  """
)

st.write(
    "**What skills did you wish you had while you were doing the project?**"
)
st.write(
    """I wish I new a little more html because that would have made understanding tags and webscraping easier. I also wish I new more about streamlit because I hadn't used that before either and learning new software always has a learning curve as it takes a while to understand how it
    works and what it is capable of."""
)

st.write(
    "**What would you do “next” to expand or augment the project?**"
)

st.write(
    "To expand my project I could perform more statistical analysis or add more data sources and variables. Another dataset that could be added is the cost of living, cost of housing, or rates of phyical activity."
)


