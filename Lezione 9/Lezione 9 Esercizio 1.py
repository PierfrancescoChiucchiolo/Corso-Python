'''

Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array.

'''

import numpy as np


nda1 = np.arange(10, 49)
print(nda1)
print(nda1.dtype)
print(nda1.shape)

nda2 = nda1.astype(float)
print(nda2)
print(nda2.dtype)
print(nda2.shape)

