import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "penguin_logo.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "penguins.csv")

st.title(":red[Penguin] :green[Species]:fire:")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

Species = st.selectbox("Select the species:", df['species'].unique())

col1, col2, col3 = st.columns(3)

fig_1 = px.histogram(df[df['species'] == Species], x="bill_length_mm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['species'] == Species], y="bill_length_mm")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.scatter(df[df['species'] == Species], y="bill_length_mm")
col3.plotly_chart(fig_3, use_container_width=True)