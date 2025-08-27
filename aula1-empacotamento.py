# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

tupla = (10,20,30,40,50)


'''
- quando usamos tuplas e não sabemos o número de valores, podemos pegar
 os excedentes e colocá-los numa variável só em forma de lista usando *
 
- uma variável chamada _ significa que ela não será usada futuramente em python
 '''

a,*b,c = tupla


item = tupla[1]
#print(item)

#------------------------------------------------------------------------------

def somar_tudo(a,b,c):
    return a+b+c

numeros = [1,2,3]
#print(somar_tudo(*numeros))

#------------------------------------------------------------------------------

def apresentar(nome, idade):
    return f"{nome} tem {idade} anos"

pessoa = {"nome":"Arthur", "idade":19}

#print(apresentar(**pessoa))

#------------------------------------------------------------------------------

def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave} = {valor}")

#mostrar_info(nome="Arthur", idade=19, altura = 176)

#------------------------------------------------------------------------------

d1 = {'a':1, 'b':2}
d2 = {'b':99, 'c': 3}

d3 = {**d1, **d2} 
'''Ele desempacota e as chaves-valor de d1 são adicionadas a d3, já as de d2,
sobrescrevem as de d1 com chave igual e adicionam as que não exitem'''

#print(d3)

#------------------------------------------------------------------------------

def relatorio(*args, **kwargs):
    # args = argumentos nomeados
    # kwargs = argumentos não nomeados
    
    print("Participantes:")
    for nome in args:
        print(f" - {nome}")
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")

#relatorio("Ana", "Arthur", "Yuri", tema="Anime", duração='2h')