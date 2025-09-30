from typing import Callable, Iterable, List, Sequence, Tuple
import numpy as np
import unittest

def normalizar_matriz(matriz : Iterable) -> Iterable:
    """Função para normalizar matrizes

    Args:
        matriz (Iterable): np.array a ser normalizado

    Returns:
        Iterable: matriz já normalizada

    Examples:
        >>> print(normalizar_matriz(np.array([[2,4,8],[2,4,8]])))
        [[0.25 0.5  1.  ]
        [0.25 0.5  1.  ]]

        >>> print(normalizar_matriz(np.array([[1 1 1],[1 1 1]]))
        [[1. 1.  1.  ]
        [1. 1.  1.  ]]
    """
    matriz = np.array(matriz)
    divisor = matriz.max()
    if divisor == 0:
        return matriz
    else:
        nova_matriz = matriz/divisor
        return nova_matriz
    
first = normalizar_matriz(np.array([[2,4,8],[2,4,8]]))
print(first) 
second = [[0.25, 0.5,  1.  ],[0.25, 0.5,  1.  ]]

print(first == second)

class TestNormalizar(unittest.TestCase):
    def test_matriz_padrao(self):
        matriz = np.array([[2, 4, 8], [2, 4, 8]])
        esperado = np.array([[0.25, 0.5, 1.0],
                             [0.25, 0.5, 1.0]])
        np.testing.assert_array_almost_equal(normalizar_matriz(matriz), esperado)

    def test_matriz_zeros(self):
        matriz = np.array([[0, 0], [0, 0]])
        esperado = np.array([[0, 0], [0, 0]])
        np.testing.assert_array_equal(normalizar_matriz(matriz), esperado)

    def test_matriz_todos_iguais(self):
        matriz = np.array([[5, 5], [5, 5]])
        esperado = np.array([[1, 1], [1, 1]])
        np.testing.assert_array_equal(normalizar_matriz(matriz), esperado)

    def test_matriz_unitaria(self):
        matriz = np.array([[1, 1, 1], [1, 1, 1]])
        esperado = np.array([[1, 1, 1], [1, 1, 1]])
        np.testing.assert_array_equal(normalizar_matriz(matriz), esperado)



if __name__ == "__main__":
    unittest.main()
    