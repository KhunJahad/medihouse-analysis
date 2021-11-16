import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt



st.title('Medihouse Adherance Dashboard')
st.markdown('The dashboard will visualize the Adherance Situation')
st.sidebar.title('Analysis')
st.sidebar.markdown('Select a Parameter:')

parameter = ('Age','County','Ethencity','Race','Gender','City')
select = st.sidebar.radio('',parameter)