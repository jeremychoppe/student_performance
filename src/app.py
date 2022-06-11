# Standard imports
import pandas as pd

#plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

import streamlit as st

st.title("Student Performance")

df = pd.read_csv("../data/student_data.csv", sep=',')

# Basic set-up of the page:
# First the checkbox to show the data frame
if st.sidebar.checkbox('Show dataframe'):
    st.header("dataframe")
    st.dataframe(df.head())

st.header("Highway Fuel Efficiency")
years = ["All"]+sorted(pd.unique(df['year']))
year = st.sidebar.selectbox("choose a Year", years)   # Here the selection of the year.
car_classes = ['All'] + sorted(pd.unique(df['class']))
car_class = st.sidebar.selectbox("choose a Class", car_classes)  # and the selection of the class.

show_means = st.sidebar.radio(
    label='Show Class Means', options=['Yes', 'No'])

st.subheader(f'Fuel efficiency vs. engine displacement for {year}')

def mpg_plotly(year, car_class, show_means):
    if year == 'All':
        group = df
    else:
        group = df[df['year'] == year]
    if car_class != 'All':
        group = group[group['class'] == car_class]
    fig = px.scatter(group, x='displ', y='hwy', opacity=0.5, range_x=[1, 8], range_y=[10, 50])
    if show_means == "Yes":
        means = df.groupby('class').mean().reset_index()
        fig = px.scatter(means, x='displ', y='hwy', opacity=0.5, color='class', range_x=[1, 8], range_y=[10, 50])
        fig.add_trace(go.Scatter(x=group['displ'], y=group['hwy'], mode='markers', name=f'{year}_{car_class}',
                                 opacity=0.5, marker=dict(color="RoyalBlue")))
    return fig
  

st.plotly_chart(mpg_plotly(year, car_class, show_means))


