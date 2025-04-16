import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Análise de Combustíveis", layout="wide")

# Título
st.title("⛽ Análise de Vendas de Combustíveis (Brasil - ANP)")

# Carregando os dados
@st.cache_data
def load_data():
    df = pd.read_csv("data/vendas-combustivel.csv", sep=';')
    df['VENDAS'] = df['VENDAS'].str.replace(',', '.').astype(float)
    
    mes_map = {
        'JAN': '01', 'FEV': '02', 'MAR': '03', 'ABR': '04',
        'MAI': '05', 'JUN': '06', 'JUL': '07', 'AGO': '08',
        'SET': '09', 'OUT': '10', 'NOV': '11', 'DEZ': '12'
    }
    df['MÊS_NUM'] = df['MÊS'].map(mes_map)
    df['DATA'] = pd.to_datetime(df['ANO'].astype(str) + '-' + df['MÊS_NUM'])
    return df

df = load_data()

# Sidebar para seleção de combustível
produtos = df['PRODUTO'].unique()
combustivel_escolhido = st.sidebar.selectbox("Escolha o tipo de combustível:", sorted(produtos))

# Filtrar por combustível
df_filtrado = df[df['PRODUTO'] == combustivel_escolhido]

# Agregar por data
vendas_mensais = df_filtrado.groupby('DATA')['VENDAS'].sum().reset_index()

# Gráfico
st.subheader(f"📈 Consumo Mensal de {combustivel_escolhido} no Brasil")
plt.figure(figsize=(12, 5))
sns.lineplot(data=vendas_mensais, x='DATA', y='VENDAS', color='royalblue')
plt.title(f"Vendas de {combustivel_escolhido} (m³)")
plt.xlabel("Data")
plt.ylabel("Volume (m³)")
plt.xticks(rotation=45)
st.pyplot(plt.gcf())
