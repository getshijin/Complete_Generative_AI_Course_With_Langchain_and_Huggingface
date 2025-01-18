import streamlit as st
import pandas as pd
import numpy as np


st.title('Streamlit text Input')

name =st.text_input('Enter your name:')

age =st.slider('select your age:', 0,100,25)

st.write(f'your age is {age}.')

options =['python', 'C++', 'Java']
choice = st.selectbox('Choose your option ', options)
st.write(f'Your choice is {choice}')

if name:
    st.write(f'hello, {name.upper()}')

data ={
    'Name': ['Shijin', 'Anju','Ram' ,'Raavan'],
    'Age': [28,24,4,5],
    'City': ['TVM','KOC','KZM','USA']
}

df= pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)

uploaded_file =st.file_uploader('choose a csv file',type='csv')

if uploaded_file is not None:
    df =pd.read_csv(uploaded_file)
    st.write(df)