import keyword
import re
import unicodedata

__author__ = "Ana"

def _strip_accents(text: str) -> str:
    """
    Função usada para retirar os acentos do texto fornecido, com ajuda do 
    módulo unicode.

    Parameters
    ----------
    text : str
        Texto a ter os acentos retirados.

    Returns
    -------
    str
        Texto sem acentos.

    """
    #Usa uma função do módulo unicode para normalizar o texto em formado NFKD
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))

def normalize_identifier(text, *, allow_leading_underscore=False):
    """
    Converte um texto em identificador “seguro” para código: minúsculo, sem acento,
    separadores como "_" (colapsados), sem "_" nas pontas (opcional no início) e
    com sufixo "_" se for palavra reservada de Python.

    Parameters
    ----------
    text : str
        O texto que será modificado.
        
    allow_leading_underscore : bool, optional.
        Define se são permitidos underscores à esquerda do texto seguro. 
        O padrão é False.

    Raises
    ------
    TypeError
        A entrada não é uma string.
    ValueError
        O texto seguro é vazio.

    Returns
    -------
    safe : str
        Texto com as modificações necessárias.
        
        
    Examples
    -------
    >>> normalize_identifier('textooo o o o o o __')
    'textooo_o_o_o_o_o'
    
    >>> normalize_identifier('textooo o o o o o __', allow_leading_underscore = True)
    'textooo_o_o_o_o_o'
    
    >>> normalize_identifier('__textooo o o o o o __')
    'textooo_o_o_o_o_o'
    
    >>> normalize_identifier('__textooo o o o o o __', allow_leading_underscore = True)
    '_textooo_o_o_o_o_o'
    
    >>> normalize_identifier('__ __ _')
    Traceback (most recent call last):
        ...
    ValueError: empty identifier after normalization
    
    >>> normalize_identifier(False, allow_leading_underscore = True)
    Traceback (most recent call last):
        ...
    TypeError: text must be str

    """

    #Aqui, verificamos se o texto realmente é string. Se não for, levanta um 
    #TypeError
    if not isinstance(text, str):
        raise TypeError("text must be str")
    
    
    #Nesta linha, além de aplicar a função _strip_accents ao texto, colocamos 
    #em minúsculo
    text = _strip_accents(text).lower()
    
    #Se o caracetere for alfanumérico ou um underscore, iremos incluir "" após
    #sua aparição (não mudará nada na string). Caso contrário, será adicionado
    #um underscore.
    safe = "".join(ch if (ch.isalnum() or ch == "_") else "_" for ch in text)
    
    #Essa linha garante que não haja mais de um undersocre consecutivo em safe
    safe = re.sub(r"_+", "_", safe)


    #Verificamos se pode conter underscores à esquerda no texto final
    if allow_leading_underscore:
        #Aqui, verificamos se há um underscore como prefixo do texto formatado
        prefix = len(safe) - len(safe.lstrip("_"))
        
        #Nesta linha, pegamos a string sem prefixo e retiramos os underscores
        #à direita
        core = safe[prefix:].rstrip("_")
        
        #Por fim, refenimos safe como a concatenação entre os underscores do 
        #prefixo e o core
        safe = "_" * prefix + core
        
    else:
        #Esta parte retira os underscores que estão no fim/início da string
        safe = safe.strip("_")

    #Nesta parte, verificamos se safe contém caracteres após a normalização e 
    #retornamos um ValueError em caso negativo
    if not safe:
        raise ValueError("empty identifier after normalization")

    #Verfica se a palavra é uma palavra chave do python, se sim, concatena um 
    #underscore
    if keyword.iskeyword(safe):
        safe += "_"

    return safe

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)