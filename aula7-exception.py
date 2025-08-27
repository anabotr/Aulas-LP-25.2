# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 07:49:57 2025

@author: C3007784
"""

class AppError(Exception):
    """Raiz dos erros de domínio da aplicação"""
    
class AuthenticationError(AppError):
    """Falha de Autenticação (Identidade Inválida)"""

class AuthorizationError(AppError):
    """Falha de autorização (Permissão Inválida)"""

class RateLimiteExceededError (AppError):
    """Cliente excedeu o limite de requisições permitido"""

class ResourceNotFoundError(AppError):
    """Recurso solicitado não foi enconttrado"""
    
def demo_heranca():
    erro = AuthorizationError("Acesso negado a recurso")
    print(erro.args)
    print(str(erro))
    mro_classes = [cls.__name__ for cls in erro.__class__.mro()]
    print(mro_classes)
    
    print(hasattr(erro, "__cause__"))
    print(hasattr(erro, "__context__"))
    print(hasattr(erro, "__traceback__"))
    
def mock_obter_recurso(simular):
    if simular == "authn":
        raise AuthenticationError("Cred inv")
    if simular == 'authz':
        raise AuthorizationError("Cred inv")
    if simular == 'limit':
        raise RateLimiteExceededError("Limite de requisitos excedido")
    return "OK"

def demo_ordem_erros(recurso):
    try:
        resultado = mock_obter_recurso(recurso)
        print(resultado)
    except (AuthenticationError, AuthorizationError) as err:
        print("Fiz um tratamento de erro para (authn, authz):", err)
    except RateLimiteExceededError as err:
        print("Fiz um tratamento de erro para (limit):", err)
    except AppError as err:
        print("Tratamento genérico para qualquer AppError:", err)
    else:
        print("Estou fazendo operações após o sucesso de execução")
    finally:
        print("eu sempre executo")
        
def buscar_em_armazenamento(chave, dicionario):
    try:
        return dicionario[chave]
    except KeyError as err:
        print("Eu estou tratando um pouquinho da exceção")
        raise ResourceNotFoundError(f"Chave ausente: {chave!r}") from err
        
def demo_encadeamento():
    dados = {"login_ativo": True}
    try:
        buscar_em_armazenamento("Carlos Ivan", dados)
    except ResourceNotFoundError as err:
        print("\nEncadeado:", err)
        """Entender o que acontece na próxima linha, pq é importante!"""
        if err.__cause__ is not None: #quero saber se o erro vem de outro erro
            print("Causa original:", (err.__cause__).__class__.__name__, "-", 
                  err.__cause__)
            
        
"""string!r é o mesmo que repr(string), o método repr() representa a 
string de forma crua

string!s é o mesmo que str(string)
string!a é o mesmo que ascii(string)"""
                

if __name__ == "__main__":
    #demo_heranca()
    
    for caso in ["authn", "authz", "limit", "ok"]:
        print(f"\nCaso: {caso}")
        demo_ordem_erros(caso)
        
    demo_encadeamento()