'''

18.Esercizio 3: Pandas e Numpy e Visualizzazione 
Descrizione: Crea un dataset autogenerandolo monolineare con 50 posizioni matematica e cambia la sua forma in 10 file da 5
normalizza i valori e rendili interi , nessun valore deve essere uguale a un altro sulla stessa linea della collezione
dopodiché stampa un grafico che lo rappresenti

'''

import numpy as np
import random as random
from scipy import stats
import matplotlib.pyplot as plt


def rand_matrix(x, y, a, b):
    columns = []
    for i in range(0, x):
        rows = []
        for j in range(0, y):
            intero = random.randint(a, b)
            rows.append(intero)
        columns.append(rows)

    array = np.array(columns)
    return array



randarray = np.random.randint(0, 100, (1, 50))
print(randarray)

array_5_10 = randarray.reshape(5, 10)
print(array_5_10)


plt.plot(array_5_10)
plt.show()
