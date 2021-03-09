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
    
        contagi[row[3]].append((data.strftime("%d/%m/%y"),int(row[12])))


print(header)
file.close()

fig, ax = plt.subplots(3,7)
date = []
conta = []

for i in contagi["Campania"]:
    date.append(i[0])
    conta.append(i[1])

#ax[0].plot(date,conta)

print(len(date))
print(len(conta))
print("le regioni sono le seguenti ", contagi.keys(), "\ne sono ", len(contagi))

#print(contagi["Campania"])
