'''

personale cucina classe padre: nome / eta
metodi: lavora

classi figlie chef / souschef / cuocolinea:
chef: specializzazione tipo cucina / prepara menu
souschef: gestisci inventario / assiste chef
cuocolinea: cucina piatto


importa
from abc import ABC, abstractmethod
metti ABC nella signature della classe astratta

nei metodi metti prima
    @abstractmethod

'''

from abc import ABC, abstractmethod

## TODO RISTORANTE aggiungi personale
## TODO ORDINAZIONE lista piatti, feedback piatto e chef che ha cucinato
## TODO CLIENTE budget
## TODO MENU dizionario nome : piatto
## TODO PIATTO nome, lista di istruzioni, lista di ingredienti, costo
## TODO TASK lista di istruzioni
## TODO INVENTARIO dizionario nome : quantita
## TODO INGREDIENTE nome (non servirebbe, basta inventario)

class Ristorante():
    def __init__(self, nome, personale = {}, inventario = {}, menu = {}, ordinazioni = []):
        self.nome = nome
        self.personale = personale
        self.inventario = inventario
        self.menu = {}
        self.ordinazioni = []


    def aggiungi_personale(self, personale):
        newdict = {personale.nome : personale}
        self.personale.update(newdict)

    def aggiungi_inventario(self, ingrediente, quantita):
        self.inventario.aggiungi(ingrediente, quantita)

    def aggiungi_ordinazione(self, ordinazione):
        self.ordinazioni.append(ordinazione)

class Ordinazione():
    def __init__(self, cliente, piatti = []):
        self.cliente = cliente
        self.piatti = piatti
        self.feedback = []

    def feedback(self, piatto, fpiatto, fchef):
        if piatto in self.piatti:
            tupla = (self.piatti.index(piatto), fpiatto, fchef)
            self.feedback.append(tupla)

class Cliente():
    def __init__(self, nome, budget):
        self.nome = nome
        self.budget = budget
    
    def ordina(self, piatto):
        ordinazione1 = Ordinazione(self.nome, piatto)
        self.budget -= piatto.costo
        return ordinazione1
    

class Inventario():
    def __init__(self, dizionario = {}):
        self.dizionario = dizionario

    def check(self, ingrediente):
        return ingrediente in self.dizionario.values()
    
    def quantita(self, ingrediente):
        if self.check(ingrediente): return self.dizionario.get(ingrediente)

    def aggiungi(self, ingrediente, quantita):
        if not self.check(ingrediente):
            newdict = {ingrediente : quantita}
            self.dizionario.update(newdict)
        else:
            newdict = {ingrediente : quantita + self.quantita(ingrediente)}
            self.dizionario.update(newdict)


class Piatto():
    def __init__(self, nome, tipo, istruzioni, ingredienti, costo):
        self.nome = nome
        self.tipo = tipo
        self.istruzioni = istruzioni.splitlines()  ## dovrebbe automaticamente mettere la lista di istruzioni
        self.ingredienti = ingredienti.splitlines() ## ritorna automaticamente la lista ingredienti
        self.costo = costo

    

class Personale(ABC):
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        

@abstractmethod
def lavora(self):
    pass
    

class Chef(Personale):
    def __init__(self, nome, eta, specializzazione, ricettario = {}):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
        self.ricettario = ricettario

    def impara_piatto(self, piatto):
        if piatto.tipo == self.specializzazione:
            newdict = {piatto.nome : piatto}
            self.ricettario.update(newdict)

    def lavora(self, ristorante):
        self.prepara_menu(ristorante)

    def prepara_menu(self, ristorante):
        menu = {}
        for piatto in self.ricettario:
            for ingrediente in piatto.ingredienti:
                if not ristorante.inventario.check(ingrediente): pass
                newdict = {piatto.nome : piatto}
                menu.update(newdict)
        ristorante.menu.update(menu)

class SousChef(Personale):
    def __init__(self, nome, eta, chef):
        super().__init__(nome, eta)
        self.chef = chef

    def assisti_chef(self, ristorante, chef):
        for piatto in chef.ricettario:
            for ingrediente in piatto.ingredienti:
                if not ristorante.inventario.check(ingrediente):
                    ristorante.inventario.aggiungi(ingrediente, 10)


    def lavora(self, ristorante, chef):
        self.assisti_chef(ristorante, chef)


## tecnicamente inutile, assisti_chef è già di per se gestisci inventario
## perché controlla i piatti che lo chef può fare e se non ci sono gli ingredienti li compra
'''
def gestisci_inventario(self, inventario):
    for ingrediente in task:
        if ingrediente not in inventario:
            inventario.add(ingrediente)
'''


## cuocolinea: cucina piatto in linea di produzione
class CuocoLinea(Personale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)


######            ristorante.inventario.aggiung(ingrediente, -1)

def prepara_piatto(self, ristorante):
    for ordinazione in ristorante.ordinazioni:
        for piatto in ordinazione.piatti:
            for ingrediente in piatto.ingredienti:
                if not ristorante.inventario.check(ingrediente): pass
                ristorante.inventario.aggiungi(ingrediente, -1)


def lavora(self, ristorante):
    self.prepara_piatto(ristorante)




piatto1 = Piatto("Spaghetti", "Italiana", "Metti l'acqua a bollire. Cuoci gli spaghetti.", "Spaghetti", 5)
piatto2 = Piatto("Carne ai ferri", "Italiana", "Cuoci la carne ai ferri", "Carne", 10)
piatto3 = Piatto("Ciambellone", "Italiana", "Fai il ciambellone", "Uova. Farina. Latte.", 8)
ricettario1 = {piatto1.nome : piatto1, piatto2.nome : piatto2, piatto3.nome : piatto3}
ricettario2 = {piatto1.nome : piatto1, piatto2.nome : piatto2}

chef1 = Chef("Mike", 30, "Italiana", ricettario1)
souschef1 = SousChef("Aldo", 26, chef1)
cuoco1 = CuocoLinea("Giovanni", 28)
chef2 = Chef("Giacomo", 29, "Italiana", ricettario2)
print(chef2.ricettario)
print("Mike insegna a Giacomo il ciambellone")
chef2.impara_piatto(piatto3)
print(chef2.ricettario)

print(piatto1.ingredienti)
stringa = "Metti l'acqua a bollire. Cuoci gli spaghetti."
print(stringa.splitlines())

inventario1 = Inventario()
ristorante1 = Ristorante("Da Mike Il Pazzo", {}, inventario1, {}, [])
print("Al ristorante manca il personale!")
ristorante1.aggiungi_personale(chef1)
ristorante1.aggiungi_personale(souschef1)
ristorante1.aggiungi_personale(cuoco1)
ristorante1.aggiungi_personale(chef2)


print("Mancano gli ingredienti! Aldo vai a prenderli!")
souschef1.assisti_chef(ristorante1, chef1)

