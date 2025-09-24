import unicodedata
#usaremos essa biblioteca para tirar os possíveis acentos da frase

def contar_vogais(frase : str) -> int:
    """ Função que recebe uma frase e retorna a quantidade de vogais que ela contém
    

    Parameters
    ----------
    frase : str
        Frase da qual contaremos as vogais.

    Raises
    ------
    ValueError
        No caso de não ser fornecida uma string.

    Returns
    -------
    int
        Número de vogais da frase.
        
    Examples:
    -------
        >>> contar_vogais("oi")
        2
        >>> contar_vogais("ana foi à feira e comprou cenoura")
        16
        >>> contar_vogais("até amanhã")
        5
        >>> contar_vogais("xyz")
        0
        >>> contar_vogais([3,1])
        Traceback (most recent call last):
            ...
        ValueError: Insira uma string

    """
    
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    #verifica se uma string foi passada
    if not isinstance(frase, str):
        raise ValueError("Insira uma string")
        
    count = 0
    
    #padronizando a frase
    frase = frase.lower()
    nfkd_form = unicodedata.normalize('NFKD', frase)
    frase = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    
    #conta cada vogal e adiciona o valor no contador
    for vogal in vogais:
        count += frase.count(vogal)
    return count

import doctest

if __name__ == "__main__":
    doctest.testmod()
    
#Driver code
    
frase = input("Digite uma frase:")
print(f"O número de vogais na frase fornecida é {contar_vogais(frase)}")