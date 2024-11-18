'''

Esercizio 2: Manipolazione e Aggregazione dei Dati

Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.

Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.



Caricare i dati in un DataFrame.
Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.
Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.
Trovare il prodotto più venduto in termini di Quantità.
Identificare la città con il maggior volume di vendite totali.
Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).
Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.
Visualizzare il numero di vendite per ogni città.

'''

import pandas as pd
import numpy as np
import random

pd.DataFrame({"food":["bacon","pulled pork","bacon","pastrami","corned beef", "bacon", "pastrami", "honey ham", "nova lox"], "ounces":[4,3,12,6,7.5,8,3,5,6]})

meat_to_animal = {"bacon":"pig", "pulled pork":"pig", "pastrami":"cow", "corned beef":"cow", "honey ham":"pig", "nova lox":"salmon"}


data = pd.DataFrame({"food":["bacon","pulled pork","bacon","pastrami","corned beef", "bacon", "pastrami", "honey ham", "nova lox"], "ounces":[4,3,12,6,7.5,8,3,5,6]})


serie4 = pd.Series([1.,-999.,2.,-999.,-1000.,3.])

serie5 = [serie4 > 3] = np.nan


df = pd.DataFrame({"key1":["a", "a", None, "b", "b", "a", None],
"key2" : pd.Series([1, 2, 1, 2, 1, None, 1], dtype="Int64"),
"data1" : np.random.standard_normal(7),
"data2" : np.random.standard_normal(7)})




