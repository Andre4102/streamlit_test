import pandas as pd
import streamlit as st

st.title('The Beatles')

df = pd.read_csv("https://github.com/Andre4102/streamlit_test/blob/main/test.csv", delimiter = ";")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)