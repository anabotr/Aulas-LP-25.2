import inspect
from functools import wraps
#queremos criar um decorador para verificar se os tipos foram passados corretamente

def enforce_types(func):
    
    
    pass


@enforce_types
def concatena (texto_esquerda: str, texto_direita:str) -> str:
    return texto_esquerda + texto_direita
@enforce_types
def area_retangulo(base:float, altura:float) -> float:
    return base*altura

print(concatena("eu adoro ", "a EMAp"))
print(area_retangulo(10.3, 15.8))
print(area_retangulo("3.0", 15.0))