'''
pip = pip installs packages
PyPI = python package index, repository di librerie python

numpy = libreria open source per calcolo scientifico applicato alla programmazione, machine learning e analisi dati
qui abbiamo gli array veri e propri, come struttura dati e non un tipo

installazione pacchetti da fonti multiple (PyPI / GitHub ecc.)
gestione dipendenze tra i pacchetti
aggiornamento e rimozione di pacchetti
gestione delle versioni
integrazioni con ambienti virtuali (venv o virtualvenv)

nunpy supporta array multidimensionali, ha operazioni matriciali e algebriche, trasformazioni di fourier e funzioni statistiche
integra anche per c/c++ e fortran, con strumenti di ottimizzazione


'''

import numpy as np

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape)  # Output: (5,)
print("Dimensioni dell'array:", arr.ndim)  # Output: 1
print("Tipo di dati:", arr.dtype)  # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size)  # Output: 5
print("Somma degli elementi:", arr.sum())  # Output: 15
print("Media degli elementi:", arr.mean())  # Output: 3.0
print("Valore massimo:", arr.max())  # Output: 5
print("Indice del valore massimo:", arr.argmax())  # Output: 4