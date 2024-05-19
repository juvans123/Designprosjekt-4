#Plotting
import matplotlib.pyplot as plt
#Lese CSV
import csv
from scipy.fft import fft, fftfreq
import numpy as np

header = []
data = []
filename = 'scope.csv'
#Henter data fra csvfil
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
#Leser første linje i csv-fila (den med navn til kanalene)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
        #Legger inn data fra hver kanal i hver sin liste
time = [(p[0]) for p in data]
ch2 = [((p[2])*2) for p in data]

sampling_rate = 1 / (time[1] - time[0])

# Bruk FFT til å finne frekvenskomponentene
N = len(ch2)
yf = fft(ch2)
xf = fftfreq(N, 1 / sampling_rate)

# Finn den dominerende frekvensen
idx = np.argmax(np.abs(yf))
dominant_frequency = np.abs(xf[idx])

print(f"Dominant frequency: {dominant_frequency} Hz")

# OFFSET JUSTERING

dominant_frequency=((dominant_frequency+40)/1000)
dominant_frequency=round(dominant_frequency,3)

x_values=np.linspace(0,10,8192)

#Plot
plt.figure(figsize=(10,5))
plt.plot(x_values,ch2, label=f'{dominant_frequency} kHz')
plt.title(' Analyse av $\hat{x}_k(t)$ i tidsdomenet')
plt.xlabel('Tid ms')
plt.ylabel('Spenning V')
plt.legend(loc='upper right')

plt.show()
