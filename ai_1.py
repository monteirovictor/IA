# -*- coding: utf-8 -*-
"""AI-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KkFT7Q0mJ4MPQL1-AMwJthgeB-BhzfQI
"""

#Atividade 1 -> Rafael Faturini e Victor Monteiro

#Para baixar o Dataset utilize este link: https://drive.google.com/file/d/1cDwhyjKviU977c4jrG_Ab6-DMoRbaL7w/view?usp=sharing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#importação de Dados
df= pd.read_csv("/content/drive/MyDrive/python/water_potability.csv")

print(df.info(verbose=True))

df[1:10]

# Informações estatísticas básicas do dataframe (media, desvio padrão, maximo, minimo)
df.describe( )

coluna1=df.iloc[:,0]
coluna2=df.iloc[:,1]
coluna3=df.iloc[:,2]
coluna4=df.iloc[:,3]
coluna5=df.iloc[:,4]
coluna6=df.iloc[:,5]
coluna7=df.iloc[:,6]
coluna8=df.iloc[:,7]
coluna9=df.iloc[:,8]

# reduzimos os valores apenas de maneira ilustrativa para entender os dados faltantes
Acoluna = [coluna1,coluna2/10,coluna3/2000,coluna4,coluna5,coluna6/20,coluna7,coluna8,coluna9]

plt.boxplot(Acoluna)
plt.show()

# Fica evidente pela falta  dos Boxplots das colunas relativas ao ph (1), 
# Sulfate (5) e Trihalomethanes (8) que esses elementos possui dados faltantes

#Missing Values

# -> Verificando a quantidade de dados nulos no dataframe
df.isna().sum()

# Commented out IPython magic to ensure Python compatibility.
# -> Mapa de Dados Faltantes


import missingno as msno
# %matplotlib inline
msno.matrix(df)

#inserindo valores por media
import numpy as np
from sklearn.impute import SimpleImputer

imp=SimpleImputer(missing_values=np.nan,strategy='mean')
df_221=pd.DataFrame(imp.fit_transform(df_miss))
df_221.columns=df_miss.columns
df_221.index=df_miss.index
df_221.head()

msno.matrix(df_221)

#Outliers

graphFirst=df_221['ph']
graphSecond=df_221['Sulfate']
graphThird=df_221['Trihalomethanes']
graph=[graphFirst,graphSecond,graphThird]

plt.boxplot(graph)
plt.show()

Z = (df_221-df_221.mean())/df_221.std()
Z[20:25]

print('Numero de linhas antes da remoção de outliers = %d' % (Z.shape[0]))

Z2 = Z.loc[((Z > -3).sum(axis=1)==9) & ((Z <= 3).sum(axis=1)==9),:]
print('Numero de linhas após o tratamento = %d' % (Z2.shape[0]))

#Amostragem 

Amostra = df_221.sample(frac=0.01, random_state=1)
Amostra

# Amostra Sistemática


# Selecionado um registro aleatório entre os valores de 0 a 10:
semente = np.random.choice(10, 1)

# Gerando um array que inicia em 0 e termina em 100 com um intervalo de 7:
indices = np.arange(0,20,semente)

amostra2 = df_221.loc[indices,:]
amostra2