#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import math
import streamlit as st

# Definir título da página
st.title('Future Engineering PM')

# In[ ]:


pm_2020 = pd.read_csv('Dataset/pm_2020.csv')
pm_2021 = pd.read_csv('Dataset/pm_2021.csv')
pm_2022 = pd.read_csv('Dataset/pm_2022.csv')


# In[ ]:


st.dataframe(pm_2020)


# In[ ]:


st.dataframe(pm_2021)


# In[ ]:


st.dataframe(pm_2022)

''' ## Criação coluna ANOS_PM_21_22 '''


# In[14]:


#Tratamento da Coluna 2022
values_anos_pm_2022 = 2022 - pm_2022['ANO_INGRESSO_2022']
pm_2022.insert(2, 'ANOS_PM_2022', values_anos_pm_2022)
st.table(pm_2022.head())

''' # 2021 '''

# In[15]:


st.table(pm_2021.head())


# In[16]:


''' # Gerando coluna a partir dos datasets 2020 e 2022 '''

pm_anos_2021 = pm_2021.merge(pm_2020[['NOME','ANOS_PM_2020']], on='NOME', how='left')
print(pm_anos_2021.isna().sum())
pm_anos_2021 = pm_anos_2021.merge(pm_2022[['NOME','ANOS_PM_2022']], on="NOME", how='left')
print(pm_anos_2021.isna().sum())


# In[19]:


def calcular_anos_2020(x):
    if not math.isnan(x):
        return int(x + 1)
    else:
        return None

def calcular_anos_2022(x):
    if not math.isnan(x):
        return int(x - 1)
    else:
        return None

def calcular_anos(x, y):
    if not math.isnan(x):
        return x
    else:
        if not math.isnan(y):
            return y
        else:
            return None


# In[22]:


''' # Função de Calculo Anos de 2020 para 2021 '''
pm_anos_2021['ANOS_PM_2021_a'] = pm_anos_2021['ANOS_PM_2020'].apply(calcular_anos_2020)


# In[23]:


''' # Função de Calculo Anos de 2022 para 2021 '''
pm_anos_2021['ANOS_PM_2021_b'] = pm_anos_2021['ANOS_PM_2022'].apply(calcular_anos_2022)


# In[24]:


''' # Função de Calculo Anos Final '''
pm_anos_2021['ANOS_PM_2021'] = pm_anos_2021.apply(lambda row: calcular_anos(row['ANOS_PM_2021_a'], row['ANOS_PM_2021_b']), axis=1)


# In[25]:


''' # Codigo para tratar alunos novos '''
pm_anos_2021.loc[pm_anos_2021['SINALIZADOR_INGRESSANTE_2021'] == 'Ingressante', 'ANOS_PM_2021'] = 0


# In[26]:


''' # Dados nulos '''
pm_anos_2021['ANOS_PM_2021'].isna().sum()


# In[27]:


''' # Tratamento dos dados com mediana '''
pm_anos_2021['ANOS_PM_2021'].fillna(pm_anos_2021['ANOS_PM_2021'].median(), inplace=True)


# In[28]:


''' # Insert coluna ANOS_PM_2021 '''
list_values_anos_pm_2021 = pm_anos_2021['ANOS_PM_2021']
pm_2021.insert(2, 'ANOS_PM_2021', list_values_anos_pm_2021)


''' # # Criação coluna INGRESSANTE_ '''

# In[ ]:


def get_ingressante(anos_pm):
    if anos_pm == 0:
        return 1
    else:
        return 0

pm_2020['SINALIZADOR_INGRESSANTE_2020'] = pm_2020['ANOS_PM_2020'].apply(get_ingressante)
pm_2022['SINALIZADOR_INGRESSANTE_2022'] = pm_2022['ANOS_PM_2022'].apply(get_ingressante)


''' # # Conhecendo o Nível De Ensino '''

# In[29]:


def ajustar_fase_alfa(x):
    if x.startswith('ALFA'):
        return x.replace('ALFA ','FASE 0')
    else:
        return x

def calcular_nivel_ensino(nivel_ideal, nivel_atual):
    if nivel_ideal != 'Não se Aplica':
        nivel_str = nivel_ideal.split( )[1]
        return int(nivel_str)
    else:
        return int(nivel_atual)


''' ## 2020
#
# Sem dados de nivel de ensino atual '''

# In[33]:


pm_2020['NIVEL_IDEAL_2020'] = None
pm_2020['DEFASAGEM_2020'] = None


''' ## 2021 '''

# In[41]:


''' # Ajuste nomenclatura fase Alfa '''
pm_2021['NIVEL_IDEAL_2021'] = pm_2021['NIVEL_IDEAL_2021'].apply(ajustar_fase_alfa)


# In[42]:


st.write(pm_2021['NIVEL_IDEAL_2021'].unique())


# In[43]:


''' # Calculo numero inteiro '''
pm_2021['NIVEL_IDEAL_2021'] = pm_2021.apply(lambda row: calcular_nivel_ensino(row['NIVEL_IDEAL_2021'], row['FASE_2021']), axis=1)
st.write(pm_2021['NIVEL_IDEAL_2021'].unique())


# ## 2022

# In[45]:


st.write(pm_2022['NIVEL_IDEAL_2022'].unique())


# In[46]:


pm_2022['NIVEL_IDEAL_2022'] = pm_2022['NIVEL_IDEAL_2022'].apply(ajustar_fase_alfa)


# In[47]:


pm_2022['NIVEL_IDEAL_2022'] = pm_2022.apply(lambda row: calcular_nivel_ensino(row['NIVEL_IDEAL_2022'], row['FASE_2022']), axis=1)
st.write(pm_2022['NIVEL_IDEAL_2022'].unique())


# In[48]:


pm_2022['DEFASAGEM_2022'] = pm_2022['NIVEL_IDEAL_2022'] - pm_2022['FASE_2022']
pm_2022


''' # Colunas Instituição de Ensino e Bolsa de Estudos '''

# In[49]:


def verificar_bolsista(x):
    if x != 'Escola Pública':
        return 1
    else:
        return 0


# In[51]:


pm_2020['BOLSISTA_2020'] = pm_2020['INSTITUICAO_ENSINO_ALUNO_2020'].apply(verificar_bolsista)
pm_2021['BOLSISTA_2021'] = pm_2021['INSTITUICAO_ENSINO_ALUNO_2021'].apply(verificar_bolsista)


# In[52]:


pm_2021['BOLSISTA_2021'].value_counts()


# In[53]:


pm_2020['BOLSISTA_2020'].value_counts()


# In[54]:


pm_2022['BOLSISTA_2022'].value_counts()


# In[55]:


pm_2022.loc[pm_2022['BOLSISTA_2022'] == 1, 'INSTITUICAO_ENSINO_ALUNO_2022'] = 'Instituição Privada'
pm_2022.loc[pm_2022['BOLSISTA_2022'] == 0, 'INSTITUICAO_ENSINO_ALUNO_2022'] = 'Instituição Pública'


''' # Criação ID do Aluno e Ano Pesquisa '''

# In[58]:


pm_2020['ANO_PESQUISA'] = 2020
pm_2021['ANO_PESQUISA'] = 2021
pm_2022['ANO_PESQUISA'] = 2022


# In[59]:


def get_aluno_id(x):
    return int(x.split('-')[-1])

pm_2020['ID'] = pm_2020['NOME'].apply(get_aluno_id)
pm_2021['ID'] = pm_2021['NOME'].apply(get_aluno_id)
pm_2022['ID'] = pm_2022['NOME'].apply(get_aluno_id)


# In[64]:


st.table(pm_2020.head())


# In[65]:


st.table(pm_2021.head())


''' # Concatenação dos Dados '''

# In[69]:


def concat_dados_pm(df):
    common_cols = ['ID','NOME','ANO_PESQUISA','INSTITUICAO_ENSINO_ALUNO','BOLSISTA','ANOS_PM','FASE','TURMA','PONTO_VIRADA','INDE',
 'PEDRA', 'IAA','IEG','IPS','IDA','IPP','IPV','IAN','NIVEL_IDEAL', 'DEFASAGEM']

    ano = df['ANO_PESQUISA'].values[0]

    col_names = [col.split(f'_{ano}')[0] for col in df.columns]
    df.columns = col_names

    dados_pm = df[common_cols]

    return dados_pm


# In[72]:


pm_2020_to_merge = concat_dados_pm(pm_2020)
pm_2021_to_merge = concat_dados_pm(pm_2021)
pm_2022_to_merge = concat_dados_pm(pm_2022)


# In[75]:


list_pm = [pm_2020_to_merge, pm_2021_to_merge, pm_2022_to_merge]

df_pm_merged = pd.DataFrame()

for df in list_pm:
    if len(df_pm_merged) == 0:
        df_pm_merged = df.copy()
    else:
        df_pm_merged = pd.concat([df_pm_merged, df], axis=0)


''' ##Tratamento do Tipo de Dados '''

# In[76]:


df_pm_merged['NIVEL_IDEAL'] = df_pm_merged['NIVEL_IDEAL'].astype(float)
df_pm_merged['DEFASAGEM'] = df_pm_merged['DEFASAGEM'].astype(float)
df_pm_merged['ANOS_PM'] = df_pm_merged['ANOS_PM'].astype(int)
df_pm_merged.sort_values(by=['ANO_PESQUISA','ID'], inplace=True)
df_pm_merged.reset_index(drop=True, inplace=True)


''' #Dataset Final '''

# In[78]:


# In[81]:


df_pm_merged.to_csv('Dataset/df_pm_merged.csv', index=False)


# In[ ]:


df_pm_merged.columns


''' ## Criação de formato longo '''

# In[83]:


df_pm_melt = pd.melt(df_pm_merged, id_vars=['ANO_PESQUISA','BOLSISTA','ID','INSTITUICAO_ENSINO_ALUNO','NOME','PEDRA','PONTO_VIRADA','FASE','TURMA'], var_name='VARIAVEL', value_name='VALOR')
st.table(df_pm_melt.head())


# In[84]:


df_pm_melt.to_csv('Dataset/df_pm_melt.csv', index=False)


# In[85]:


df_pm_melt.loc[(df_pm_melt['PONTO_VIRADA'] == "Sim") & (df_pm_melt['VARIAVEL'] == 'IDA')]['VALOR'].mean()


# In[ ]:




