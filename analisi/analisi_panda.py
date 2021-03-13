import pandas as pd
import numpy as np

def inizializzazione():

    #importa la strutura dati dal csv

    reg = pd.read_csv('Tutte_le_regioni.csv', sep = ';', header = 0, index_col= 'Codice regione', usecols=['Codice regione', 'Regione', 'Maschi + Femmine'])

    print(reg) # visualizza le prime righe della tabella

    print(reg['Maschi + Femmine']) # stampo una colonna

    '''
    voglio costruire una Serie con etichette Regione.
    verrebbe una struttura di tipo array indicizzato con gli elelenti della colonna che si chiama Regioni.
    converte in float dati int, ma invece risultano NAN.

    '''

    popolazione = pd.Series(reg["Maschi + Femmine"], index=reg['Regione'])  

    print(popolazione)

    #print(popolazione)
