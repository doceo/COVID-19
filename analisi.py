'''

clone dell'open data sui contagi
https://github.com/pcm-dpc/COVID-19

'''
import csv
from datetime import datetime
import numpy as np

import matplotlib.pyplot as plt

contagi = { }
popolazione = { }
dataSom = []

'''

Dal file delle regioni costruiamo un dict 
con le popolazioni residenti

'''

with open('Tutte_le_regioni.csv', 'r') as file:
    valori = csv.reader(file, delimiter=";")
    header = next(valori)

    for row in valori:

        print("riga: ",row)
        popolazione[row[1]] = row[4] 

print(header)
file.close()

print(popolazione)

'''
a partire dagli opendata sui contagi si costruiscono i vettori
da comprarare attraverso i grafici.


'''

# apertura file riga per riga organizzando il risultato in liste
with open('dati-regioni/dpc-covid19-ita-regioni.csv', 'r') as file:
    valori = csv.reader(file, delimiter=",")
    header = next(valori)

    for row in valori:

        data = datetime.fromisoformat(row[0])
        
        if row[3] in popolazione:
            datoNorm = (int(row[12]))/int(popolazione[row[3]])*100000

        if not(row[3] in contagi):
            contagi[row[3]] = []

        contagi[row[3]].append((data,datoNorm))


print(header)
file.close()



date = []
val = []
regioni = list(contagi.keys())

regMatrix = []

for i in range(7):
    regMatrix.append([])

print(regMatrix)

i = 0

for row in range(7):
    for col in range(3):
        if(regioni[i]):
            regMatrix[row].append(regioni[i])
        i = i+1
print(regMatrix)

regioni.remove("Campania")

campVal = []
campDate = []
# x = np.arange(1,len(campDate),dtype=int)


for i in contagi["Campania"]:
    campDate.append(i[0])
    campVal.append(i[1])

print(regMatrix)

nome = "contagi-"

for j in range(7):

    fig, ax = plt.subplots(1, 3, figsize=(12,7))

    # generiamo una matrice di una riga per 4 colonne da inserire in Figure
    #left, bottom, width, height = 1, 1, 1, 1 
    #plt.xticks(rotation=70)

    for i in range(3):
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
        #ax[i].set_ylabel('Contagi')
        plt.setp( ax[i].xaxis.get_majorticklabels(), rotation=70 )
        plt.setp( ax[i].yaxis.get_majorticklabels(), rotation=70 )   

        #print(len(val))
        #print(len(date))
        date.clear()
        val.clear()

        nome = nome + str(regMatrix[j][i]) + "-"
        
    nome = nome + ".png"
    fig.savefig(nome, dpi=100, facecolor="#f1f1f1")
    nome = "contagi-"




