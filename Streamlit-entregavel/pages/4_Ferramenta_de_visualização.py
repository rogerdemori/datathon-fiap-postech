# libs gráficas

import matplotlib.pyplot as plt

# Streamlit

import streamlit as st

st.set_page_config(layout="wide",page_icon="🔍")

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Código para alinhar imagens expandidas no centro da tela e justificar textos
st.markdown(
    """
    <style>
        body {text-align: justify}
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

# Alterando cor dos hyperlinks
st.markdown(
   """
    <style>
     a:link {
       color: #a277ff;
       background-color: transparent;
       text-decoration: none;
     }

     a:visited {
        color: #a277ff;
        background-color: transparent;
        text-decoration: none;
    }

     a:hover {
        color: #a277ff;
        background-color: transparent;
        text-decoration: none;
    }

    a:active {
        color: #a277ff;
        background-color: transparent;
        text-decoration: none;
    }
    </style>
    """ , unsafe_allow_html=True
)

# Definir título da página
st.title('Ferramenta de visualização | Análise no Power BI')

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

st.image(load_img('Imagens/PowerBI.jpg'))

'''
## Você pode conferir o projeto de análise no Power BI nesse [repositório do Github](https://github.com/fegastal/PowerBI_Analise_PosTech_Datathon). Basta fazer o download e importar no ambiente. Contudo, você também pode conferir logo abaixo!
'''

col1, col2 = st.columns([0.035,0.965])
with col2:

    #Dashboard_Power_BI = '<p align="center"><iframe title="datathon_alura_pos_tech" style="width:94.1%; height:1700px" src="https://app.powerbi.com/groups/me/reports/0b826257-171f-4ba6-8696-27bf5226b946/ReportSection?experience=power-bi" frameborder="0" allowFullScreen="true"></iframe></p>'
    Dashboard_Power_BI = '<p align="center"><iframe title="Dashboard_Datathon" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=0b826257-171f-4ba6-8696-27bf5226b946&autoAuth=true&ctid=6f683370-0bff-4fa5-a74a-b943ff7d8e57" frameborder="0" allowFullScreen="true"></iframe></p>'
    st.divider()

    with st.container():
        st.markdown(Dashboard_Power_BI, unsafe_allow_html=True)