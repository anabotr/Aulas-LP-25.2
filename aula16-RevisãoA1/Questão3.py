import unicodedata
#usaremos essa biblioteca para tirar os possíveis acentos da frase
import unittest

def eh_palindromo(frase: str) -> bool:
    """
    Frase que verifica se uma string fornecida é palíndromo.

    Parameters
    ----------
    frase : str
        String a ser verificada se é palíndromo.

    Raises
    ------
    ValueError
        Ocorre se não for fornecida uma string.

    Returns
    -------
    bool
        True se for palíndromo, False caso contrário.
    
    Examples:
    -------
        >>> eh_palindromo("arara")
        True
        >>> eh_palindromo("hoje é quarta")
        False
        >>> eh_palindromo("subi no ônibus")
        True
        >>> eh_palindromo([34, 'oie', 1])
        Traceback (most recent call last):
            ...
        ValueError: O valor fornecido deve ser uma string.

    """
    
    if not isinstance(frase, str):
        raise ValueError("O valor fornecido deve ser uma string.")
        
    #aqui estamos padronizando a frase: tirando acentos e colocando tudo em minúsculo
    frase = frase.lower()
    nfkd_form = unicodedata.normalize('NFKD', frase)
    frase = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    
    #nesta parte, retirei os espaços da frase
    lista_frase = frase.split()
    frase = "".join([frase for frase in lista_frase])
    
    
    frase_reversa = frase[-1::-1]
    
    return (frase == frase_reversa)

class TestPalindromo(unittest.TestCase):
    def teste_palin_simples(self):
        self.assertTrue(eh_palindromo("arara"))
    
    def teste_palin_case_insensitive(self):
        self.assertTrue(eh_palindromo("ARara"))
    
    def teste_palin_vazio(self):
        self.assertTrue(eh_palindromo(""))
        
    def teste_palin_falso(self):
        self.assertFalse(eh_palindromo("ana beatriz"))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    unittest.main()
