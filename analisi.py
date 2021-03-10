'''

clone dell'open data sui contagi
https://github.com/pcm-dpc/COVID-19

'''
import csv
from datetime import datetime
import numpy as np

import matplotlib.pyplot as plt

contagi = { }

dataSom = []

# apertura file riga per riga organizzando il risultato in liste
with open('dati-regioni/dpc-covid19-ita-regioni.csv', 'r') as file:
    valori = csv.reader(file, delimiter=",")
    header = next(valori)

    for row in valori:

        data = datetime.fromisoformat(row[0])
        
#        dataSom.append(data)

        if not(row[3] in contagi):
            contagi[row[3]] = []

        contagi[row[3]].append((data,int(row[12])))


print(header)
file.close()

date = []
val = []
regioni = list(contagi.keys())
regioni.remove("Campania")

regMatrix = []

for i in range(5):
    regMatrix.append([])

print(regMatrix)

i = 0

for row in range(5):
    for col in range(4):
        regMatrix[row].append(regioni[i])
        i = i+1
print(regMatrix)


campVal = []
campDate = []
# x = np.arange(1,len(campDate),dtype=int)


for i in contagi["Campania"]:
    campDate.append(i[0])
    campVal.append(i[1])

for i in range(5):
    for j in range(4):
        print(regMatrix[i][j])

#print(campVal)

#print(campDate)
#print(campVal)
#print(contagi["Campania"])



nome = "contagi-"

for j in range(5):

    fig, ax = plt.subplots(1, 4, figsize=(12,7))

    # generiamo una matrice di una riga per 4 colonne da inserire in Figure
    left, bottom, width, height = 0.4, 0.4, 0.4, 0.4 
    #plt.xticks(rotation=70)

    for i in range(4):
        reg = contagi[regMatrix[j][i]]
        
        for dati in reg:
            date.append(dati[0])
            val.append(dati[1])
        #print(len(val), val)
        #print(len(date), date)

        ax[i].plot(date, val, color="blue", label=regMatrix[j][i])
        ax[i].plot(campDate, campVal, color="red", label="Campania")
        ax[i].legend()
        ax[i].grid(True)
        #ax[i].set_xlabel('date')
        ax[i].set_ylabel('Contagi')
        plt.setp( ax[i].xaxis.get_majorticklabels(), rotation=70 )   

        print(len(val))
        print(len(date))
        date.clear()
        val.clear()

        nome = nome + str(regMatrix[j][i]) + "-"
        
    nome = nome + ".png"
    fig.savefig(nome, dpi=100, facecolor="#f1f1f1")
    nome = "contagi-"




