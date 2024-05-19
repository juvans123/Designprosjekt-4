#Plotting
import matplotlib.pyplot as plt
#Lese CSV
import csv
header = []
data = []
filename = 'bandpass.csv'
#Henter data fra csvfil
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
#Leser første linje i csv-fila (den med navn til kanalene)
    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
        #Legger inn data fra hver kanal i hver sin liste
ch1 = [(p[0]) for p in data]
ch2 = [(p[1]) for p in data]



#Plot
plt.plot(ch1,ch2)
plt.axvline(3950,linestyle='dotted',
color='red', label = '3950 Hz')
plt.title('Amplituderespons for båndpassfilter')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('|H(w)| (db)')
plt.legend()
plt.show()
plt.savefig('frefre')
