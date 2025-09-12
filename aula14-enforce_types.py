#Aula 13 e 14 - 10 e 12 de setembro

import inspect
from functools import wraps
#queremos criar um decorador para verificar se os tipos foram passados corretamente

def enforce_types(func):
    assinatura = inspect.signature(func) #pega a assinatura da função, que é 
    #como "nome_func(param1 : tipo1, param2: tipo2, ...) -> tipo returns
    
    #print("Assinatura:", str(assinatura))
    pass
    
    anotacoes = func.__annotations__ #pega as anotações da função, que é como
    #{'param1': classe1, 'param2':classe2, ..., 'return': classereturn}
    
    #print("Anotações", anotacoes)
    pass
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = assinatura.bind(*args, **kwargs) #organiza os argumentos
        bound.apply_defaults() #garante que se o usuário não passar os argumentos
        #definidos com default, não dará erro
        
        #print("Bound:", str(bound))
        #print("Bound Arguments:", str(bound.arguments))
        
        for nome_param, valor in bound.arguments.items():
            if nome_param in anotacoes: #vê se os parâmetros foram tipados, se
            #for, entra dentro do if, senão, passa direto
                tipo_esperado = anotacoes[nome_param]
                #lista[str] e etc dificultam muito a verificação, então vamos
                #nessa aula, cuidar apenas dos tipos básico, como list, str, int
                #se houver mais de um tipo possível para a variável, precisamos
                #fazer uma verificação usando or
                if not isinstance(tipo_esperado, type): #verifica se o tipo 
                #esperado é uma classe, ou seja, não cuidaremos de list[str] etc
                    raise TypeError(f"Anotação para \"{nome_param}\" utiliza tipo não suportado")
                if not isinstance(valor, tipo_esperado): #verifica se o tipo
                #da variável usada é o mesmo tipo que é requerido
                    raise TypeError(f"Argumento para \"{nome_param}\" esperado: \"{tipo_esperado!r}\", argumento recebido: \"{type(valor)!r}\"")
            
        resultado = func(*args, **kwargs)
        
        #ainda temos que verificar se a função retorna o que queremos
        if "return" in anotacoes: #primeiro vê se o retorno ta especificado
            tipo_retorno = anotacoes['return']
            if not isinstance(tipo_retorno, type): #verifica se o tipo 
            #do retorno é uma classe, ou seja, não cuidaremos de list[str] etc
                raise TypeError(f"Anotação de retorno utiliza tipo não suportado : \"{tipo_retorno!r}\"")
            if not isinstance(resultado, tipo_retorno): #verifica se o o tipo
            #do resultado é o tipo que esperávamos no resultado
                raise TypeError(f"Retorno de \"{func.__name__}\" esperado: \"{tipo_retorno!r}\", argumento recebido: \"{type(resultado)!r}\"")
        
        return resultado 
    
    return wrapper
                    

@enforce_types
def concatena (texto_esquerda: str, texto_direita:str) -> str:
    return texto_esquerda + texto_direita
@enforce_types
def area_retangulo(base:float, altura:float) -> float:
    return base*altura

print(concatena("eu adoro ", "a EMAp"))
print(area_retangulo(10.3, 15.8))
print(area_retangulo("3.0", 15.0))