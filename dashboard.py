import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("empresa_invoicesnew.csv", sep=";", decimal=",")
df