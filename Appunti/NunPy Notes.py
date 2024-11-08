''''


'''


import numpy as np

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