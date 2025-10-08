import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #para usar o método show

df = pd.read_json("pandas_aula_02.json")
print(df)
print(df.dtypes)
print("_"*60)

#a coluna month está como objeto, então vamos formatar ela para ser do tipo data
df["month"] = pd.to_datetime(df["month"])
print(df)
print(df.dtypes)
print("_"*60)

#vamos tirar os nomes de filmes dos índices, pq não seria legal mexer com isso
#no código
df = df.set_index("month").sort_index()
print(df.head(5))
print("_"*60)


#gráfico de linhas
#usando o plot do pandas
ax = df.plot(figsize = (8,4), title = "Evolução Mensal de Visualizações por Série")
ax.set_xlabel("Mês")
ax.set_ylabel("Número de visualizações")
plt.show() #aqui usamos o matplotlib.pyplot

#gráfico de barras
totais = df.sum(axis =0).sort_values(ascending = False)
ax = totais.plot(kind = "bar", rot = 45, title = "Total de Visualizações por série")
#rot = 45 é pra definir a rotação dos títulos do eixo x
ax.set_xlabel("Série")
ax.set_ylabel("Total de visualizações")
plt.show()

#gráfico de barras horizontais
medias = df.mean(axis = 0).sort_values(ascending = False)
ax = medias.plot(kind = "barh", title = "Média de Visualizações por série")
ax.set_xlabel("Média")
ax.set_ylabel("Série")
plt.show()

#gráfico de pizza
top3 = totais.head(3)
ax = top3.plot(kind="pie", autopct = "%1.1f%%", ylabel="", title = "Participação das Top 3 séries")
plt.show()

#histograma
ax = df["Dexter"].plot(kind = "hist", bins = 5, title = "Distribuição de Visualizações - Dexter")
ax.set_xlabel("Visualizações")
plt.show()

#box plot
ax = df.plot(kind = "box", rot = 45, title = "Boxplot das Visualizações por Série")
plt.show()

#dispersão
ax = df.plot(kind = "scatter", x = "Breaking Bad", y = "Dexter", title = "Sem sentido, como a vida")
plt.show()