import streamlit as st
import pandas as pd
from modules.data_prep import DataImport


st.title("⭐️ Worthy of Preservation")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title('My title')
st.subheader('My sub')
st.button('Hit me')

st.markdown("## 🛠️ What is the TOP Skill for Data Analysts?!?")

#get the dataframe
app_data = DataImport().fetch_and_clean_data()

#get state names
states = DataImport().get_state_names()

col1, col2 = st.columns(2)

with col1:
    col1.write('Column1')
    select_state = st.selectbox('Select State', states)

with col2:
    col2.write('Column2')

st.dataframe(data=app_data[:15], width=500, height=500)

st.divider()
