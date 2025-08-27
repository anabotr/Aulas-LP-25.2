# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 08:18:09 2025

@author: C3007784
"""

texto = '   EMAp  '

#print(texto.strip())

nome_metodo = 'strip'
#print('todos os métodos disponíveis para uma string:')
#print(dir(texto))
#print('#'*80)


"""bound method: quando você extrai um aributo de um objeto, o atributo fica 
ligado ao objeto do qual ele foi extraido, de modo que depois basta chamar
o atributo usando atributo(), e ele irá aplicar ao objeto original"""

if hasattr(texto, nome_metodo):
    var = getattr(texto, nome_metodo)
    texto = var(texto)
    #print(texto)
    #print("Antes de invocar o método:", texto)
    #print(var(""))
    #print(var())
    #ou var() com qualquer coisa dentro do parêntese
    #print("Após invocar o método", texto)
else:
    #print(f"O método \"{nome_metodo}\" não existe no objeto")
    pass
    
#a \" é pra " ser interpretada como texto em uma string

#------------------------------------------------------------------------------
def exibir_evento(mensagem):
    print("Evento:", mensagem)
    
exibir_evento.contador = 0
exibir_evento.log = []

#print(exibir_evento.__dict__)

''' toda a função é um dicionário, toda a vez que você acessa uma coisa que não
existe em uma função, ela é criada no método __dict__'''

def registrar_evento(mensagem):
    exibir_evento.contador += 1
    exibir_evento.log.append(mensagem)
    exibir_evento(mensagem)
    #print(f"Chamadas até agora: {exibir_evento.contador}")
    #print(f"Histórico: {exibir_evento.log}")
    #print("-"*129)
    
#registrar_evento('Sistema Iniciado')
#registrar_evento('Usuário Autenticado')
#registrar_evento('Navegador Iniciado')
#registrar_evento('Instagram Acessado')

#------------------------------------------------------------------------------
def saudador(pessoa):
    saudacao = 'Bem-vindo'
    
    def mensagem(): 
        print('Eu sou a MENSAGEM')

    mensagem()
    #return mensagem()
    return f'{saudacao},{pessoa}'

#print(saudador('joao'))
    
    
#metodos e funções são qualquer coisa :( sad 
#funções de primeira ordem 

#print(saudador.__code__)
#print(dir(saudador.__code__))    
#print(saudador.__code__.co_consts)    
#print(dir(saudador.__code__.co_consts))    
    
#print(hasattr(saudador.__code__.co_consts, '__iter__')) #é interavel
#print(hasattr(saudador.__code__.co_consts, '__next__')) #não é interador 

for cada_constante in saudador.__code__.co_consts:
    if isinstance(cada_constante, type(saudador.__code__)): 
#verificando cada item se é igual ao mesmo tipo de codigo que tá no saudador
#dentro de co_consts tem codigo? se sim, são códigos dentro da minha função? 
        #print(f'Função interna detectada: {cada_constante.co_name}')
        pass
    
    