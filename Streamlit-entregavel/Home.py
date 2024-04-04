import matplotlib.pyplot as plt
import streamlit as st
from st_pages import show_pages_from_config
from pytube import YouTube

st.set_page_config(
    page_title="DATATHON | FIAP + ALURA | FASE 4",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "Projeto de análise de Impacto Socioeducacional das crianças de Embu-Guarçu (SP) através da Associação Passos Mágicos."
    }
)

@st.cache_data
def load_img(img):
    return plt.imread(img)

st.title('A ASSOCIAÇÃO PASSOS MÁGICOS')

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

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

st.image(load_img('Imagens/passos_magicos.png'))

# Função para baixar vídeo do YouTube
def download_video(youtube_url, save_path):
    try:
        yt = YouTube(youtube_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path, filename='video')
        return True
    except Exception as e:
        st.error(f"Erro ao baixar vídeo: {e}")
        return False

# URL do vídeo do YouTube
youtube_url = "https://www.youtube.com/watch?app=desktop&v=6ssGeZgqIh4"

# Pasta para salvar o vídeo
save_path = "videos/"

# Baixar o vídeo
if download_video(youtube_url, save_path):
    st.video(f"{save_path}video.mp4")


show_pages_from_config()

url = 'https://passosmagicos.org.br/'
link = 'Associação Passos Mágicos'

'''

A Associação Passos Mágicos é uma instituição com mais de três décadas de existência, dedicada a promover mudanças positivas na vida de crianças e jovens de famílias menos privilegiadas. Seu compromisso central é criar oportunidades equitativas, com foco especial em educação, ações sociais e apoio psicopedagógico.

Criada por Michelle Flues e Dimitri Ivanoff, sua jornada começou nos orfanatos de Embu-Guaçu. Desde então, a Associação tem trabalhado incansavelmente para transformar sua comunidade em um lugar onde todos, independentemente de sua origem, possam prosperar.

Atualmente, a Passos Mágicos oferece suporte abrangente, desde a infância até o final do Ensino Médio. Isso inclui aulas extras em disciplinas como português, matemática e inglês, além de oportunidades de estudo em escolas particulares e intercâmbios. Além disso, a organização fornece apoio emocional e promove atividades culturais e comunitárias, visando moldar não apenas estudantes bem-sucedidos, mas também cidadãos conscientes.

O sucesso da Associação é resultado do comprometimento de seus colaboradores, que se dedicam com amor e cuidado às crianças, e do apoio de patrocinadores que reconhecem o valor vital da Associação para a comunidade. Portanto, é essencial para a Passos Mágicos avaliar o impacto de suas iniciativas, garantindo assim que possa expandir seus programas e alcançar um número ainda maior de beneficiados.

'''

st.divider()

'''

## Contexto e oportunidade

Após interação com os fundadores, corpo docente e profissionais de suporte foi identificado algumas oportunidades de melhoria dos processos da ONG:

_ Input ou transferência manual de dados físicos - Avaliação de alunos

_ Consolidação de base de dados de forma manual - Processo de consolidação de indicadores

_ Competição de recursos humanos com competência técnica para atividades mais críticas

'''

st.divider()

'''

## Proposta da Consultoria DMGB Vintage Analytics

_ Apresentar uma revisão de processos para criar uma cultura de dados na ONG

_ Somada a inclusão de ferramentas de fácil manutenção para consolidação de dados e indicadores de alta importância

_ Adicionalmente será apresentado uma ferramenta para os gestores conseguirem extrair insights.

O objetivo principal é uma solução simples, de manutenção intuitiva que estabeleça um novo patamar em relação a dados


'''

st.divider()

'''

## Explore outras análises

Para mais dados, DataFrames e análises detalhadas, visite a [página do GitHub](https://github.com/rogerdemori/datathon-fiap-postech) do projeto. Lá você encontrará uma variedade de informações adicionais para expandir sua compreensão.

'''

st.divider()

'''

## Descubra mais sobre o projeto

[passosmagicos.org.br](https://passosmagicos.org.br/): Acesse o site oficial da Associação Passos Mágicos para obter mais informações sobre suas iniciativas e como você pode ajudar.

[cidades.ibge.gov.br](https://cidades.ibge.gov.br/brasil/sp/embu-guacu/panorama): Confira o censo do IBGE para o município de Embu-Guaçu e obtenha dados relevantes sobre a região.

[servicodados.ibge.gov.br](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3): Explore a API de dados agregados do IBGE para acessar informações estatísticas detalhadas sobre diversas áreas.


'''