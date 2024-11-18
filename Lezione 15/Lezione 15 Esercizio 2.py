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

## non funziona ovviamente, oggi sono abbastanza influenzato e non riesco a produrre

data = {
    'Prodotto': ['Alici', 'Bombi', 'Carletti', 'Dentellini', 'Eppelletti', 'Farfallini'],
    'Quantita': [12, 23, 49, 18, 12, 32],
    'Prezzo Unita' : [1, 2, 5, 3, 4, 2],
    'Città': ['Roma', 'Milano', 'Napoli', 'Firenze', 'Bologna', 'Torino']
}
df = pd.DataFrame(data)
print(df)



np.random.seed(0)
quantita = random.randint(1, 50, size = 20)
citta = np.random.choice(citta, size = 20)


df["Totale vendite"] = df["Quantita"] * df["Prezzo Unita"]

df.groupby("Prodotto")["Totale Vendite"].sum().reset_index

df.groupby("Prodotto")["Totale Vendite"].sum().idxmax()

df.sort_values(by = "Totale Vendite", ascending = False)
