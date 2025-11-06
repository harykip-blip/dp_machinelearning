import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Hello world!')

st.info('This app builds machine learning models')
df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
df

