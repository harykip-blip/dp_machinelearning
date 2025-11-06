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
  
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species') 

# data preparation
with st.sidebar:
  st.header('input features')
  # "species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex"
island= st.selectbox('island'('Biscoe','Dream',Torgersen'))
gender=st.selectbox('Gender',('male','female'))
bill_length_mm= st.slider('bill length (mm)',32.1,59.6,43.9) 
              
