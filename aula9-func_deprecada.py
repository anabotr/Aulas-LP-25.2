# -*- coding: utf-8 -*-

#Deprecamos uma função para dar tempo de os clientes de adaptarem a mudanças
#que fizermos

import math
import warnings


#Criamos uma função que vai morrer
def funcao_antiga(valor: float) -> float:
    """ [DEPRECATED] funcao_antiga: use 'math.sqrt'
    
    Função que retorna a raiz quadrada

    Parameters
    ----------
    valor : float
        Valor inicial.

    Returns
    -------
    float
        Quadrado do valor dado.


    Esta função será removida no versão 2.6.9 da aplicação.
    """
    #Aqui, deprecamos a função
    warnings.warn(
        "funcao_antiga está deprecada e será removida em versão futura. Use \"math.sqrt\".",
        category= DeprecationWarning,
        stacklevel = 2)
    
    #Stacklevel diz pra onde o python vai "apontar" a mensagem de deprecado.
    #Ele pode apontar pra quem chamou o código ou pro código que é o problema.
    #2 aponta para o código da pessoa onde ela chamou a função.
    #1 aponta para o código fonte onde a função foi criada
    
    return math.sqrt(valor)


print(funcao_antiga(16))