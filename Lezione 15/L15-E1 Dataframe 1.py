'''

Esercizio 1: Analisi Esplorativa dei Dati

Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.

Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 

Caricare i dati in un DataFrame autogenerandoli casualmente .
Visualizzare le prime e le ultime cinque righe del DataFrame.
Visualizzare il tipo di dati di ciascuna colonna.
Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).
Identificare e rimuovere eventuali duplicati.
Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.
Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).
Salvare il DataFrame pulito in un nuovo file CSV.

'''


import pandas as pd
import numpy as np
import random

# DataFrame esempio, inclusi valori mancanti e duplicati
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}
df = pd.DataFrame(data)

nameslist = ['Alice', 'Bob', 'Carla', 'Devin', 'Edwin', 'Felix']
ageslist = [25, 30, 22, 30, 25, 29]
citieslist = ['Roma', 'Milano', 'Napoli', 'Firenze', 'Bologna', 'Torino']
salarieslist = [10000, 12000, 8000, 7500, 11000, 9000]
print(nameslist)

random.shuffle(nameslist)
random.shuffle(ageslist)
random.shuffle(citieslist)
random.shuffle(salarieslist)
print(nameslist)


data = {
    'names': nameslist,
    'ages': ageslist,
    'cities': citieslist,
    'salaries' : salarieslist
}

'''names = { "names" : nameslist }
ages = { "ages" :  ageslist}
cities = { "cities" :  citieslist}
salaries = { "salaries" : salarieslist }
print(names)


data = {}
data.update(names)
data.update(ages)
data.update(cities)
data.update(salaries)
print(data)'''

dataframe1 = pd.DataFrame(data)
print(dataframe1)

## dataframe1 = dataframe1[1:3]
## print(dataframe1)

print(dataframe1.describe())
print(dataframe1.dtypes())


pd.DataFrame({"food":["bacon","pulled pork","bacon","pastrami","corned beef", "bacon", "pastrami", "honey ham", "nova lox"], "ounces":[4,3,12,6,7.5,8,3,5,6]})

meat_to_animal = {"bacon":"pig", "pulled pork":"pig", "pastrami":"cow", "corned beef":"cow", "honey ham":"pig", "nova lox":"salmon"}


data = pd.DataFrame({"food":["bacon","pulled pork","bacon","pastrami","corned beef", "bacon", "pastrami", "honey ham", "nova lox"], "ounces":[4,3,12,6,7.5,8,3,5,6]})


serie4 = pd.Series([1.,-999.,2.,-999.,-1000.,3.])




df = pd.DataFrame({"key1":["a", "a", None, "b", "b", "a", None],
"key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
"data1" : np.random.standard_normal(7),
"data2" : np.random.standard_normal(7)})





