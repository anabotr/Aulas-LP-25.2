from typing import Callable, Iterable, List, Sequence, Tuple

def multiplicador(n: int|float) -> Callable:
    """ Função que cria um multiplicador por um número fixo n.
    Esse multiplicador retorna outro objeto função, que receberá um valor x 
    fornecido pelo usuário, que será multiplicado por n sempre que a função 
    definida anteriormente for chamada.
    

    Parameters
    ----------
    n : int|float
        número que será o multiplicador fixo na função retornada.

    Returns
    -------
    Callable
        Objeto executável que, ao receber um valor , retornará a multiplicação 
        deste valor fornecido com o valor definido em sua criação.

    """
    if not isinstance(n, (int, float)):
        raise ValueError("O valor fornecido deve ser numérico")
    
    def multiplica_inner(x: int|float):
        if not isinstance(x, (int, float)):
            raise ValueError("O valor fornecido deve ser numérico")
        return x*n
        
    return multiplica_inner

duplica = multiplicador(2)
triplica = multiplicador(3)

print(duplica(5))
print(triplica(5))
print(duplica(64))
print(triplica(64))
print(duplica('oi'))