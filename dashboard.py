import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Faturamento", layout="wide")

# Carregar dados do CSV
df = pd.read_csv("empresa_invoicesnew.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")
df["Month"] = df["Date"].dt.strftime("%Y-%m")


df["Total"] = pd.to_numeric(df["Total"], errors="coerce")

# Sidebar
st.sidebar.header("Filtros")
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())

# Filtrar dados pelo mês selecionado
df_filtered = df[df["Month"] == month]

# Indicadores principais
st.markdown("### Resumo do Faturamento")
total_faturamento = df_filtered["Total"].sum()
st.metric(label="Faturamento Total", value=f"R$ {total_faturamento:,.2f}")

# Layout dos gráficos
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Gráficos
fig_date = px.bar(df_filtered, x="Date", y="Total", title="Faturamento por Dia", color="Total", color_continuous_scale="Blues")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Product Line", y="Total", title="Faturamento por Tipo de Produto", color="Total", color_continuous_scale="Viridis")
col2.plotly_chart(fig_prod, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por Tipo de Pagamento", color_discrete_sequence=px.colors.qualitative.Pastel)
col3.plotly_chart(fig_kind, use_container_width=True)

fig_scatter = px.scatter(df_filtered, x="Date", y="Total", size="Total", color="Total", title="Tendência de Faturamento", color_continuous_scale="Sunset")
col4.plotly_chart(fig_scatter, use_container_width=True)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com ❤️")
