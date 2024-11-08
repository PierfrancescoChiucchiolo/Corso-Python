'''

python: interpretato, orientato agli oggetti, dinamico e ad alto livello
supporta dinamiche imperative e funzionali
è tipizzato dinamicamente e in modo forte, ovvero inferenza di tipo implicito, ma non vengono convertiti se non esplicitamente
pseudocompilato (prima interprete, poi traduci e esegui) 

un metodo si riconosce al 90% dei casi da una parola seguita dalle parentesi, in minuscolo
l'unica cosa scritta in maiuscolo sono nomi dei moduli e nomi delle classi


regole fondamentali: asincronia(o astrazione) ereditarietà / polimorfismo / incapsulamento
print(1 + 2)
astrazione perché non abbiamo definito quella funzione, ma esiste, è nativa, aldifuori del contesto
ereditarietà gli oggetti traggono comportamenti da altri oggetti affini
polimorfismo stessa forma diverso comportamento o viceversa, l'operatore + funziona con molte varianti, funziona con str, int, double
incapsulamento nascondere complessità, garantisce codice più robusto e modulare


sopra i metodi cosa fanno / commenta dove sei arrivato se lavori in gruppo

convenzioni variabili: no spazi / lettere numeri e underscore / inizia solo lettere e underscore
basilari numeri (interi/float/double) / stringhe (sono in realtà un tipo composto da char) / booleani
non basilari (oggetti e classi)

la stringa non è tecnicamente un array/lista ma è l'unico tipo con dei metodi proprio
non è neanche un tipo basilare, tecnicamente è un composto da char


collezioni:
list (tipo List e sono collezioni disomogenee di elementi tipizzati, ordinati con indice) lista = [1, 2, 3]
tupla NON modificabile a differenza della lista, python non ha costanti tupla = [1, 2, 3]
dizionario tipo chiave valore dizionario = {"nome": "io" "cognome": "mio"}


range(1, 10, 2)
da 1 a 20 con step 2, accetta anche paramentri, si può anche fare sezione aurea e ecc

in ciclo: break esce dal ciclo, pass passa la mano, exit
* operatore splat, rende esplicito quello che passiamo, come numeri = [*range(1,11)]

coerenza funzionale: con lo stesso codice a parità di input parità di output su macchine diverse

la funzione è un pezzo isolato di codice con sua proprietà
rendono il codice più manutenibile e modulare, a patto di una buona implementazione
unitarie: una singola responsabilità
controllabili: con output per errore
generiche: utilizzabili in più contesti

funzione vs procedura (qui non esiste davvero la distinzione, ma ci sono con e senza return semplicemente)


parametro vs argomento
stampa("Alice") vs stampa(stringa)

dizionario: dict = {nome: "Alice", cognome: "Aliciani"}
keys() lista chiavi
values() lista valori
items() lista coppia-valore
get() ottieni valore da chiave, anche se chiave non esiste
update(key value) per aggiungere

decoratore: funzione che modifica una funzione o metodo senza modificarlo
servono per aggiungere logging, caching, access control
DEVE avere @ sopra la funzione che incapsula

def decoratore
    def wrapper()
        print()
        funzione()
        print()
    return wrapper

il wrapper esegue codice prima e dopo la funzione, può modificare argomenti e keywords con *args e **kwargs
i decoratori funzionano perché le funzioni possono essere fornite come argomento ad una funzione, assegnate a variabili, o in output


f stringa
print(f "io ho " {29} " anni")
oppure metti le virgole "io ho ", 29, " anni"
string escape: "\



slicing di liste
lista[1:5] da 1 a 5
lista[:-1] togli ultimo
lista[::-1] reverse con step -1


set = {1, 2, 3, "stella"}


le classi sono delle variabili di tipo non basilari


oggetto = istanza unica di classe

negli oggetti il primo attributo è sempre self
__init__ è il costruttore


git e versionamento:
conserva la storia / branching e merging (branch quando modifichi, poi merge) / gestione conflitti
github crea snapshot di versioni, ogni modifica è legata a criteri di integrità

metodi privati __nome__ non printabili all'esterno, si ereditati dai figli, ma sarebbe meglio non richiamarli al di fuori della classe padre
metodi protected _nome_ printabili all'esterno, si ereditati dai figli


in python non abbiamo le interfacce, usiamo le classi astratte che non possono essere istanziate per legare classi ad altre

duck typing: tipo o classe meno importanti dei metodi e attributi
if it walks like a duck, quacks like a duck, then it's a duck

importa
from abc import ABC, abstractmethod
metti ABC nella signature della classe astratta

nei metodi metti prima:
    @abstractmethod

sicurezza = capacità di resistere ad intrusione
robustezza = capacità di non cadere in errore

cast implicito = 3 + 3.0 (int + float)
casting esplicito = str(3) = "3"

pip = pip installs packages
PyPI = python package index, repository di librerie python

numpy = libreria open source per calcolo scientifico applicato alla programmazione, machine learning e analisi dati
qui abbiamo gli array veri e propri, come struttura dati e non un tipo

installazione pacchetti da fonti multiple (PyPI / GitHub ecc.)
gestione dipendenze tra i pacchetti
aggiornamento e rimozione di pacchetti
gestione delle versioni
integrazioni con ambienti virtuali (venv o virtualvenv)

ndarray: numpy data array
nunpy supporta array multidimensionali, ha operazioni matriciali e algebriche, trasformazioni di fourier e funzioni statistiche
integra anche per c/c++ e fortran, con strumenti di ottimizzazione

dtype (data type dell'array stesso) / shape (dimensioni massime dell'array) / arange (funzione per valori sequenziali)
reshape (cambia shape senza modifiche ai dati) / linspace (ndarray di valori equidistribuiti tra start e finish)
random (genera distribuzioni randomn, o anche normali e uniformi) / sum, media, deviazione standard (somma, media, deviazione standard)


'''