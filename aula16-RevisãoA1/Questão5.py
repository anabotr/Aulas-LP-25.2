from typing import Callable, Iterable, List, Sequence, Tuple
import time

def registrar_execucao(func) -> Callable:
    """Decorador que emite uma mensagem com a hora de execução da função

    Args:
        func (_type_): função a ser decorada
    """
    def wrapper(*args, **kwargs):
        hora = time.ctime()
        print(f"Iniciando a função {func.__name__}, chamada em {hora}")
        resultado = func(*args, **kwargs)
        if resultado is not None:
            print(resultado)
        print(f"Finalizando a função {func.__name__}, chamada em {hora}")
        return "" #pro decorador não retornar none

    return wrapper

@registrar_execucao
def oi():
    print("olá")
    return

@registrar_execucao
def multiplicar(x,y):
    return(x*y)



oi()
print(multiplicar(2,5))