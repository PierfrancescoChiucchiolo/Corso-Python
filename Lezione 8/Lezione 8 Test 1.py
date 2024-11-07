'''

Chiucchiolo Pierfrancesco pierfrancescochiucchiolo@gmail.com

Es 1: Crea un sistema ripetibile che si occupi di dividere su tre possibili liste i tipi basilari di dato che riceve in entrata.
Deve poter stampare una lista singola o tutte.   Richiede: un oggetto come esecutore


'''

## es1

'''
input1 = [1, 3.0, True, "Caravaggio"]

int_float_double = []
stringhe = []
booleani = []
lista = [int_float_double, stringhe, booleani]


for x in input1:
    if x == True: booleani.append(x)
    elif x == False: booleani.append(x)
    elif type(x) == float: int_float_double.append(x)
    elif type(x) == int: int_float_double.append(x)
    else: stringhe.append(x)

print(lista)
'''

## blocchi di codice / classi / valori / collezioni

## La capacità di poter eseguire lo stesso codice su macchine diverse e, a parità di input, ricevere parità di output

## Che viene utilizzata solo per la sua funzionalità operativa



## Es 2:  Crea una sistema ripetibile che dopo aver preso in input X parole e/o numeri e li aggiunga a una collezione
## si deve ripetere tante volte quante l'utente richiede e poi stampare tutti gli elementi nella lista che non si ripetono.
## Richiede: Che ogni valore o aggregazione dell'oggetto siano incapsulati 


'''
inputbase = input("Dammi un elenco di valori, numeri o parole, li aggiungerò ad una collezione, stop per uscire")
dizionario = {}

while inputbase != "stop":
    for valore in inputbase.split():
        newdict = {}
        if valore not in dizionario.keys():
            newdict = {valore : 0}
        else:
            occorrenze = dizionario.get(valore)
            newdict = {valore : occorrenze + 1}
        dizionario.update(newdict)
    print(dizionario)

    inputbase = input("Dammi un elenco di valori, numeri o parole, li aggiungerò ad una collezione, stop per uscire")

'''


## elif

##Una classe è una sorta di schema, o stampino
# contiene tutta una serie di caratteristiche e funzioni (ovvero attributi e metodi) proprie degli oggetti
# che fanno parte della classe e sono comuni ai rappresentanti delle classi stesse, ovvero degli oggetti che sono creati tramite esse


##uguale

##Es 3:  Crea un sistema che permetta di valorizzare una lista di 5 numeri per due volte
# dopodiché somma ogni posizione con la corrispettiva dell'altra aggregazione e stampa i risultati
# alla fine chiedi se si vuole ripete.                                                                                                                                                Richiede: L'uso di due oggetti, ognuno deve contenere una delle due aggregazioni da confrontare il confronto deve avvenire in una funzione polimorfica 

'''
inputbase = input("Dammi un elenco pari di numeri, sommerò gli elementi in posizione pari con quelli dispari e li mostrerò, stop per fermare")


while inputbase != "stop":
    numeri = inputbase.split()
    pari = []
    dispari = []
    somma = []
    for indice in range(0, len(numeri)):
        if indice % 2 == 0: pari.append(numeri[indice])
        else: dispari.append(numeri[indice])

    print("La lista di numeri è: ")
    print(numeri)
    print("La lista di elementi in posizione pari è: ")
    print(pari)
    print("La lista di elementi in posizione dispari è: ")
    print(dispari)
    for indice in range(0, len(pari)):
        somma.append( int(pari[indice]) + int(dispari[indice]) )
    
    print("La lista di elementi dopo la somma è: ")
    print(somma)


    inputbase = input("Dammi un elenco di valori, stop per uscire")
'''



## La classe astratta non può essere istanziata e può avere metodi astratti



##Es 4:  Crea un sistema che permetta di ordinare da varie classi figlie di autofficine
# ogni autofficina deve avere disponibile una funzione per riparare un tipo specifico di Veicolo.
# Richiede: Classe autofficine (min 2 figli), Classe Veicolo (min 2 figli ), Classe App_Riparazioni (gestore)

class Veicolo():
    def __init__(self, targa):
        self.targa = targa

class Auto(Veicolo):
    def __init__(self, targa, numero_porte):
        super().__init__(targa)
        self.numero_porte = numero_porte

class Moto(Veicolo):
    def __init__(self, targa, numero_ruote):
        super().__init__(targa)
        self.numero_ruote = numero_ruote

class Autofficina():
    def __init__(self, nome, riparazioni = {}):
        self.nome = nome
        self.riparazioni = riparazioni

    def aggiungi_riparazione(self, veicolo, guasto):
        newdict = {veicolo.targa : (veicolo, guasto)}
        self.riparazioni.update(newdict)

class OfficinaAuto(Autofficina):
    def __init__(self, nome, riparazioni={}):
        super().__init__(nome, riparazioni)

    def aggiungi_riparazione(self, auto, guasto):
        if type(auto) != Auto: pass
        newdict = {auto.targa : (auto, guasto)}
        self.riparazioni.update(newdict)

class OfficinaMoto(Autofficina):
    def __init__(self, nome, riparazioni={}):
        super().__init__(nome, riparazioni)

    def aggiungi_riparazione(self, moto, guasto):
        if type(moto) != Moto: pass
        newdict = {moto.targa : (moto, guasto)}
        self.riparazioni.update(newdict)


class Riparatore():
    def __init__(self, nome, indirizzo, titolare, storico_riparazioni = {}):
        self.nome = nome
        self.indirizzo = indirizzo
        self.titolare = titolare
        self.storico_riparazioni = storico_riparazioni

    def ripara(self, officina, veicolo, guasto):
        officina.aggiungi_riparazione(veicolo, guasto)
        newdict = {veicolo.targa : (veicolo, guasto)}
        self.storico_riparazioni.update(newdict)

auto1 = Auto("AA123BB", 4)
moto1 = Moto("123AB", 2)
off_auto1 = OfficinaAuto("Autoriparo")
off_moto1 = OfficinaMoto("Motoriparo")
riparatore1 = Riparatore("ArtAttack", "Via Dell'Attacco D'Arte 10", "Giovanni Muciaccia")
riparatore1.ripara(off_auto1, auto1, "Mi si è rotto il sedile")
riparatore1.ripara(off_moto1, moto1, "Mi si è rotto il sellino")





## 1) ereditarietà: le classi possono tramandare tra di loro attributi e metodi
# se vengono create in modo da ereditare tali peculiarità dalle classi genitore
# 2) polimorfismo: stessa forma e diverso comportamento, o viceversa
# ad esempio l'operatore + agisce su numeri e stringhe in maniera diversa, ma ha forme simili
# 3) incapsulamento: serve a nascondere la complessità, aumenta robustezza e modularità
# un perfetto esempio è la definizione di funzioni che contengono codice che rende il codice più leggibile e manutenibile.
# l'astrazione non è tecnicamente una regola fondamentale dell'OOP, ma una caratteristica dei linguaggi di programmazione in generale, ci permette di ridurre i concetti in concetti più semplici ma non meno potenti
# ci consente di usare funzioni senza sapere esattamente come operano come ad esempio type(x)


## il print è 3

##Es 5:  Andare a creare un sistema di gestione dei ruoli e delle aule in una scuola
# partendo dalla classe base PROFESSORE andare a creare varie classi astratte che definiscono
# la specifica di[ Materia e numeroStudenti ] e a partire dalla classe studente bisogna andare a riempire l'aula
# con il giusto numero di oggetti.      Richiede:  Classe Professore, Classi astratte(Almeno due), Classe studente/aula 


## avendo studiato molto computer science in generale non conoscevo i decoratori, ho avuto modo di apprenderli un po', il resto era già ben noto da altri linguaggi