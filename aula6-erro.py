# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 07:47:52 2025

@author: C3007784
"""

import doctest

def soma(num1, num2):
    """
    Soma dois números inteiros
        
    :param num1: int
    :param num2: int
    :return: int
        
    >>> soma(7,0)
    7
    
    >>> soma(42,666)
    708
    
    >>> soma(-13,10)
    -3
    
    >>> soma(100,"Carlos Ivan")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    
    return num1 + num2

""" o módulo doctest tem a função testmod que vai testar todo o código, 
inclusive a parte do docstring que tem >>>soma(x,y) vai testar o programa e ver
se ele retorna o mesmo resultado que está na linha de baixo. Se falharem algum 
deles, o código dá erro, se não falhar, não retorna nada"""

"""No caso da soma entre string e numero, se colocarmos a exata mensagem de 
erro do console, ele aceita.
Precisamos colocar a primeira e a última lina da entrada, separadas por uma
linha com reticências"""


if __name__ == "__main__":
    doctest.testmod()    
    
    
    
    """
    HIERARQUIA DE ERROS
    
    BaseException
     ├── BaseExceptionGroup
     ├── GeneratorExit
     ├── KeyboardInterrupt
     ├── SystemExit
     └── Exception
          ├── ArithmeticError
          │    ├── FloatingPointError
          │    ├── OverflowError
          │    └── ZeroDivisionError
          ├── AssertionError
          ├── AttributeError
          ├── BufferError
          ├── EOFError
          ├── ExceptionGroup [BaseExceptionGroup]
          ├── ImportError
          │    └── ModuleNotFoundError
          ├── LookupError
          │    ├── IndexError
          │    └── KeyError
          ├── MemoryError
          ├── NameError
          │    └── UnboundLocalError
          ├── OSError
          │    ├── BlockingIOError
          │    ├── ChildProcessError
          │    ├── ConnectionError
          │    │    ├── BrokenPipeError
          │    │    ├── ConnectionAbortedError
          │    │    ├── ConnectionRefusedError
          │    │    └── ConnectionResetError
          │    ├── FileExistsError
          │    ├── FileNotFoundError
          │    ├── InterruptedError
          │    ├── IsADirectoryError
          │    ├── NotADirectoryError
          │    ├── PermissionError
          │    ├── ProcessLookupError
          │    └── TimeoutError
          ├── ReferenceError
          ├── RuntimeError
          │    ├── NotImplementedError
          │    ├── PythonFinalizationError
          │    └── RecursionError
          ├── StopAsyncIteration
          ├── StopIteration
          ├── SyntaxError
          │    └── IndentationError
          │         └── TabError
          ├── SystemError
          ├── TypeError
          ├── ValueError
          │    └── UnicodeError
          │         ├── UnicodeDecodeError
          │         ├── UnicodeEncodeError
          │         └── UnicodeTranslateError
          └── Warning
               ├── BytesWarning
               ├── DeprecationWarning
               ├── EncodingWarning
               ├── FutureWarning
               ├── ImportWarning
               ├── PendingDeprecationWarning
               ├── ResourceWarning
               ├── RuntimeWarning
               ├── SyntaxWarning
               ├── UnicodeWarning
               └── UserWarning

    """
    
x = 10
y = 0



try: 
    resultado = x/y
except ZeroDivisionError as erro:
    print("Erro", type(erro), erro.__class__.mro())
    resultado = "Erro de divisão por zero"
except ArithmeticError as erro:
    print("Erro", type(erro), erro.__class__.mro())
    resultado = "Erro aritmético"
except NameError as erro:
    print("Erro", type(erro), erro.__class__.mro())
    resultado = "Erro de nome"
except Exception as erro: #pega tudo
    print("Erro", type(erro), erro.__class__.mro())
    resultado = "Erro não previsto"
    
print(resultado)
    