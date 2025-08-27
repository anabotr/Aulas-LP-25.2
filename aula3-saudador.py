# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 08:32:49 2025

@author: C3007784
"""

def saudador(pessoa):
    saudacao = "Bem-vindo"
    
    def mensagem():
        return f"{saudacao} {pessoa}!"
    
    return mensagem

mensagem_jose = saudador("José")
mensagem_beatriz = saudador("Beatriz")

#print(mensagem_jose())
#print(mensagem_beatriz())

#print(mensagem_beatriz.__closure__)

'''O closure é onde ficam armazenadas as variáveis da função, é como se fosse 
uma foto da função (?) '''


for cada_celula in mensagem_beatriz.__closure__:
    #print(cada_celula.cell_contents)
    pass

#------------------------------------------------------------------------------

def criar_contador(nome):
    numero = 0
    
    def proximo():
        nonlocal numero
        numero += 1
        print(f'Contador {nome} : {numero}')
        return numero
    
    return proximo

contador_downloads = criar_contador("downloads")
contador_likes = criar_contador("likes")
        
# contador_downloads()
# contador_likes()
# contador_downloads()

#------------------------------------------------------------------------------

import numpy as np

def criar_normalizador(base_min, base_max):
    intervalo = base_max - base_min
    
    def normalizar(numpy_array):
        return (numpy_array - base_min) / intervalo
            

    return normalizar

dados = np.array([10,15,20,25,30])
dados2 = np.array([8,11,17,14,10])
normalizador = criar_normalizador(10,30)
normalizador2 = criar_normalizador(8,17)

#print("Dados normalizados 10-30:", normalizador(dados))
#print("Dados normalizados 8-17:", normalizador2(dados2))

def criar_filtro_mediana(referencia):
    def filtrar(numpy_array):
        return(numpy_array[numpy_array > np.median(referencia)])
    
    return filtrar

valores = np.array([1,5,7,10,15,18])
filtro_mediana_1 = criar_filtro_mediana(valores)
print("Valores acima da mediana:", filtro_mediana_1(valores))





