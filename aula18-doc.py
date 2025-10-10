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

#aqui eu defini que estou usando a média centrada no valor atual, então, os 3
#primeiros e 3 últimos dias têm média 0
media_movel = media_movel[3:-3]
df["Média móvel"] = media_movel


#PARTE B
#9)
fig = plt.figure(figsize=(12,8))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)
locator = AutoDateLocator() 
fmt = ConciseDateFormatter(locator)


#10)
ax1 = fig.add_subplot(gs[0, 0])
df['Datas'] = df['dates'].dt.strftime('%d-%b')
df.plot(kind = "line", x = 'Datas', y = 'temp', lw = 1.0, title= "Temperatura por data", ylabel = "°C", label = "Temperatura", ax = ax1, color = 'orange')
df["Média móvel"].plot(kind = "line", label = "Média móvel")
ax1.fill_between(df['Datas'], df['temp'], base_temp, where=(df['temp'] < base_temp), color='blue', alpha=0.15, label = "Menor que temperatura base")
ax1.fill_between(df['Datas'], df['temp'], base_temp, where=(df['temp'] > base_temp), color='red', alpha=0.15, label = "Maior que temperatura base")
ax1.legend()
ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(fmt)

#11)
ax2 = fig.add_subplot(gs[0,1])
df.plot(kind = "scatter", alpha = 0.7, x='temp', y='energy', xlabel = "°C", ylabel = "Energia", title="Energia por Temperatura", label = "Energia", ax = ax2)
for i in indexes:
    ax2.annotate("spike", (df["temp"].iloc[i], df["energy"].iloc[i]),
                 xytext=(8, 8), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", facecolor = 'black', lw=2.0))
ax2.legend()

#12)
ax3 = fig.add_subplot(gs[1,0])
df["temp"].plot(kind = 'hist', alpha = 0.7, title = "Histograma de temperaturas", xlabel= "°C", ylabel="Contagem", label = "Quantidade", ax = ax3, color = "orange")


#13)
df.set_index("dates", inplace=True)
weekly = df.resample("W").agg({"energy":"sum", "temp":"mean"})
ax4 = fig.add_subplot(gs[1, 1])
weekly.index = weekly.index.strftime("%d-%b") #mudamos para string para plotar
#no documento pede width = 5, como as barras estavam se sobrepondo, tomamos liberdade para colocar 0.5
weekly["energy"].plot(kind='bar', width = 0.5, align = 'center', label="Energia (semanal)", ax=ax4, title = "Comparação semanal", color = "orange", alpha = 0.4)
ax4.set_ylabel("Energia")
ax4.xaxis.set_major_locator(locator)
ax4.xaxis.set_major_formatter(fmt)

ax4_t = ax4.twinx()

weekly["temp"].plot(kind='line', marker="o", lw=1.8, label="Temp média (semanal)", ax=ax4_t)
ax4_t.set_ylabel("°C")
ax4_t.set_xlabel("Semanas")

ax4.legend(loc="upper left")
ax4_t.legend(loc="upper right")

#14)
plt.tight_layout()
fig.savefig("numpy_matplotlib.png", dpi=150)
