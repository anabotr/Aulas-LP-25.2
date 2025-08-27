# -*- coding: utf-8 -*-
"""
Módulo de Matemática Financeira
"""

#Fórmula que calcula montante e juros simples em um regime de juros simples
def juros_simples(capital: int, taxa: int, tempo: int) -> tuple:
    
    #Fórmula padrão de juros simples
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    
    #TODO: Utilizar números de ponto flutuante nesta função
    
    return (montante, juros)


#Docstring NumPy/SciPy
def juros_compostos(capital: int, taxa: int, tempo: int = 1) -> tuple:
    """
    Cálculo de juros compostos

    Parameters
    ----------
    capital : int
        Valor inicial utilizado para a base do cálculo.
    taxa : int
        Taxa de juros.
    tempo : int, optional
        Tempo total, seu valor padrão é 1.

    Returns
    -------
    tuple
        Tupla contendo montante e juros, nesta ordem.

    """
    
    montante = capital*pow(1 + taxa/100, tempo)    
    juros = montante - capital
    
    return(round(montante, 2), round(juros, 2))