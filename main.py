# fazendo teste unitário automatizado
# aula 11 - 05/09

import modulo2 as modulo
import unittest

#cada def é entendido como um teste, independentemente de quantas vezes chamamos
#a função dentro dele
class TestFatorial(unittest.TestCase):
    def test_greather_than_1(self):
        self.assertEqual(modulo.fatorial(2), 2)
        self.assertEqual(modulo.fatorial(3), 6)
        self.assertEqual(modulo.fatorial(4), 24)
        self.assertEqual(modulo.fatorial(5), 120)
    
    def test_lesser_than_1(self):
        self.assertEqual(modulo.fatorial(-1), 1)
    
    def test_equal_to_1(self):
        self.assertEqual(modulo.fatorial(1), 1)
    
    def test_input_type(self):
        self.assertRaises(TypeError, modulo.fatorial, "oi")
    
    def testar_decimal_digits(self):
        num1 = 3.1415926589
        num2 = 3.141592658972323
        digitos_decimais = 9
        
        self.assertAlmostEqual(num1, num2, digitos_decimais)
        
if __name__ == "__main__":
    #executa todos os testes, que foram marcados dentro do def
    unittest.main()