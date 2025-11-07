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
  


with st.sidebar:
  st.header('input features')
 
  island= st.selectbox('island',('Biscoe','Dream','Torgersen'))
  gender=st.selectbox('Gender',('male','female'))
  bill_length_mm= st.slider('bill length (mm)',32.1,59.6,43.9) 
  bill_depth_mm= st.slider('bill depth (mm)',13.1,21.5,17.3)
  flipper_length_mm= st.slider('flipper length (mm)',172.0,231.0,201.0)
  body_mass_g= st.slider('body mass(g)',2700.0,6300.0,4207.0)

  st.header("Your Selected Inputs")
  st.write(f"**Island:** {island}")
  st.write(f"**Gender:** {gender}")
  st.write(f"**Bill length:** {bill_length_mm} mm")
  st.write(f"**Bill depth:** {bill_depth_mm} mm")
  st.write(f"**flipper length: **{flipper_length_mm} mm")
  st.write(f"**body mass:** {body_mass_g} g")
              


