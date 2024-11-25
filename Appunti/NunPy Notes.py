''''


'''


import numpy as np
import random as random
from scipy import stats



# one dimensional ndarray
arr = np.array([1, 2, 3, 4, 5])

# two dimensional ndarray
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)  # Output: (5,)
print("Dimensioni dell'array:", arr.ndim)  # Output: 1
print("Tipo di dati:", arr.dtype)  # Output: int64 (varies based on platform)
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

## float conversion
nda2 = arr.astype(float)
print(nda2)
print(nda2.dtype)
print(nda2.shape)


## slicing uses a range-like form (start included, stop excluded, step)

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
# Slicing rows from 1 to 3 excluded
print(arr_2d[1:3])  # Output: [[ 5  6  7  8]
                   #          [ 9 10 11 12]]
# Slicing columns from 1 to 3 excluded
print(arr_2d[:, 1:3])  # Output: [[ 2  3]
                       #          [ 6  7]
                       #          [10 11]]
# Slicing rows 1 onwards, columns from 1 to 3 excluded
print(arr_2d[1:, 1:3])  # Output: [[ 6  7]
                        #          [10 11]]


## linshape si usa come arange ma per generare delle serie più complesse

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

randarray = np.random.randint(0, 100, (3, 3))
print(randarray)