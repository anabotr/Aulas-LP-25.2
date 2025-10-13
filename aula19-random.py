#Esse arquivo cria uma nova pasta de nome data, com os aquivos vendas.csv e 
#vendas.xlsx

import pandas as pd
import numpy as np
import io
import os
from pathlib import Path

#como não há constantes em python, criamos a variável em caixa alta e esperamos
#que ninguém mexa nela
BASE = Path(__file__).parent if "__file__" in globals() else Path(".")

#aqui, o operador / serve parea concatenar caminhos, neste caso, estamos 
#criando um diretório de nome data e nele guardaremos os dados
DATA_DIR = BASE / "data"
#essa linha garante que não se sobrescreverá
DATA_DIR.mkdir(exist_ok = True)

np.random.seed(42)

print("_"*60)

#criaremos um dataset com 100 entradas
datasample_size = 100
vendedores = np.random.choice(["Matheus", "Luis Eduardo", "Elias", "Nina", 
                               "Cauã", "Yuri"],
                              size = datasample_size,
                              p=[.15, .15, .20, .20, .15, .15]#probabilidade
                              #de cada um ser sorteado para algum evento
                              )
produtos = np.random.choice(["Pepino", "Café", "Panela", "Cobertor", "DVD",
                             "Marmita"],
                              size = datasample_size,
                              p=[.25, .15, .20, .10, .15, .15]#probabilidade
                              #de cada um ser sorteado para algum evento
                              )

valor_base= {"Pepino" : 50, "Café" : 2, "Panela" : 100, "Cobertor" : 30, 
             "DVD" : 10, "Marmita" : 20}

#precisamos permitir que a função get seja aplicada a vetores: temos um 
#dicionário e queremos pegar um conjunto de valores (vetor)

get_preco = np.vectorize(valor_base.get) #esse método já está ligado ao 
#dicionario valor_base, então sempre que for chamada, vai usar os valores dele

valor_base = get_preco(produtos)

#criamos um ndarray que vai oscilar entre 0.87 e 1.13
valores = valor_base*np.random.normal(1.0, 0.13, size = datasample_size)
valores = np.round(valores, 2)


datas = pd.to_datetime("2025-01-01") + pd.to_timedelta(
    np.random.randint(0,90, size = datasample_size), unit = "D")
#o to_timedelta soma uma delta a uma data escolhida, precisamos dizer a unidade
#de "medida" da soma, no nosso caso é "D" -> dia
#usamos o randint para randomizar isso, dizendo que o número de dias somados
#vai variar de 0 a 90

#aqui fizemos inconsistências intencionais, como se o usuário tivesse feito
#quando colocamos algum dados bruto (não tratado), colocamos _raw no nome
regioes_raw = np.random.choice(["sul", "norte", "sudeste ", "Sudeste", 
                           "Centro-oeste", "Nordeste"], size = datasample_size)

#aqui, vamos colocar erros na coluna de preços
#aqui, estamos sorteando um número datasample_size vezes, toda a vez que ele for
#menor do que 0.07, teremos True, então estamos fazendo um vetor com valores
#booleanos, que, em média, têm 7% de True 
mascara_de_erros = np.random.rand(datasample_size) < 0.07
valores[mascara_de_erros] = np.nan

#aqui, pegaremos 7 índices do dataset, que não podem ser dupliados entre eles
#(replace garante isso) e criamos um array com eles
duplicatas = np.random.choice(np.arange(datasample_size), size = 7, 
                              replace = False)

#dataset bruto/não tratado
#chave: nome da coluna, valor: ndarray/lista/tupla, e ele espera que todos os 
#valores tenham mesmo tamanho
df_raw = pd.DataFrame({"Vendedor" : vendedores, "Produto": produtos, "Valor" : 
                       valores, "Região": regioes_raw, "DataVenda" : datas})


#Quando achamos que pode ter colisão de índice, ignoramos os índices já
#existentes nos dfs
#o concat cria novos índices

#nessa linha, estamos colcoando ao final do df as linhas duplicadas
df_raw = pd.concat([df_raw, df_raw.iloc[duplicatas]], ignore_index = True)

print(df_raw)

csv_path = DATA_DIR/"vendas.csv"
xlsx_path = DATA_DIR/"vendas.xlsx"

#esse parâmetro index desconsidera o índice da base de dados na hora de salvar
#o encoding tenta ser o mais geral (vai dar erro no índice)
df_raw.to_csv(csv_path, index = False, encoding = "utf-8")

#para salvar em excel, precisamos de um objeto writer
#with é um gerenciador de contexto, eles protegem de exceções
with pd.ExcelWriter(xlsx_path) as writer:
    df_raw.to_excel(writer, index = False, sheet_name = "Vendas")