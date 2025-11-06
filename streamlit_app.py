import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Hello world!')

st.info('This app builds machine learning models')

with st.expander ('Data'):
  st.write('**raw data**')
  df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df

st.write('**x**')
X=df.drop('species',axis=1)
X
st.write('**y**')
y=df.species
y
with st.expander ('Data visualization'):
  
  st.scatter_chart(data=df,X="bill_length_mm", y="body_mass_g", color= "species") 
