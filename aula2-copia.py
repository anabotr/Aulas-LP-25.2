# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 07:44:56 2025

@author: C3007784
"""

lista_original = [1,2,3]
lista_alias = lista_original
lista_alias[2] = 4

''' temos duas variáveis que "olham" para o mesmo espaço na memória, ou seja,
tem o mesmo id
mudando a lista alias, mudamos também a lista original'''

#print("ID lista original:".ljust(20,'-'), id(lista_original))
#print("ID lista alias:".ljust(20,'-'), id(lista_alias))
#print(lista_original)
#print(lista_alias)

#------------------------------------------------------------------------------
perfil_aluno = {
    "nome":"João",
    "idade":18,
    "preferencias": ['filmes', 'musica', 'livros']}

perfil_aluno_shallow = perfil_aluno.copy()
perfil_aluno_shallow["idade"] = 40
perfil_aluno_shallow["preferencias"][0] = 'teatro'

'''essa é uma cópia rasa, ela só copia em primeiro nível, ou seja, se tem uma
lista dentro de lista, ela não copia o segundo nível, apenas o primeiro e se 
alterar algum nível mais profundo ela vai mudar o original'''

#print(perfil_aluno)
#print(perfil_aluno_shallow)

#------------------------------------------------------------------------------
import copy

perfil_aluno_deep = copy.deepcopy(perfil_aluno)

perfil_aluno_deep['idade'] = 32
perfil_aluno_deep['preferencias'][2] = 'lego'

'''essa é uma cópia profunda, modifica o objeto criado sem mudar o original em 
qualquer nível'''

#print(perfil_aluno_deep)