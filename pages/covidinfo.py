
import streamlit as st
import os
import pandas as pd
import matplotlib as plt
import plotly.express as px
import plotly.figure_factory as ff
st.set_page_config(layout = "wide")
st.title(":violet[**_COVID_19 Information  Worldwide_**]")
st.markdown(":red[Covid_19 Dashboard]")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "covid_data.csv")



df=pd.read_csv(DATA_PATH)
df.head(20)
df.dropna()
st.dataframe(df)


page = st.sidebar.selectbox(':red[Select page]',['Total Cses and Total Deaths in each country','Recovered and active cases in each country'])
if page == 'Total Cses and Total Deaths in each country':
  clist = df['Country'].unique()
  country = st.selectbox(":red[Select a country]",clist)
  col1, col2 = st.columns(2)
  fig = px.line(df[df['Country'] == country], 
    x = "Country", y = "Total Cases",title = "Total number of  Cases in each country]")
 
  col1.plotly_chart(fig,use_container_width = True)
  fig = px.line(df[df['Country'] == country], 
    x = "Country", y = "Total Deaths",title = "Total number of Deaths im each country")
  
  col2.plotly_chart(fig,use_container_width = True)

else:

  country = df['Country'].unique()
 
  st.markdown(":red[_**Total recovered and active cases in each country **_]")

  col1,col2 = st.columns(2)
  fig = px.line(df[df['Country'] == country], 
    x = "Country", y = "Total Recovered",
    title = "Total Recoveries in each country",)
  
  col1.plotly_chart(fig)
  fig = px.line(df[df['Country'] == country], 
    x = "Country", y = "Active Cases",
    title = "Active Cases in each country")
  
  col2.plotly_chart(fig, use_container_width = True)