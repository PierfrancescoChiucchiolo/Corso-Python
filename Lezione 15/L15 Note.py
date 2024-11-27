'''

pandas è una libreria orientata alle tables come in sql, ma direttamente in python
introduce dataframe (come fogli di calcolo e table sql) e serie

usiamo un foglio jupyter, si creano in estensione .ipynb



'''

import pandas as pd
import random
import numpy as np

filepath = "Lezione 15/ex1.csv"

dataframe1 = pd.read_csv(filepath)

print(dataframe1.head())

serie1 = pd.Series([4, 7, -3, 5], index = ["uno", "due", "tre", "quattro"])
print(serie1)

## si può convertire un dizionario in una serie
dizionario1 = {"1" : "Ciao", "2" : "Ciaone", "3" : "Ciaozzo"}
serie2 = pd.Series(dizionario1)
print(serie2)

## e viceversa

dizionario2 = serie2.to_dict()
print(dizionario1 == dizionario2)


## NaN not a number, viene da R, è uno dei modi per rappresentare i dati non presenti
## iloc / loc individua elementi in base alla posizione / in base al label dato al rigo


##dataframe 10 righe e 3 colonne con numeri randomici

colonna = []
for i in range(10):
    riga = []
    for j in range(3):
        intero = random.randint(0, 100)
        riga.append(intero)
    colonna.append(riga)
    

print(colonna)

dataframe2 = pd.DataFrame(colonna)
print(dataframe2)

## 15 numeri randomici, 3 indici a random con null, poi ffill


lista = []
for i in range (0, 15):
    lista.append(random.randint(0, 100))

for i in range (0, 3):
    indice = random.randint(0, len(lista))
    lista[indice] = None

dataframe3 = pd.Series(lista)
print(dataframe3)
dataframe3.reindex(method = "ffill")
print(dataframe3)


## usa describe per una serie di dati
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=["a", "b", "c", "d"], columns=["one", "two"])
print(df.describe())


## importa dataframe/csv, stampa con describe



##filtra per valore
serie5 = [serie4 > 3] = np.nan

