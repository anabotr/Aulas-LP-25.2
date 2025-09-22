# aula 15 - 22/09

import numpy as np

A = np.array([[1,2,3],[4,5,6]])
B = np.array([10,20,30])

print("Matriz A:\n", A)
print("Vetor B:\n", B)

print("Resultado A+B:\n", A+B)

A[0,:] = 42 #modifica a primeira linha de A para 42

print("Matriz A:\n", A)

array = np.arange(1,13)
print("Array original:", array)

mat = array.reshape((3,4)) #as dimensões do reshaped tem que ser divisores do 
#número de elementos do array original
print("Array reshaped:\n", mat)

c_flat = mat.flatten(order="C") #o order = "C" é o estilo do flat que queremos
#fazer, no caso, C é o estilo padrão então não é necessário colocar p fazer
#Esse meio que concatena as linhas
print("Flatten, estilo C:", c_flat)

f_flat = mat.flatten(order="F") #o order = "F" é o estilo do fortran
#Esse pega os objetos por coluna
print("Flatten, estilo Fortran:", f_flat)

mat_ravel = mat.ravel() #o ravel não te traz uma cópia dos dados, apenas uma 
#visualização deles, também tem o order que pode ser definido, porém, sua 
#vantagem é a enorme rapidez
print("Ravel:", mat_ravel)

a = np.array([1,2,3])
b = np.array([4,5,6])
#aqui, é como concatenar, as dimensões devem ser compatíveis
print("Empilhamento vertical:\n", np.vstack([a,b]))
print("Empilhamento horizontal:\n", np.hstack([a,b]))

c = np.arange(10)
print("Array base:", c)
#na hora de usar o split, é importante prestar atenção nos divisores
#ele retorna objeto array
print("Split em 2 partes iguais:", np.split(c,2))

#podemos também fazer split com quantias diferentes, se especificarmos os
#índices de separação dos arrays
print("Split em 3 partes:", np.split(c,[3,6]))

#Salvando uma matriz como arquivo txt
#format %d significa que é inteiro: trucaremos os decimais: 3.9 vira 3
np.savetxt("dados.csv", mat, delimiter=",", fmt="%d")
print("Dados salvos!")

#Carregando um arquivo
dados_carregados = np.loadtxt("dados.csv", delimiter=",", dtype = int)
print("Matriz carregada:\n", dados_carregados)



