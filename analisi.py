'''

clone dell'open data sui contagi
https://github.com/pcm-dpc/COVID-19

'''
import csv
from datetime import datetime
import numpy as np

import matplotlib.pyplot as plt

dataSom = []
regione = []
lazio = []
campania = []
nuoviPositivi = []

# apertura file riga per riga organizzando il risultato in liste
with open('dati-regioni/dpc-covid19-ita-regioni.csv', 'r') as file:
    valori = csv.reader(file, delimiter=",")
    header = next(valori)

    for row in valori:
        if not(row[3] in regione):
            regione.append(row[3])

        if((row[3]=="Campania") ):
#           print(type(row[0]))
            data = datetime.fromisoformat(row[0])
            data.strftime("%d/%m/%y")
            dataSom.append(data)
#           dataSom.append(datetime.datetime.strptime(row[0], '%Y-%m-%d')) 
            campania.append(int(row[12]))

        if((row[3]=="Lazio") ):
#           print(type(row[0]))
            data = datetime.fromisoformat(row[0])
            data.strftime("%d/%m/%y")
            dataSom.append(data)
#           dataSom.append(datetime.datetime.strptime(row[0], '%Y-%m-%d')) 
            lazio.append(int(row[12]))


print(header)

file.close()

for reg in regione:
    print(reg)

fig, ax = plt.subplots(1, 2, figsize=(14,3))
#fig, ax = plt.subplots()

# generiamo una matrice di una riga per 4 colonne da inserire in Figure
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 

# x = np.linspace(-5,5,100)

# generiamo le quattro istanze Axes, inserendo i valori dei 4 grafici
ax[0].plot(campania,color="blue", label="Campania")
ax[1].plot(lazio ,color="red", label="Lazio")

#ax.plot(dataSom, nuoviPositivi, color="blue", label="Contagi")
#ax.legend()

for i in range(2):
    
    ax[i].legend()


# salva il grafico in un file di nome grafico.png
fig.savefig("grafico.png", dpi=100, facecolor="#f1f1f1")
plt.show()