# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 07:52:23 2025

@author: C3007784
"""

import modulo

def meu_decorador(funcao_original):
    def nova_funcao():
        print("algo bem foda antes da funcao")
        funcao_original()
        print("algo depois da função")
        
    return nova_funcao

def diga_ola():
    print("Olá!")
    
def diga_tchau():
    print("Tchau!")
  
    
'''Aqui, decoramos a função na sua criação, sem precisar criar um 
diga_tudobem_decorado'''
@meu_decorador
def diga_tudobem():
    print("Tudo bem?")
    
#diga_ola_decorado = meu_decorador(diga_ola)
#diga_ola_decorado()
#diga_tchau()
#diga_tudobem()

from functools import wraps

def log_args(func):
    '''o @wraps(func) pega todos os dados de func e dá para wrapper, serve para
que a função wrapper não oculte a função decorada'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Decorador!

        Parameters
        ----------
        func : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        
        print(f"Chamando função {func.__name__} com args={args} e kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
        
def dobra_wrapper(func):
    def wrapper(*args, **kwargs):
       resultado = func(*args, **kwargs)
       return resultado*2
    return wrapper


'''Aqui, primeiro é aplicado dobra_wrapper e depois o log_args'''
@log_args
@dobra_wrapper
def somar(a,b):
    return a + b

@log_args
def subtrair(a,b):
    """
    Subtrair

    Parameters
    ----------
    a : TYPE
        DESCRIPTION.
    b : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return a - b
    

#print("Resultado:", somar(1,41))


'''A função decorada é a wrapper, então ela toma conta dos atributos de 
subtrair'''
#print(subtrair.__name__)
#print(subtrair.__doc__)

import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executada em {fim-inicio:.4f} segundos")
        return resultado
    return wrapper


@medir_tempo
def tarefa_lenta():
    time.sleep(5)
    return "concluida"

print(tarefa_lenta())