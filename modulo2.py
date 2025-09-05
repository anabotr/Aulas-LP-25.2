#aula 11 - 05/09

def fatorial(num : int) -> int:
    """
    Calcula o fatorial de um num.

    Parameters
    ----------
    num : int
        Número base para o cálculo. Esse número deve ser maior ou igual a zero.

    Returns
    -------
    int
        Fatorial de num.

    """
    
    if num <= 1:
        return 1
    
    return num * fatorial(num-1)
    
    
#teste dinâmico: o código é executado (teste funcional)
#filosofia da caixa preta: não olhamos dentro da unidade, damos uma entrada e 
#vemos se a saída é o que esperávamos

#teste estático: o código é parseado (code review)