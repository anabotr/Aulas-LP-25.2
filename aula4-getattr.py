# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 08:00:58 2025

@author: C3007784
"""

def aplicar(objeto, nome, *args, **kwargs):
    if not hasattr(objeto, nome):
        raise AttributeError(f"{type(objeto).__name__} não tem {nome}")
    
    atributo = getattr(objeto, nome)
    
    if callable(atributo):
        return atributo(*args, **kwargs)
    
    raise TypeError(f"{nome} não é invocável em {type(objeto).__name__}")
    

texto_1 = '  EMAp     '
texto_2 = 'banana'

#print(aplicar(texto_1, "strip"))
#print(aplicar(texto_1, "stripa"))
#print(aplicar(texto_2, "replace", "a", "@"))

