def media_acumulada():
    lista = []
    def wrapper(*nums):
        for num in nums:
            nonlocal lista
            lista.append(num)
        return sum(lista)/len(lista)
    return wrapper

f = media_acumulada()
print(f(2,3))
print(f(1))
print(f(5,9,12))

def nao_negativo(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                print("Os argumentos não podem ser negativos")
                break
        for k, v in kwargs.items():
            if v < 0:
                print("Os argumentos não podem ser negativos")
                break 
        return func(*args, **kwargs)
    return wrapper

@nao_negativo
def f1(*nums, **kwargs):
    pass

(f1(1,2,3,4))
(f1(0,3,6,-2,5))
(f1(1,2,3,a=4,b=0, c=85))
(f1(1,2,45, a=9, b=-9, c = 92))