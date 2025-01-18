import streamlit as st
import pandas as pd
import numpy as np

###Tittile of the application 
st.title('Hello Stream lit')

##Display a simple text
st.write('this is a simple text')

## create a df

df = pd.DataFrame({
    'Col1':[1,2,3,4],
    'col2':[5,6,7,8]
})

#Display DF
st.write('Here is my DF')
st.write(df)

##Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)