import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title("Scatter Plot on Tips data Set")
st.header("Overview of Data set")

df=sns.load_dataset("tips")
st.write(df.head())

st.subheader("Checking Columns")

st.write(df.columns)

st.subheader("Scatter plot on the basis of Days")

day_option = df['day'].unique().tolist()

Day= st.selectbox('On which day you want to check?', day_option,0)

st.header('Scatter Plot')
fig = px.scatter(df,x="tip",y='total_bill',size='total_bill',color='sex',hover_name='time', size_max=17,range_x=[0,5],range_y=[0,40]
, animation_frame='day',animation_group='smoker' )
st.write(fig)
