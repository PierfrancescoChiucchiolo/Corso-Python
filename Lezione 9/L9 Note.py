'''
oggi test nel pomeriggio di piccolo videogioco come 3 livelli per spiegare quello che abbiamo imparato


sicurezza = capacità di resistere ad intrusione
robustezza = capacità di non cadere in errore
'''


import numpy as np

# Creazione di un array unidimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array bidimensionale
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)  # Output: (5,)
print("Dimensioni dell'array:", arr.ndim)  # Output: 1
print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size)  # Output: 5
print("Somma degli elementi:", arr.sum())  # Output: 15
print("Media degli elementi:", arr.mean())  # Output: 3.0
print("Valore massimo:", arr.max())  # Output: 5
print("Indice del valore massimo:", arr.argmax())  # Output: 4



print("Forma dell'array:", arr2d.shape)
print("Dimensioni dell'array:", arr2d.ndim)
print("Tipo di dati:", arr2d.dtype)
print("Numero di elementi:", arr.size)
print("Somma degli elementi:", arr2d.sum())
print("Media degli elementi:", arr2d.mean())
print("Valore massimo:", arr2d.max())
print("Indice del valore massimo:", arr2d.argmax())

## slicing usa range(start incluso, end escluso, step):

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
# Slicing sulle righe con righe da 1 a 3 escluso
print(arr_2d[1:3])  # Output: [[ 5  6  7  8]
                   #          [ 9 10 11 12]]
# Slicing sulle colonne da 1 a 3
print(arr_2d[:, 1:3])  # Output: [[ 2  3]
                       #          [ 6  7]
                       #          [10 11]]
# Slicing misto: righe da 1 in poi, colonne da 1 a 3 escluso
print(arr_2d[1:, 1:3])  # Output: [[ 6  7]
                        #          [10 11]]



# fancy indexing: elementi arbitrari anche non contigui / ritorna una copia / usa indici interi
# slicing: solo selezioni rettangolari / ritorna una view / indici di inizio, fine, step
