import numpy as np
import pandas as pd

indices = ["Ted Lasso", "Parks & Recreation", "Vikings", "Suits", "Breaking Bad"]
colunas = ["Nota", "Temporadas", "Episódios"]
dados = [[9, 4, 34], [9, 7, 125], [9, 6, 89], [8, 9, 134], [10, 5, 62]]

df = pd.DataFrame(dados, index = indices, columns= colunas)


print(df["Nota"] > 8 ) 
print("_"*60)

#ganhamos uma série -> nome para a sequência 
print(df[(df["Nota"] > 8) & (df["Temporadas"] > 6 )])
print("_"*60)

#retorna somente uma série de acordo com o filtro
print(df[(df["Nota"] > 8) | (df["Temporadas"] > 6 )])
print("_"*60)

indices = ["Aluno 1","Aluno 2", "Aluno 3"]
colunas = ["nome", "idade", "matricula"]
dados = [["Nome 1", 15,100],["Nome 2", 21, np.nan],["Nome 3",18, 102]]

df = pd.DataFrame(dados, index=indices, columns=colunas)
print(df)
print("_"*60)
print(df.isnull())
print("_"*60)
print(df["matricula"].isnull())
print("_"*60)
print(df[df["matricula"].isnull()],sep="")
print("_"*60)
print(df.dropna(thresh=2, inplace=True)) 
# o thresh diz limite mínimo de valores não nulos necessários para manter a linha
print("_"*60)
print(df.fillna(101, inplace=True))
print(df)

#TODO entender dropna e fillna 