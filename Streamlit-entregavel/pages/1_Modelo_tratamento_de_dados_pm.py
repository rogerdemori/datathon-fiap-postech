#!/usr/bin/env python
# coding: utf-8

# # Datathon Pós-Tech Data Analytics

# ## Importando as bibliotecas e trazendo a Base de Dados

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st

# Definir título da página
st.title('Modelo para tratamento de dados PM')

# In[2]:


df = pd.read_csv('Dataset/PEDE_PASSOS_DATASET_FIAP.csv', index_col=1, sep=";")
st.table(df.head())


# In[3]:


print(df.columns.tolist())


# In[4]:


st.write(df.info())


# In[5]:


st.write(df.describe())


''' ## Tratamento e Manipulação de Dados

### Fissão da Base de Dados por Ano '''

# In[6]:


df_2020 = df.loc[df["INSTITUICAO_ENSINO_ALUNO_2020"].notnull(), ["INSTITUICAO_ENSINO_ALUNO_2020", "IDADE_ALUNO_2020", "ANOS_PM_2020", "FASE_TURMA_2020", "PONTO_VIRADA_2020", "INDE_2020", "INDE_CONCEITO_2020", "PEDRA_2020", "DESTAQUE_IEG_2020", "DESTAQUE_IDA_2020", "DESTAQUE_IPV_2020", "IAA_2020", "IEG_2020", "IPS_2020", "IDA_2020", "IPP_2020", "IPV_2020", "IAN_2020"]]


# In[7]:


st.write(df_2020.info())


# In[8]:


df_2021 = df.loc[df["INSTITUICAO_ENSINO_ALUNO_2021"].notnull(), ["INSTITUICAO_ENSINO_ALUNO_2021", "FASE_2021", "TURMA_2021", "PONTO_VIRADA_2021", "SINALIZADOR_INGRESSANTE_2021", "INDE_2021", "PEDRA_2021", "IAA_2021", "IEG_2021", "IPS_2021", "IDA_2021", "IPP_2021", "IPV_2021", "IAN_2021", "REC_EQUIPE_1_2021", "REC_EQUIPE_2_2021", "REC_EQUIPE_3_2021", "REC_EQUIPE_4_2021", "NIVEL_IDEAL_2021", "DEFASAGEM_2021"]]


# In[9]:


st.write(df_2021.info())


# In[10]:


df_2022 = df.loc[df["ANO_INGRESSO_2022"].notnull(), ['ANO_INGRESSO_2022', 'BOLSISTA_2022', 'FASE_2022', 'TURMA_2022', 'PONTO_VIRADA_2022', 'INDE_2022', 'PEDRA_2022', 'CG_2022', 'CF_2022', 'CT_2022', 'DESTAQUE_IEG_2022', 'DESTAQUE_IDA_2022', 'DESTAQUE_IPV_2022', 'IAA_2022', 'IEG_2022', 'IPS_2022', 'IDA_2022', 'IPP_2022', 'IPV_2022', 'IAN_2022', 'NOTA_PORT_2022', 'NOTA_MAT_2022', 'NOTA_ING_2022', 'QTD_AVAL_2022', 'REC_AVA_1_2022', 'REC_AVA_2_2022', 'REC_AVA_3_2022', 'REC_AVA_4_2022', 'NIVEL_IDEAL_2022', 'INDICADO_BOLSA_2022']]


# In[11]:


st.write(df_2022.info())


''' ### Base de Dados 2020

#### Instituição de Ensino '''

# In[12]:


st.write(df_2020["INSTITUICAO_ENSINO_ALUNO_2020"].unique())


# In[13]:


df_2020["INSTITUICAO_ENSINO_ALUNO_2020"] = df_2020["INSTITUICAO_ENSINO_ALUNO_2020"].astype("category")


''' #### Idade Aluno '''

# In[14]:


st.write(df_2020['IDADE_ALUNO_2020'].unique())


# In[15]:


#ValueError: invalid literal for int() with base 10: 'D108'
df_2020.loc[df_2020["IDADE_ALUNO_2020"] == 'D108']


# In[16]:


df_2020 = df_2020.drop(["ALUNO-1259"])


# In[17]:


df_2020["IDADE_ALUNO_2020"] = df_2020["IDADE_ALUNO_2020"].astype(pd.Int64Dtype())


''' #### Anos na Passos Magicos '''

# In[18]:


st.write(df_2020['ANOS_PM_2020'].unique())


# In[19]:


df_2020['ANOS_PM_2020'] = df_2020['ANOS_PM_2020'].astype(pd.Int16Dtype())


''' #### Fase do Aluno na Passos Magicos em 2020 '''

# In[20]:


st.write(df_2020['FASE_TURMA_2020'].unique())


# In[21]:


df_fase = df_2020['FASE_TURMA_2020'].astype(str).str[0]


# In[22]:


df_2020.insert(3,"FASE_2020", df_fase)


# In[23]:


st.write(df_2020["FASE_2020"].unique())


# In[24]:


df_2020["FASE_2020"] = df_2020["FASE_2020"].astype("category")
st.table(df_2020.head())


''' #### Turma do Aluno na Passos Magicos em 2020 '''

# In[25]:


df_turma = df_2020['FASE_TURMA_2020'].astype(str).str[1]


# In[26]:


df_2020.insert(4,"TURMA_2020", df_turma)


# In[27]:


st.write(df_2020["TURMA_2020"].unique())


# In[28]:


df_2020["TURMA_2020"] = df_2020["TURMA_2020"].astype("category")


# In[29]:


df_2020 = df_2020.drop(['FASE_TURMA_2020'], axis=1)


''' #### Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2020 '''

# In[30]:


st.write(df_2020['PONTO_VIRADA_2020'].unique())


# In[31]:


df_2020['PONTO_VIRADA_2020'].isna().sum()


# In[32]:


df_2020['PONTO_VIRADA_2020'] = df_2020['PONTO_VIRADA_2020'].fillna("Não se Aplica")


# In[33]:


df_2020["PONTO_VIRADA_2020"] = df_2020["PONTO_VIRADA_2020"].astype("category")


''' #### Indice do Desenvolvimento Educacional – Metrica de Processo Avaliativo Geral do Aluno '''

# In[34]:


st.write(df_2020["INDE_2020"].unique())


# In[35]:


df_2020['INDE_2020'].isna().sum()


# In[36]:


df_2020['INDE_2020'] = df_2020['INDE_2020'].astype(pd.Float64Dtype())


# In[37]:


df_2020['INDE_2020'] = np.round(df_2020['INDE_2020'], decimals=3)


# #### INDE Conceito

# In[38]:


# Category
st.write(df_2020['INDE_CONCEITO_2020'].unique())


# In[38]:





# In[39]:


df_2020["INDE_CONCEITO_2020"] = df_2020["INDE_CONCEITO_2020"].astype("category")


''' ### Classificaça o do Aluno baseado no nu mero do INDE, o conceito de classificaça o e dado por:
####Quartzo – 2,405 a 5,506
####Agata – 5,506 a 6,868
####Ametista – 6,868 a 8,230
####Topazio – 8,230 a 9,294.'''

# In[40]:


st.write(df_2020['PEDRA_2020'].unique())


# In[41]:


df_2020["PEDRA_2020"] = df_2020["PEDRA_2020"].astype("category")


''' #### Destaque IEG '''

# In[42]:


st.write(df_2020['DESTAQUE_IEG_2020'].unique())


# In[43]:


df_2020["DESTAQUE_IEG_2020"] = df_2020["DESTAQUE_IEG_2020"].astype("category")


''' #### Destaque IDA '''

# In[44]:


# Category
st.write(df_2020['DESTAQUE_IDA_2020'].unique())


# In[45]:


df_2020["DESTAQUE_IDA_2020"] = df_2020["DESTAQUE_IDA_2020"].astype("category")


''' #### Destaque IPV '''

# In[46]:


st.write(df_2020['DESTAQUE_IPV_2020'].unique())


# In[47]:


df_2020['DESTAQUE_IPV_2020'].isna().sum()


# In[48]:


df_2020['DESTAQUE_IPV_2020'] = df_2020['DESTAQUE_IPV_2020'].fillna("Não se Aplica")


# In[49]:


df_2020["DESTAQUE_IPV_2020"] = df_2020["DESTAQUE_IPV_2020"].astype("category")


''' #### Indicador de Auto Avalição '''

# In[50]:


st.write(df_2020["IAA_2020"].unique())


# In[51]:


df_2020['IAA_2020'].isna().sum()


# In[52]:


df_2020['IAA_2020'] = df_2020['IAA_2020'].astype(pd.Float64Dtype())


# In[53]:


df_2020['IAA_2020'] = np.round(df_2020['IAA_2020'], decimals=3)


# #### IEG

# In[54]:


st.write(df_2020["IEG_2020"].unique())


# In[55]:


df_2020['IEG_2020'].isna().sum()


# In[56]:


df_2020['IEG_2020'] = df_2020['IEG_2020'].astype(pd.Float64Dtype())


# In[57]:


df_2020['IEG_2020'] = np.round(df_2020['IEG_2020'], decimals=3)


# #### IPS

# In[58]:


st.write(df_2020["IPS_2020"].unique())


# In[59]:


df_2020['IPS_2020'].isna().sum()


# In[60]:


df_2020['IPS_2020'] = df_2020['IPS_2020'].astype(pd.Float64Dtype())


# In[61]:


df_2020['IPS_2020'] = np.round(df_2020['IPS_2020'], decimals=3)


''' #### IDA '''

# In[62]:


st.write(df_2020["IDA_2020"].unique())


# In[63]:


df_2020['IDA_2020'].isna().sum()


# In[64]:


df_2020['IDA_2020'] = df_2020['IDA_2020'].astype(pd.Float64Dtype())


# In[65]:


df_2020['IDA_2020'] = np.round(df_2020['IDA_2020'], decimals=3)


''' #### IPP '''

# In[66]:


st.write(df_2020["IPP_2020"].unique())


# In[67]:


''' Float64 '''
df_2020['IPP_2020'].isna().sum()


# In[68]:


df_2020['IPP_2020'] = df_2020['IPP_2020'].astype(pd.Float64Dtype())


# In[69]:


df_2020['IPP_2020'] = np.round(df_2020['IPP_2020'], decimals=3)


# #### IPV

# In[70]:


st.write(df_2020["IPV_2020"].unique())


# In[71]:


df_2020['IPV_2020'].isna().sum()


# In[72]:


df_2020['IPV_2020'] = df_2020['IPV_2020'].astype(pd.Float64Dtype())


# In[73]:


df_2020['IPV_2020'] = np.round(df_2020['IPV_2020'], decimals=3)


''' #### IAN '''

# In[74]:


st.write(df_2020["IAN_2020"].unique())


# In[75]:


df_2020['IAN_2020'].isna().sum()


# In[76]:


df_2020['IAN_2020'] = df_2020['IAN_2020'].astype(pd.Float64Dtype())


# In[77]:


df_2020['IAN_2020'] = np.round(df_2020['IAN_2020'], decimals=2)


''' #### Base de Dados 2020 Tratada '''

# In[78]:


st.write(df_2020.info())


# In[79]:


df_2020.reset_index(inplace=True)

# In[81]:


df_2020.to_csv('Dataset/pm_2020.csv', index=False)


# In[81]:





''' ### Base de Dados 2021

#### Instituição de Ensino '''

# In[82]:


st.write(df_2021["INSTITUICAO_ENSINO_ALUNO_2021"].unique())


# In[83]:


df_2021["INSTITUICAO_ENSINO_ALUNO_2021"] = df_2021["INSTITUICAO_ENSINO_ALUNO_2021"].astype("category")


''' #### Nível de Aprendizado do Aluno em 2021 '''

# In[84]:


st.write(df_2021["FASE_2021"].unique())


# In[85]:


df_2021['FASE_2021'] = df_2021['FASE_2021'].astype(str).str[0]


# In[86]:


df_2021["FASE_2021"] = df_2021["FASE_2021"].astype("category")


''' #### Numero da Turma de cada fase (1A,1B,1C) '''

# In[87]:


st.write(df_2021["TURMA_2021"].unique())


# In[88]:


df_2021["TURMA_2021"] = df_2021["TURMA_2021"].astype("category")


''' #### Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2021. '''

# In[89]:


st.write(df_2021["PONTO_VIRADA_2021"].unique())


# In[90]:


df_2021["PONTO_VIRADA_2021"].loc[df_2021["PONTO_VIRADA_2021"] == '#NULO!']


# In[91]:


df_2021["PONTO_VIRADA_2021"] = df_2021["PONTO_VIRADA_2021"].replace('#NULO!','Não se Aplica')


# In[92]:


df_2021["PONTO_VIRADA_2021"] = df_2021["PONTO_VIRADA_2021"].astype("category")


''' #### Ingressou ou e Veterano no ano de 2021 '''

# In[93]:


st.write(df_2021["SINALIZADOR_INGRESSANTE_2021"].unique())


# In[94]:


df_2021["SINALIZADOR_INGRESSANTE_2021"] = df_2021["SINALIZADOR_INGRESSANTE_2021"].astype("category")


# #### Indice do Desenvolvimento Educacional – Metrica de Processo Avaliativo Geral do Aluno

# In[95]:


df_2021['INDE_2021'].isna().sum()


# In[96]:


st.write(df_2021["INDE_2021"].unique())


# In[97]:


df_2021["INDE_2021"].loc[df_2021["INDE_2021"] == "#NULO!"]


# In[98]:


df_2021["INDE_2021"] = df_2021["INDE_2021"].replace('#NULO!','0.0')


# In[99]:


df_2021['INDE_2021'] = df_2021['INDE_2021'].astype(pd.Float64Dtype())


# In[100]:


df_2021['INDE_2021'] = np.round(df_2021['INDE_2021'], decimals=3)


''' ### Classificaça o do Aluno baseado no nu mero do INDE, o conceito de classificaça o e dado por:
# ####Quartzo – 2,405 a 5,506
# ####Agata – 5,506 a 6,868
# ####Ametista – 6,868 a 8,230
# ####Topazio – 8,230 a 9,294. '''

# In[101]:


st.write(df_2021["PEDRA_2021"].unique())


# In[102]:


df_2021["PEDRA_2021"] = df_2021["PEDRA_2021"].replace('#NULO!','Não se Aplica')


# In[103]:


df_2021["PEDRA_2021"] = df_2021["PEDRA_2021"].astype("category")


# #### Indicador de Auto Avaliçao

# In[104]:


st.write(df_2021["IAA_2021"].unique())


# In[105]:


df_2021['IAA_2021'] = df_2021['IAA_2021'].astype(pd.Float64Dtype())


# In[106]:


df_2021['IAA_2021'] = np.round(df_2021['IAA_2021'], decimals=3)


''' #### IEG '''

# In[107]:


st.write(df_2021["IEG_2021"].unique())


# In[108]:


df_2021['IEG_2021'] = df_2021['IEG_2021'].astype(pd.Float64Dtype())


# In[109]:


df_2021['IEG_2021'] = np.round(df_2021['IEG_2021'], decimals=3)


''' #### IPS '''

# In[110]:


st.write(df_2021["IPS_2021"].unique())


# In[111]:


df_2021['IPS_2021'] = df_2021['IPS_2021'].astype(pd.Float64Dtype())


# In[112]:


df_2021['IPS_2021'] = np.round(df_2021['IPS_2021'], decimals=3)


''' #### IDA '''

# In[113]:


st.write(df_2021["IDA_2021"].unique())


# In[114]:


df_2021['IDA_2021'] = df_2021['IDA_2021'].astype(pd.Float64Dtype())


# In[115]:


df_2021['IDA_2021'] = np.round(df_2021['IDA_2021'], decimals=3)


''' #### IPP '''

# In[116]:


st.write(df_2021["IPP_2021"].unique())


# In[117]:


df_2021['IPP_2021'] = df_2021['IPP_2021'].astype(pd.Float64Dtype())


# In[118]:


df_2021['IPP_2021'] = np.round(df_2021['IPP_2021'], decimals=3)


''' #### IPV '''

# In[119]:


st.write(df_2021["IPV_2021"].unique())


# In[120]:


df_2021['IPV_2021'] = df_2021['IPV_2021'].astype(pd.Float64Dtype())


# In[121]:


df_2021['IPV_2021'] = np.round(df_2021['IPV_2021'], decimals=3)


''' #### IAN '''

# In[122]:


st.write(df_2021["IAN_2021"].unique())


# In[123]:


df_2021['IAN_2021'] = df_2021['IAN_2021'].astype(pd.Float64Dtype())


# In[124]:


df_2021['IAN_2021'] = np.round(df_2021['IAN_2021'], decimals=2)


# #### REC 1

# In[125]:


st.write(df_2021["REC_EQUIPE_1_2021"].unique())


# In[126]:


df_2021["REC_EQUIPE_1_2021"] = df_2021["REC_EQUIPE_1_2021"].astype("category")


''' #### REC 2 '''

# In[127]:


st.write(df_2021["REC_EQUIPE_2_2021"].unique())


# In[128]:


df_2021["REC_EQUIPE_2_2021"] = df_2021["REC_EQUIPE_2_2021"].astype("category")


''' #### REC 3 '''

# In[129]:


st.write(df_2021["REC_EQUIPE_3_2021"].unique())


# In[130]:


df_2021["REC_EQUIPE_3_2021"] = df_2021["REC_EQUIPE_3_2021"].astype("category")


''' #### REC 4 '''

# In[131]:


st.write(df_2021["REC_EQUIPE_4_2021"].unique())


# In[132]:


df_2021["REC_EQUIPE_4_2021"] = df_2021["REC_EQUIPE_4_2021"].astype("category")


''' #### Nivel '''

# In[133]:


st.write(df_2021["NIVEL_IDEAL_2021"].unique())


# In[134]:


df_2021["NIVEL_IDEAL_2021"].loc[df_2021["NIVEL_IDEAL_2021"] == 'ERRO']


# In[135]:


df_2021.iloc[178]


# In[136]:


df_2021.iloc[615]


# In[137]:


df_2021["NIVEL_IDEAL_2021"] = df_2021["NIVEL_IDEAL_2021"].replace('ERRO','Não se Aplica')


# In[138]:


st.write(df_2021["NIVEL_IDEAL_2021"].unique())


# In[139]:


df_2021["NIVEL_IDEAL_2021"] = df_2021["NIVEL_IDEAL_2021"].astype("category")


''' #### Defasagem '''

# In[140]:


st.write(df_2021["DEFASAGEM_2021"].unique())


# In[141]:


df_2021['DEFASAGEM_2021'] = df_2021['DEFASAGEM_2021'].astype(pd.Int16Dtype())


''' ### Anos PM

#### DataFrame 2021 Final '''

# In[142]:


st.write(df_2021.info())


# In[143]:


df_2021.reset_index(inplace=True)


# In[144]:

# In[144]:





# In[145]:


''' Salvando o DataFrame '''
df_2021.to_csv('Dataset/passos_2021.csv', index=False)


''' ### Limpando DataFrame 2022

#### Ano Ingresso '''

# In[146]:


st.write(df_2022["ANO_INGRESSO_2022"].unique())


# In[147]:


df_2022['ANO_INGRESSO_2022'] = df_2022['ANO_INGRESSO_2022'].astype(pd.Int16Dtype())


''' #### Bolsista '''

# In[148]:


# Bool
st.write(df_2022["BOLSISTA_2022"].unique())


# In[149]:


df_2022["BOLSISTA_2022"] = df_2022["BOLSISTA_2022"].map({'Sim':True,'Não':False})


''' #### Fase '''

# In[150]:


''' # Category '''
st.write(df_2022["FASE_2022"].unique())


# In[151]:


df_2022['FASE_2022'] = df_2022['FASE_2022'].astype(str).str[0]


# In[152]:


df_2022["FASE_2022"] = df_2022["FASE_2022"].astype("category")


''' #### Turma '''

# In[153]:


''' Category '''
st.write(df_2022["TURMA_2022"].unique())


# In[154]:


df_2022["TURMA_2022"] = df_2022["TURMA_2022"].astype("category")


''' #### Ponto de Virada '''

# In[155]:


# Category
st.write(df_2022["PONTO_VIRADA_2022"].unique())


# In[156]:


df_2022["PONTO_VIRADA_2022"] = df_2022["PONTO_VIRADA_2022"].astype("category")


''' #### INDE '''

# In[157]:


''' Float64 '''
st.write(df_2022["INDE_2022"].unique())


# In[158]:


df_2022["INDE_2022"].isna().sum()


# In[159]:


df_2022['INDE_2022'] = df_2022['INDE_2022'].astype(pd.Float64Dtype())


# In[160]:


df_2022['INDE_2022'] = np.round(df_2022['INDE_2022'], decimals=3)


''' #### Pedra '''

# In[161]:


''' Category '''
st.write(df_2022["PEDRA_2022"].unique())


# In[162]:


df_2022["PEDRA_2022"] = df_2022["PEDRA_2022"].astype("category")


''' #### CG '''

# In[163]:


''' Int16 '''
st.write(df_2022["CG_2022"].unique())


# In[164]:


df_2022["CG_2022"].isna().sum()


# In[165]:


df_2022['CG_2022'] = df_2022['CG_2022'].astype(pd.Int16Dtype())


''' #### CF '''

# In[166]:


''' Int16 '''
st.write(df_2022["CF_2022"].unique())


# In[167]:


df_2022["CF_2022"].isna().sum()


# In[168]:


df_2022['CF_2022'] = df_2022['CF_2022'].astype(pd.Int16Dtype())


''' #### CT '''

# In[169]:


''' Int16 '''
st.write(df_2022["CT_2022"].unique())


# In[170]:


df_2022["CT_2022"].isna().sum()


# In[171]:


df_2022['CT_2022'] = df_2022['CT_2022'].astype(pd.Int16Dtype())


''' #### Destaque IEG '''

# In[172]:


''' Category '''
st.write(df_2022["DESTAQUE_IEG_2022"].unique())


# In[173]:


df_2022["DESTAQUE_IEG_2022"] = df_2022["DESTAQUE_IEG_2022"].astype("category")


''' #### Destaque IDA '''

# In[174]:


''' # Category '''
st.write(df_2022["DESTAQUE_IDA_2022"].unique())


# In[175]:


df_2022["DESTAQUE_IDA_2022"] = df_2022["DESTAQUE_IDA_2022"].astype("category")


''' #### Destaque IPV '''

# In[176]:


'''  Category '''
st.write(df_2022["DESTAQUE_IPV_2022"].unique())


# In[177]:


df_2022["DESTAQUE_IPV_2022"] = df_2022["DESTAQUE_IPV_2022"].astype("category")


''' #### IAA '''

# In[178]:


df_2022["IAA_2022"].isna().sum()


# In[179]:


''' Float64 '''
st.write(df_2022["IAA_2022"].unique())


# In[180]:


df_2022['IAA_2022'] = df_2022['IAA_2022'].astype(pd.Float64Dtype())


# In[181]:


df_2022['IAA_2022'] = np.round(df_2022['IAA_2022'], decimals=3)


''' #### IEG '''

# In[182]:


df_2022["IEG_2022"].isna().sum()


# In[183]:


''' Float64 '''
st.write(df_2022["IEG_2022"].unique())


# In[184]:


df_2022['IEG_2022'] = df_2022['IEG_2022'].astype(pd.Float64Dtype())


# In[185]:


df_2022['IEG_2022'] = np.round(df_2022['IEG_2022'], decimals=3)


''' #### IPS '''

# In[186]:


df_2022["IPS_2022"].isna().sum()


# In[187]:


''' # Float64 '''
st.write(df_2022["IPS_2022"].unique())


# In[188]:


df_2022['IPS_2022'] = df_2022['IPS_2022'].astype(pd.Float64Dtype())


# In[189]:


df_2022['IPS_2022'] = np.round(df_2022['IPS_2022'], decimals=3)


''' #### IDA '''

# In[190]:


df_2022["IDA_2022"].isna().sum()


# In[191]:


''' # Float64 '''
st.write(df_2022["IDA_2022"].unique())


# In[192]:


df_2022['IDA_2022'] = df_2022['IDA_2022'].astype(pd.Float64Dtype())


# In[193]:


df_2022['IDA_2022'] = np.round(df_2022['IDA_2022'], decimals=3)


''' #### IPP '''

# In[194]:


df_2022["IPP_2022"].isna().sum()


# In[195]:


''' # Float64 '''
st.write(df_2022["IPP_2022"].unique())


# In[196]:


df_2022['IPP_2022'] = df_2022['IPP_2022'].astype(pd.Float64Dtype())


# In[197]:


df_2022['IPP_2022'] = np.round(df_2022['IPP_2022'], decimals=3)


''' #### IPV '''

# In[198]:


df_2022["IPV_2022"].isna().sum()


# In[199]:


''' # Float64 '''
st.write(df_2022["IPV_2022"].unique())


# In[200]:


df_2022['IPV_2022'] = df_2022['IPV_2022'].astype(pd.Float64Dtype())


# In[201]:


df_2022['IPV_2022'] = np.round(df_2022['IPV_2022'], decimals=3)


''' #### IAN '''

# In[202]:


df_2022["IAN_2022"].isna().sum()


# In[203]:


''' # Float64 '''
st.write(df_2022["IAN_2022"].unique())


# In[204]:


df_2022['IAN_2022'] = df_2022['IAN_2022'].astype(pd.Float64Dtype())


# In[205]:


df_2022['IAN_2022'] = np.round(df_2022['IAN_2022'], decimals=2)


''' #### Nota Português '''

# In[206]:


df_2022["NOTA_PORT_2022"].isna().sum()


# In[207]:


df_2022["NOTA_PORT_2022"] = df_2022["NOTA_PORT_2022"].replace(np.nan,'0.0')


# In[208]:


''' # Float64 '''
st.write(df_2022["NOTA_PORT_2022"].unique())


# In[209]:


df_2022['NOTA_PORT_2022'] = df_2022['NOTA_PORT_2022'].astype(pd.Float64Dtype())


# In[210]:


df_2022['NOTA_PORT_2022'] = np.round(df_2022['NOTA_PORT_2022'], decimals=3)


''' #### Nota Matemática '''

# In[211]:


df_2022["NOTA_MAT_2022"].isna().sum()


# In[212]:


df_2022["NOTA_MAT_2022"] = df_2022["NOTA_MAT_2022"].replace(np.nan,'0.0')


# In[213]:


''' # Float64 '''
st.write(df_2022["NOTA_MAT_2022"].unique())


# In[214]:


df_2022["NOTA_MAT_2022"] = df_2022["NOTA_MAT_2022"].replace('#NULO!','0.0')


# In[215]:


df_2022['NOTA_MAT_2022'] = df_2022['NOTA_MAT_2022'].astype(pd.Float64Dtype())


# In[216]:


df_2022['NOTA_MAT_2022'] = np.round(df_2022['NOTA_MAT_2022'], decimals=3)


''' #### Nota Inglês '''

# In[217]:


df_2022["NOTA_ING_2022"].isna().sum()


# In[218]:


df_2022["NOTA_ING_2022"] = df_2022["NOTA_ING_2022"].replace(np.nan,'0.0')


# In[219]:


''' # Float64 '''
st.write(df_2022["NOTA_ING_2022"].unique())


# In[220]:


df_2022['NOTA_ING_2022'] = df_2022['NOTA_ING_2022'].astype(pd.Float64Dtype())


# In[221]:


df_2022['NOTA_ING_2022'] = np.round(df_2022['NOTA_ING_2022'], decimals=3)


# In[222]:


st.write(df_2022['NOTA_ING_2022'].describe())


''' #### Quantidade de Avaliações '''

# In[223]:


# Int16
st.write(df_2022["QTD_AVAL_2022"].unique())


# In[224]:


df_2022['QTD_AVAL_2022'] = df_2022['QTD_AVAL_2022'].astype(pd.Int16Dtype())


''' #### REC 1 '''

# In[225]:


''' # Category '''
st.write(df_2022["REC_AVA_1_2022"].unique())


# In[226]:


df_2022["REC_AVA_1_2022"] = df_2022["REC_AVA_1_2022"].astype("category")


''' #### REC 2 '''

# In[227]:


''' # Category '''
st.write(df_2022["REC_AVA_2_2022"].unique())


# In[228]:


df_2022["REC_AVA_2_2022"] = df_2022["REC_AVA_2_2022"].astype("category")


''' #### REC 3 '''

# In[229]:


''' # Category '''
st.write(df_2022["REC_AVA_3_2022"].unique())


# In[230]:


df_2022["REC_AVA_3_2022"] = df_2022["REC_AVA_3_2022"].astype("category")


''' #### REC 4 '''

# In[231]:


''' # Category '''
st.write(df_2022["REC_AVA_4_2022"].unique())


# In[232]:


df_2022["REC_AVA_4_2022"] = df_2022["REC_AVA_4_2022"].astype("category")


''' #### Nivel '''

# In[233]:


''' # Category '''
st.write(df_2022["NIVEL_IDEAL_2022"].unique())


# In[234]:


df_2022["NIVEL_IDEAL_2022"] = df_2022["NIVEL_IDEAL_2022"].astype("category")


''' #### Indicação para Bolsa '''

# In[235]:


''' # Bool '''
st.write(df_2022["INDICADO_BOLSA_2022"].unique())


# In[236]:


df_2022["INDICADO_BOLSA_2022"] = df_2022["INDICADO_BOLSA_2022"].map({"Sim":True,"Não":False})


''' #### DataFrame 2022 Final '''

# In[237]:


st.dataframe(df_2022.info())


# In[238]:


df_2022.reset_index(inplace=True)


# In[239]:

df_2022.to_csv('Dataset/passos_2022.csv', index=False)


# In[239]:




