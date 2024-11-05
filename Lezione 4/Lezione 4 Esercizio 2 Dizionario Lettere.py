'''

input stringa utente, output dizionario con chiave lettera e output numero di occorrenze

Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}


'''

## rubato da https://datagy.io/python-list-alphabet/

import string

## lista delle lettere
## alfabeto = string.ascii_letters
alfabeto = string.ascii_lowercase

dizionario = {}

input1 = input("Scrivere una parola: ")
input1 = input1.lower()

for lettera in alfabeto:

    dizionario.update( {lettera : input1.count(lettera)} )

print(dizionario)