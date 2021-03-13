import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# costruiscto un array associativo con le regioni e i suoi abitanti

def inizializzazione():

    #importa la strutura dati dal csv

    reg = pd.read_csv('Tutte_le_regioni.csv', sep = ';', header = 0, index_col= 'Codice regione', usecols=['Codice regione', 'Regione', 'Maschi + Femmine'])

    print(reg) # visualizza le prime righe della tabella

    print(reg['Maschi + Femmine']) # stampo una colonna

    regList = list(reg['Maschi + Femmine'])

    popolazione = pd.Series(regList, index=reg['Regione'])  

    return(popolazione)


'''
estrapola riceve 4 valori in input:
- datoUno è la prima colonna da estrapolare
- datoDue è la seconda colonna da estrapolare
'''


def estrapola(datoUno, datoDue):

    estrazione = pd.read_csv('dati-regioni/dpc-covid19-ita-regioni.csv', sep = ',', header = 0, usecols=[datoUno, datoDue])

    colUno = list(estrazione[datoUno])
    colDue = list(estrazione[datoDue])
 
    return(estrazione)

'''
INIZIO DEL MAIN
'''

popol = inizializzazione()
print(popol)

tIntensiva = estrapola("denominazione_regione","ingressi_terapia_intensiva")
print(tIntensiva)

fig, axes = plt.subplots (1,2, figsize=(12,8))
popol.plot(ax=axes[0], kind = 'line', title='line')
popol.plot(ax=axes[1], kind = 'bar', title = 'bar')

plt.show()