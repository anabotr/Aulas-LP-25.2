import numpy as np

dados = np.loadtxt("dados2.csv", delimiter = ",", skiprows = 3, usecols = (1,2), dtype = float)
print("Idades", dados[:,0])
print("Notas", dados[:,1])

