import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Dashboard Teste Streamlit",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Painel de Teste - Streamlit")
st.write("Se você está vendo essa página, o Streamlit está funcionando corretamente!")

# Criando dados fictícios
np.random.seed(42)

dados = pd.DataFrame({
    "Mês": [
        "Jan", "Fev", "Mar", "Abr",
        "Mai", "Jun", "Jul", "Ago"
    ],
    "Vendas": np.random.randint(100, 500, 8),
    "Clientes": np.random.randint(50, 300, 8),
    "Satisfação": np.random.uniform(7, 10, 8).round(1)
})


# Sidebar
st.sidebar.header("Filtros")

mes_selecionado = st.sidebar.multiselect(
    "Selecione os meses",
    dados["Mês"],
    default=dados["Mês"]
)

dados_filtrados = dados[
    dados["Mês"].isin(mes_selecionado)
]


# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de Vendas",
        dados_filtrados["Vendas"].sum()
    )

with col2:
    st.metric(
        "Total de Clientes",
        dados_filtrados["Clientes"].sum()
    )

with col3:
    st.metric(
        "Média de Satisfação",
        f'{dados_filtrados["Satisfação"].mean():.1f}'
    )


# Tabela
st.subheader("📋 Dados")

st.dataframe(
    dados_filtrados,
    use_container_width=True
)


# Gráfico vendas
st.subheader("📈 Evolução das Vendas")

grafico_vendas = px.line(
    dados_filtrados,
    x="Mês",
    y="Vendas",
    markers=True
)

st.plotly_chart(
    grafico_vendas,
    use_container_width=True
)


# Gráfico clientes
st.subheader("👥 Clientes por mês")

grafico_clientes = px.bar(
    dados_filtrados,
    x="Mês",
    y="Clientes"
)

st.plotly_chart(
    grafico_clientes,
    use_container_width=True
)