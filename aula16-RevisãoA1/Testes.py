
import unittest

def processar_texto(texto):
    """_summary_

    Args:
        texto (_type_): _description_

    Returns:
        _type_: _description_

    Examples:
        >>> print(processar_texto("ana"))
        ana

        >>> print(processar_texto("Ana"))
        ana

        >>> print(processar_texto("Ana123"))
        ana123

        >>> print(processar_texto("ana banana"))
        ana banana

        >>> print(processar_texto("ana ? 34 "))
        ana  34
    """
    texto = texto.lower().strip()
    texto_final = ''
    for i in range(len(texto)):
        if texto[i].isalnum() or texto[i] == " ":
            texto_final += texto[i]
    return texto_final



class TestTexto(unittest.TestCase):

    def test_tudo_minusculo(self):
        self.assertEqual(processar_texto("ana"), "ana")
    
    def test_com_maiuscula(self):
        self.assertEqual(processar_texto("Ana"), "ana")
    
    def test_com_numeros(self):
        self.assertEqual(processar_texto("Ana123"), "ana123")

    def test_com_espaco_no_meio(self):
        self.assertEqual(processar_texto("ana banana"), "ana banana")

    def test_com_espaco_no_final(self):
        self.assertEqual(processar_texto("oi     "), "oi")

    def test_com_not_alnum(self):
        self.assertEqual(processar_texto("ana ? 34 "), "ana  34")

if __name__ == "__main__":
    unittest.main()



