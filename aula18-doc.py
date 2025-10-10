#PARTE A
#1)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter

seed = np.random.seed(42)

#2)
N = 180
base_temp = 22.0
amp = 8.0
noise_temp = 1.5
noise_energy = 10.0

#3)
dates = pd.date_range(start = "2025-01-01", periods = N)
t = np.arange(N)

#4)
ruido_temp = np.random.normal(0, noise_temp, N)
temp = base_temp + amp*np.sin(2*np.pi*t/30) + ruido_temp

#5)
ruido_energy = np.random.normal(0, noise_energy, N)
energy = 200 + 5*np.abs(temp - base_temp) + ruido_energy

#6)
indexes = np.random.choice(N, 3, replace=False)
for index in indexes:
    energy[index] += 80

#7)
df = pd.DataFrame({"dates": dates, "temp": temp, "energy": energy})
print(df.head())
print("_"*60)
print(df.describe())
print("_"*60)

#8)
df["HDD"] = base_temp - df["temp"]
df["CDD"] = df["temp"] - base_temp
df["HDD"] = df["HDD"].clip(lower = 0)
df["CDD"] = df["CDD"].clip(lower = 0)


filtro = np.ones(7)/7
media_1 = np.convolve(filtro, temp, mode = 'valid')
media_movel = np.convolve(filtro, temp)

#formatando a média móvel para ter o mesmo tamanho de temp mas apenas os valores
#válidos
media_movel[:6] = 0
media_movel[-6:] = 0

#aqui eu defini que estou usando a média centrada no valor atual, então, os 3
#primeiros e 3 últimos dias têm média 0
media_movel = media_movel[3:-3]
df["Média móvel"] = media_movel


#PARTE B
#9)
fig = df.plot(figsize=(12,8))
#gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)
locator = AutoDateLocator() 
fmt = ConciseDateFormatter(locator)
fig.xaxis.set_major_locator(locator)
fig.xaxis.set_major_formatter(fmt)


#10)
#ax1 = fig.add_subplot(gs[0, 0])
ax1 = df.plot(kind = "line", x = dates, y = temp, lw = 1.0)
plt.plot()