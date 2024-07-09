import streamlit as st
import pandas as pd
from data_prep import DataImport


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.button('Hit me')

app_data = DataImport().fetch_and_clean_data()