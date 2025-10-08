import numpy as np
import pandas as pd

indices = ["Ted Lasso", "Parks & Recreation", "Vikings", "Suits", "Breaking Bad"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[9, 4, 34], [9, 7, 125], [9, 6, 89], [8, 9, 134], [10, 5, 62]]

#pd.DataFrame() é o objeto constrrutor da classe DataFrame, que cria um df
#a partir do que passarmos. Recebe qualquer iterável como parâmetro.
df = pd.DataFrame(dados, index = indices, columns= colunas)

print(df)
print("_"*60)

#Seleção de colunas
print("Nota:")
print(df["Nota"], "\n")
print("Temoradas:")
print(df["Temporadas"], "\n")
print("_"*60)

print("Nota e episódios:")
print(df[["Nota", "Episódios"]], "\n")
print("_"*60)

#Seleção de linhas
#Como as linhas têm rótulos, vamos usá-los
print("Suits (loc):")
print(df.loc["Suits"], "\n")

#podemos usar o índice implícito
print("Suits (iloc):")
print(df.iloc[3])
print("_"*60)

#Selecionando linhas e colunas
print("Nota de Suits (loc):", df.loc["Suits", "Nota"]) #automaticamente, o 
#primeiro parâmetro é a linha e o segundo é a coluna
print(type(df.loc["Suits", "Nota"]))
print("Nota de Suits (iloc):", df.iloc[3,0]) #aqui, os índices são ao contrário

#este é mais rápido pq é feito para pegar o valor de células
print("Nota de Suits (at):", df.at["Suits", "Nota"])
print("_"*60)

print("Ted Lasso e Parks & Recreation, Nota e Temporadas:")
print(df.loc[["Ted Lasso", "Parks & Recreation"], ["Nota", "Temporadas"]], "\n")

#Usando slice para fazer um minidf
print("Ted Lasso até Suits, Temporadas e Episódios:")
print(df.loc["Parks & Recreation":"Suits", "Temporadas":])
print("_"*60)

#Operações
print(df.head(2))
print(df.tail(2), "\n")
print("Valores únicos de Nota:")
print(df["Nota"].unique())
print("Número de valores únicos de Nota:")
print(df["Nota"].nunique())
print("Contagem de Nota:")
print(df["Nota"].count())
print("Contagem de valores de Nota:")
print(df["Nota"].value_counts(), "\n")

df.at["Vikings", "Nota"] = 5
print("Valores únicos de Nota:")
print(df["Nota"].unique())
print("Número de valores únicos de Nota:")
print(df["Nota"].nunique())
print("Contagem de Nota:")
print(df["Nota"].count())
print("Contagem de valores de Nota:")
print(df["Nota"].value_counts(), "\n")

print("Nota mínima dos dados:", df["Nota"].min())
print("Nota máxima dos dados:", df["Nota"].max())
print("Nota média dos dados:", df["Nota"].mean())
print("_"*60)

print(df.columns)
print(df.columns.to_list(), "\n")

print(df.index)
print(df.index.to_list())
print(df.index.to_numpy())
print(df.index.values)
print("_"*60)

df["Coluna Extra"] = df["Nota"]/2
print(df)
print("_"*60)

#percorrendo as colunas: axis = 0 (padrão); percorrendo as linhas: axis = 1
#o drop retorna um df sem a coluna, mas não substitui o original, a menos que
#usemos inplace = True
df.drop("Coluna Extra", axis = 1, inplace = True)
print(df)
print("_"*60)
df.drop("Vikings", inplace = True)
print(df)
