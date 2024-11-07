'''

personale cucina classe padre: nome / eta
metodi: lavora

classi figlie chef / souschef / cuocolinea:
chef: specializzazione tipo cucina / prepara menu
souschef: gestisci inventario / assiste chef
cuocolinea: cucina piatto in linea di produzione


importa
from abc import ABC, abstractmethod
metti ABC nella signature della classe astratta

nei metodi metti prima
    @abstractmethod

'''

from abc import ABC, abstractmethod

## TODO MENU dizionario nome : piatto
## TODO PIATTO nome, lista di istruzioni, lista di ingredienti
## TODO TASK lista di istruzioni
## TODO INVENTARIO dizionario nome : quantita
## TODO INGREDIENTE nome

class Personale():
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

@abstractmethod
def lavora(self):
    pass
    

class Chef(Personale):
    def __init__(self, nome, eta, specializzazione, tasks = [] ):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
        self.tasks = tasks

def lavora(self, task):
    pass

def prepara_menu(self, menu):
    for piatto in menu:
        for task in piatto.istruzioni:
            self.tasks.append(task)


class SousChef(Personale):
    def __init__(self, nome, eta, chef):
        super().__init__(nome, eta)
        self.chef = chef

def assisti_chef(self):
    for task in self.chef.tasks():
        self.lavora(task)

def lavora(self, task):
    pass

def gestisci_inventario(self, inventario):
    for ingrediente in task:
        if ingrediente not in inventario:
            inventario.add(ingrediente)



## cuocolinea: cucina piatto in linea di produzione
class CuocoLinea(Personale):
    def __init__(self, nome, eta, coda = [] ):
        super().__init__(nome, eta)
        self.coda = coda

def lavora_coda(self):
    for task in self.coda:
        self.lavora(task)

def lavora(self, task):
    pass