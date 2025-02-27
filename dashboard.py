import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#visão mensal
#checar dados da planilha

df = pd.read_csv("empresa_invoicesnew.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]
df_filtered

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)