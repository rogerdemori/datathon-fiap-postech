# Importação das bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Definir título da página
st.title('Dados tratados')

# Função para a leitura da base de dados
@st.cache_resource
def read_csv_file(file):
    return pd.read_csv(file)

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Carregar os dados
dados = read_csv_file('Dataset/df_pm_target.csv')

# Exibir os dados em uma tabela
st.write(dados)

st.image(load_img('Imagens/Correlação_de_Dados_Passos_Magicos.png'))