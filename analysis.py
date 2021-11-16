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
	st.markdown('We analyzed the data given by UGH Optum in order to deduce what patients are prone to non-adherence,what are their specific traits and relationship between them')
	st.markdown('First we analysed the data and came with the algorthim to classify as non-adherence and Adherence type primarily on the basis of medication count and frequency pattern of different patients over the years.')
	st.markdown('Then based on this we concluded the following parameters are most correlated to having Adherence:')
	st.markdown('• Age')
	st.markdown('• Marital Status')
	st.markdown('• Race')
	st.markdown('• Ethnicity')
	st.markdown('• County region')
	add_image('correlation_adherence.jfif','Variation of Adherence with other parameter based on data provided')
	st.markdown('The above figure depicts the correlation of these parameters with each other')
	st.markdown('We further analysed these parameters to fine details and that can be accessed via side-bar')

def show_age_page():
	st.title("Age vs Adherence")
	st.markdown('Different age group resulted in different level of Adherence. When we analysed the given data we found that Adherence for the people aged 45 contributed the most , followed by age group of 18-45 and then <18')
	add_image('age_pie_chart.jpeg','')
	st.markdown('Then we analysed the finer details as distribution of Adherence and non-adherence among a particular age group.')
	st.markdown('We found out that level of Adherence in elderly is more with more medication and hospital visits as compared to other age group. ')
	add_image('age_bar_graph.jpeg','')

def show_marital_page():
	st.title("Marital vs Adherence")
	st.markdown('Who knew being married can play a such a vital role in Adherence?')
	st.markdown('We broke down the the Adherence level in single and married individuals. The results are as follow:')
	add_image('marital_pie_chart.jpeg','')
	st.markdown('On the surface it looks like single individuals have less contribution to the overall Adherence level.')
	st.markdown('But the relative Adherence vs non-adherence level tells us that the non-adherence in singles are more than that of adherence one in the same bracket.')
	add_image('marital_bar_graph.jpeg','')

def show_race_page():
	st.title("Race vs Adherence")
	st.markdown('Different race have different impact and culture in society, during our analysis we found out that certain races contribute more to the non-adherence than others.')
	st.markdown('The breakdown of non-adherence level from these different races in contribution ot the total non-adherence was observed as follow : ')
	add_image('race_pie_chart.jpeg','')
	st.markdown('On the surface , white people contributes the most , but if we dive into the non-adherence vs adherence comparsion race-wise , we can conclude that native , black and others have more contribution per person wise followed by asian and white race people')
	add_image('race_bar_graph.jpeg','')

def show_ethnicity_page():
	st.title("Ethnicity vs Adherence")
	st.markdown('When we tried to dive into the adherence relationship with ethnicity , we found something interesting')
	add_image('ethnicity_pie_chart.jpeg','')
	st.markdown('The contribution of non-hispanic is more than hispanic but that is due to large sample of non-hispanic in the database, we followed this with internal division of non-adherence in these ethnics group , and they had a very small margin within them. The graph of the same is : ')
	add_image('ethnicity_bar_graph.jpeg','')

def show_gender_page():
	st.title("Gender vs Adherence")
	st.markdown('The Gender and non-adherence relationship is simple is it gets, they have somewhat equal contribution in the non-adherence.')
	add_image('gender_pie_chart.jpeg','')
	st.markdown('Women edging only by a bit in term of males but thats due to more female sample, and the rate of non-adherence in both demographic remaining almost same.')
	add_image('gender_bar_graph.jpeg','')

def show_county_page():
	st.title("County vs Adherence")
	st.markdown('The environment and region where a person lives can have significant effect on adherence practices like rural and urban regions have different adherence levels.')
	st.markdown('When we broke down the county regions based on there contribution to the adherence , we found some counties contribute more than others.')
	add_image('county_pie_chart.jpeg','')
	st.markdown('On further breakdownm, we arrived at the same conclusion , the pie chart of the same is shown below :')
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