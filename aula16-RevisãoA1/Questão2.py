def converter_celsius_para_fahrenheit(temperaturas : list[int | float]) -> list[float]:
    """ Função que converte uma lista de temperaturas em graus celsius para 
    graus fahrenheit.

    Parameters
    ----------
    temperaturas : list[int | float]
        Lista de temperaturas em graus celsius, os valores devem ser inteiros 
        ou floats.

    Raises
    ------
    ValueError
        Ocorre se não for passada uma lista como argumento ou se houverem 
        valores não numéricos na lista de temperaturas passada.

    Returns
    -------
    list[int | float]
        Lista com os valores devidamente convertidos para Fahrenheit arredondados
        para duas casas decimais.
    
    Examples:
    -------
        >>> converter_celsius_para_fahrenheit([0, 7])
        [32.0, 44.6]
        >>> converter_celsius_para_fahrenheit([12.5, 7.9, 10])
        [54.5, 46.22, 50.0]
        >>> converter_celsius_para_fahrenheit("até amanhã")
        Traceback (most recent call last):
            ...
        ValueError: Deve ser fornecida uma lista com as temperaturas
        >>> converter_celsius_para_fahrenheit([34, 'oie', 1])
        Traceback (most recent call last):
            ...
        ValueError: Impossível converter valores não numéricos

        
    """
    
    fahrentheit = []
    if not isinstance(temperaturas, list):
        raise ValueError("Deve ser fornecida uma lista com as temperaturas")
        
    
    for temp_c in temperaturas:
        if not isinstance(temp_c, (float, int)):
            raise ValueError("Impossível converter valores não numéricos")
        temp_f = 1.8*float(temp_c) + 32
        temp_f = round(temp_f, 2)
        fahrentheit.append(temp_f)
        
    return fahrentheit
        

import doctest

if __name__ == "__main__":
    print(doctest.testmod())
    