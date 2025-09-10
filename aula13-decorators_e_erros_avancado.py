import time
from functools import wraps

contador_falhas = 0 #usado para simular falhas e depois sucesso

#vamos criar um decorador retry, que vai repetir a função retries (3) vezes, 
#vai esperar delay (1000 milissegundos) para executar de novo, se ocorrer
#uma exception (valueerror), ele não vai quebrar o programa, o backoff 
#significa que a cada execução, será dobrado o tempo de espera

def retry(retries = 3, exceptions = (ValueError,), delay = 0.1, backoff = 2.0):
    #validação básica de parâmetro
    if not isinstance (retries, int) or retries < 1:
        raise ValueError("retries deve ser int e >= 1")
    if not isinstance(delay, (int, float)) or delay < 0:
        raise ValueError("delay deve ser int ou float e >= 0")
    if not isinstance(backoff, (int, float)) or backoff < 1:
        raise ValueError("backoff deve ser int ou float e >= 1.0")
        
    if not isinstance(exceptions, tuple):
        exceptions = (exceptions, )
    for exc in exceptions:
        if not (isinstance(exc, type) and issubclass(exc, BaseException)):
            raise TypeError("exception deve conter classes derivadas de BaseException")
    
    
    def decorador(func):
        #o wraps mantém os dados originais da função em vez de mudar para wrapper
        @wraps(func)
        def wrapper(*args, **kwargs):
            tentativa_atual = 1
            atraso_atual = float(delay)
            
            while True:
                try:
                    return func(*args, **kwargs)
                #verifica se o exception pegou algo que está no exceptions e
                #define esse exception como err
                except exceptions as err:
                    #se a tentativa atual for maior do que o parâmetro dado, 
                    #ele deixa o erro ocorrer
                    if tentativa_atual >= retries:
                        raise err
                    nome_erro = type(err).__name__
                    msg_erro = str(err) #a maior parte dos objetos em python 
                    #pode ser covertida para string, no caso de exceção, é 
                    #possível e retorna a mensagem do erro, no caso aquele
                    #ValueError("Deu ruim") retorna "deu ruim"
                    
                    print(f"Tentativa {tentativa_atual} falhou ({nome_erro}:{msg_erro}), tentando outra vez em {atraso_atual:.3f}s")                    
                    tentativa_atual += 1
                    if atraso_atual > 0:
                        time.sleep(atraso_atual)
                    atraso_atual *= backoff
            
        return wrapper
    return decorador
            




@retry(retries = 5, exceptions = (ValueError,), delay = 0.1, backoff = 2.0)
def pode_falhar():
    #essa função roda apenas uma vez pq o erro é acionado e sai dela
    global contador_falhas
    
    #falha duas vezes e só então retorna ok
    if contador_falhas < 10:
        contador_falhas += 1
        raise ValueError("Deu ruim!")
    return "Deu bom"


print(pode_falhar())
