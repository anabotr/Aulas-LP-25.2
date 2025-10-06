#QUESTÃO 1
#a)
#enter: wrapper
#exit: wrapper -> 14
#14

#b)

def call_limit(n):
    def interna(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            nonlocal n
            calls += 1
            if calls <= n:
                return func(*args, **kwargs)
            else:
                raise RuntimeError("Número de chamadas excedido")
        return wrapper
    return interna

@call_limit(2)
def somar_valores(left, right):
    return left + right

#print(somar_valores(1, 2)) # ok
#print(somar_valores(2, 3)) # ok
#print(somar_valores(3, 4)) # deve levantar RuntimeError

#c)
#1. Isso pode ocorrer porque quando decoramos somar com double,
#é como se agora somar = double(somar), porém, double retorna wrapper
#então, na verdade é como se fizéssemos somar = wrapper(somar)
#portanto, quando usamos a função 'somar' em trace, estamos na 
#verdade usando wrapper(somar), que tem como atributo __name__ "wrapper".
#Uma forma de corrigir isso é importar o modulo wraps e decorar 
#o wrapper com @wraps.
#2. Quando fazemos isso, primeiro aplicamos trace à função soma
#ou seja, o console log seria o console log de trace sobre somar
#(aqui o func.__name__ é somar) e depois ele duplicado, pois o double
#apenas duplica a saída obtida

#QUESTÃO 2
#a)
#[12, 12, 12]
#Quando iteramos a primeira vez (i==0), a lista functions
#será [number + index]. Quando i == 1, teremos [number + index, number + index].
#Quando i == 2, apenas repetimos o elemento inicial. Porém, perceba que 
#index não é fixo, ou seja, quando i = 0, index era 0, porém
#agora, na última iteração, index = 2, então, o equivalente à lista
#criada seria [number + 2, number + 2, number + 2].
#Para obter o resultado desejado, precisamos que o índice fique
#fixo, e isso pode ser feito fixando o valor de i na criação
#de lambda: lambda number, i = index: number + i 


#b)
def make_filter(starts_with= None, forbbiden_substrings= None, min_lenght = None):
    def filter_fn(name) -> bool:
        nonlocal starts_with
        nonlocal forbbiden_substrings
        nonlocal min_lenght
        if starts_with != None:
            if name[0] != starts_with:
                return False
        if min_lenght != None:
            if min_lenght < len(name):
                return False
        if forbbiden_substrings != None:
            for substring in forbbiden_substrings:
                if substring in name:
                    return False
        
        return True
    return filter_fn

#c)
operations = {
    "double": lambda number: number * 2,
    "square": lambda number: number * number,
    "negate": lambda number: -number,
}

#não entendi como fazer a compose então fiz apenas a choose_and_apply
def compose(*functions):
    pass

def choose_and_apply(program_steps, operation_map, initial_value):
    value = initial_value
    for step in program_steps[::-1]:
        value = operation_map[step](value)
    return value
    
result_value = choose_and_apply(["double", "square", "negate"], operations, 2)

print(result_value)