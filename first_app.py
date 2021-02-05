import streamlit as st
import time
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
np.random.seed(0)

# streamlit run first_app.py

dataframe = np.random.randn(5, 10)
st.dataframe(dataframe)

dataframe = pd.DataFrame(
    np.random.randn(5, 10),
    columns=('col %d' % i for i in range(10)))

st.dataframe(dataframe.style.highlight_max(axis=0))

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

dataframe = pd.DataFrame(
    np.random.randn(x, 5),
    columns=('col %d' % i for i in range(5)))
st.table(dataframe)


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.sidebar.beta_columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.sidebar.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.sidebar.write(f"You are in {chosen} house!")

@st.cache(suppress_st_warning=True)
def expensive_computation(a, b):
    st.sidebar.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    time.sleep(2)  # This makes the function take 2s to run
    return a * b + 1  # 👈 Added a +1 at the end here

a = 2
b = 210
res = expensive_computation(a, b)

st.sidebar.write("Result:", res)