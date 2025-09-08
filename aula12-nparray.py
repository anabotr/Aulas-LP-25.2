#Aula 12 - 08/09
import numpy as np

array_1 = np.array([1,2,3])
array_2 = np.array([[1,2,3], [4,5,6]])


#O array trabalho com dimensões
print("Array 1D:", array_1)
print("Array 2D:\n", array_2)

print("*"*60)

print("Propriedades dos NDArrays:")
print("- Formato (shape)")
print("1D", array_1.shape)
print("2D", array_2.shape)
print("- Tamanho (size)")
print("1D", array_1.size)
print("2D", array_2.size)
print("- Tipo de Dados (dtype)")
print("1D", array_1.dtype)
print("2D", array_2.dtype)
print("- Número de dimensões (ndim)")
print("1D", array_1.ndim)
print("2D", array_2.ndim)

print("*"*60)

print("Criação de NDArrays:")
print("Zeros:\n", np.zeros((2,3)))
print("Uns:\n", np.ones((2,3)))
print("Cheio:\n", np.full((2,3), 42))

#cria uma matriz com um range entre, por exemplo, 0 e 10 com passo 2
print("ARange:\n", np.arange(0,10,2))

#cria valores igualmente espaçados, no exemplo, 5 valores igualmente espaçados
#entre 0 e 1
print("LinSpace:\n", np.linspace(0,1,5))

#no np, dentro do módulo random, temos a função rand, que gera números 
#aleatórios de 0 a 1
print("Random:\n", np.random.rand(2,2))

print("*"*60)

#a contagem começa do zero!!!!!!
matriz = np.array([[10,20,30],[40,50,60], [70,80,90]])
print("Matriz base:\n", matriz)
print("\nElemento da linha 1, coluna 2:", matriz[1,2])
print("\nPrimeira linha:", matriz[0])
print("\nSegunda coluna:", matriz[:,1])
print("\nÚltima linha:", matriz[-1])
print("\nSubmatriz (linhas 0-1, colunas 1,2):\n", matriz[0:2, 1:3])


print("*"*60)
x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

print("x: \n", x)
print("y: \n", y, "\n")

print('Operações e Agregações em NDArrays')
print("Soma elemento a elemento:\n", x+y)
print("Multiplicação elemento a elemento:\n", x*y)
]print("Transposta de x:\n", x.T)

#Operações com agregação diminuem a dimensão do objeto
print("Soma total dos elementos de x:\n", np.sum(x))
print("Soma por colunas de X:\n", np.sum(x, axis = 0))
print("Soma por linhas de x:\n", np.sum(x, axis=1))


print("*"*60)
print("Estatística em NDArrays")
data = np.random.randint(1,100, size = 10)
print("NDArray aleatório:", data)

#a média é uma função porque traz mais leveza do que os métodos
print("Média:", np.mean(data))
print("Valor máximo:", np.max(data))
print("Valor mínimo:", np.min(data))
print("Índice do valor máximo:", np.argmax(data))
print("Desvio padrão:", np.std(data))

print("*"*60)
print("Indexação Booleana e Condicional em NDArrays")
array_ = np.array([10,15,20,25,30])
print("Array base:", array_, "\n")
print("Valores maiores que 20:", array_ > 20)
print("Valores pares:", array_%2 == 0)
#para achar os pares, %2 funciona, mas where é melhor:
print("Valores pares:", np.where(array_%2 == 0))

#indexando um array numpy com outro array de booleanos, retornará apenas os 
#que forem marcador como verdadeiros
#retorna um Array Filtrado
print("Valores ímpares:", array_[array_%2 == 1])

