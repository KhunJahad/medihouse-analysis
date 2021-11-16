import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image

def add_image(name,caption):
	path = 'Images/'+name
	image = Image.open(path)
	st.image(image, caption=caption,width=500 )

def show_home_page():
	st.title('Medihouse Adherence Dashboard')
	st.markdown(r'Medication adherence usually refers to patients taking their prescribed medications at required frequency (e.g: twice daily and duration (e.g : 3 months) without any omission of doses')
	add_image('correlation_adherence.jfif','Variation of Adherence with other parameter based on data provided')

def show_age_page():
	st.title("Age vs Adherence")
	add_image('age_pie_chart.jpeg','')
	add_image('age_bar_graph.jpeg','')

def show_marital_page():
	st.title("Marital vs Adherence")
	add_image('marital_pie_chart.jpeg','')
	add_image('marital_bar_graph.jpeg','')

def show_race_page():
	st.title("Race vs Adherence")
	add_image('race_pie_chart.jpeg','')
	add_image('race_bar_graph.jpeg','')

def show_ethnicity_page():
	st.title("Ethencity vs Adherence")
	add_image('ethnicity_pie_chart.jpeg','')
	add_image('ethnicity_bar_graph.jpeg','')

def show_gender_page():
	st.title("Gender vs Adherence")
	add_image('gender_pie_chart.jpeg','')
	add_image('gender_bar_graph.jpeg','')

def show_county_page():
	st.title("County vs Adherence")
	add_image('county_pie_chart.jpeg','')
	add_image('county_bar_graph.jpeg','')

st.sidebar.title('NAVIGATION PANEL')
st.sidebar.markdown('')
st.sidebar.markdown('Select of the following:')
parameter = ('Home','Age','Marital','Race','Ethnicity','Gender','County')
select = st.sidebar.radio('',parameter)
	
if select=='Home':
	show_home_page()
if select=='Age':
	show_age_page()

if select=='Marital':
	show_marital_page()

if select=='Race':
	show_race_page()

if select=='Ethnicity':
	show_ethnicity_page()

if select=='Gender':
	show_gender_page()

if select=='County':
	show_county_page()