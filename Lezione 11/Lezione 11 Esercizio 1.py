'''

Create 2 array numpy:

- Un array unidimensionale di numeri casuali compresi tra 0 e 1;
- Un array bidimensionale di dimensione 3x3 con valori interi casuali.


Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:

- Restituite la somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi;
- Unite i 2 array secondo l'asse 1.




Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e fate i seguenti calcoli:

- Calcolo della media;
- Calcolo della moda;
- Calcolo della deviazione standard;
- Trasformatelo in un array 5 X 10


'''



import numpy as np
import random as random
from scipy import stats


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


## arr1 = np.array([ [0, 1, 0], [1, 1, 0], [0, 0, 1] ])
## arr2 = np.array([ [1, 1, 1], [0, 1, 1], [0, 1, 1] ])

arr1 = rand_matrix(3, 3, 0, 1)
arr2 = rand_matrix(3, 3, 0, 1)
print(arr1)
print(arr2)

arr_dot = np.dot(arr1, arr2)
print(arr_dot)


arr3 = rand_matrix(4, 4, 0, 100)
arr4 = rand_matrix(4, 4, 0, 100)
print(arr3)
print(arr4)

## riga -1 (l'ultima), colonna da 1 in poi (ovvero la seconda)
last_row_second_column3 = arr3[ -1 , 1:]
print(last_row_second_column3)
somma = last_row_second_column3.sum()
print(somma)

arr_concat = np.concatenate( (arr3, arr4), axis = 1)
print(arr_concat)


array_50 = rand_matrix(1, 50, 0, 1000)
print(array_50)

## media, moda, deviazione standard, trasforma in 5 x 10

media = np.median(array_50)
print(media)

## lascia valori originari senza sovrascrivere ndarray di input
moda = stats.mode(array_50, keepdims = True).mode[0]
print(moda)

std_dv = np.std(array_50)
print(std_dv)

array_5_10 = array_50.reshape(5, 10)
print(array_5_10)






