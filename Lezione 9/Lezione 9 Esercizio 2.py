'''

Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

'''

import numpy as np

'''
# rubato da https://note.nkmk.me/en/python-numpy-random/
rng = np.random.default_rng()

print(rng.uniform(-50.0, 50.0))
# 17.611381123655846

print(rng.uniform(-50.0, 50.0, 40))
# [ 5.80448109  6.64291183 22.27752257]

print(rng.uniform(-50.0, 50.0, (2, 3)))
# [[ 12.23855165  -9.97903127 -38.40667299]
#  [-14.42414448 -45.04563195  14.37486871]]
'''


'''
rng1 = np.random.default_rng()
print(rng1.integers(10, 50, size = 100))

rng2 = np.array(rng1)
rng2 = rng2[0 : 11]
print(rng2)
'''


arr = np.array([20, 34, 12, 44, 1, 4, 19, 14, 43, 23, 6, 33, 10, 15, 18, 20, 43, 22, 3, 42])
print(arr)
copia = np.array(arr)

print(arr[0 : 10])
print(arr[15 : 20])
print(arr[5 : 14])
print(arr[2 : 20 : 3])
arr[5 : 10] = 99
print(arr)

def slice_ndarray(ndarray):
    for i in range(0, ndarray.size + 1):
        for j in range(0, ndarray.size + 1):
            print(ndarray[j : i])

slice_ndarray(copia)


'''
## sto tentando di fare i SOTTOINSIEMI non le sottostringhe dell'array in maniera ricorsiva
## ma sono anche un po' arrugginito sulla ricorsione


print("sto per darti la copia")
print(copia)

import random as random

def get_subset(ndarray):
    if ndarray.size > 1:
        random_index = random.randint(0, ndarray.size)
        print(random_index)
        ritorno = np.concatenate( get_subset(ndarray[0 : random_index]), get_subset(ndarray[random_index : ndarray.size]) )
        print(ritorno)
        return ritorno
    else:
        print(ndarray)
        return ndarray


get_subset(copia)


'''