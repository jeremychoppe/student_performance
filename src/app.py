# Standard imports
import pandas as pd

#plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

import streamlit as st

st.title("Student Performance")

df = pd.read_csv("../data/student_data2.csv", sep=',')

# Basic set-up of the page:

st.header("Student Performance")

st.subheader('Improvability score vs. Final grade')

fig = go.Figure(data=[
    go.Scatter(
        y=df["ImprovabilityScore"], x=df['FinalGrade'], 
        mode="markers",
        text=df['StudentID'],
        hovertemplate=
            "<b>Student ID: %{text}</b><br><br>" +
            "Improvability score: %{y:.1f}<br>" +
            "Final grade: %{x:.f}<br>" 
    )
])
fig.update_layout(
    title={"text": "Student Performance", "font": {"size": 24}},
    xaxis={"title": {"text": "Final grade", "font": {"size": 16}}},
    yaxis={"title": {"text": "Improvability score", "font": {"size": 16}}}
)

st.plotly_chart(fig)


