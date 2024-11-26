'''

esercizio sull'ereditarietà

'''


class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")



class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)  
        # Alternativa a super per l'ereditarietà multipla
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni()  
        # Chiamiamo il metodo della prima superclasse
        print(f"Potenza: {self.cavalli} CV")
        self.mostra_dotazioni()  
        # Possiamo chiamare metodi di entrambe le superclassi

veicolo1 = Veicolo("Fiat", "Panda")
veicolo1.mostra_informazioni()

veicolo1super = AutomobileSportiva("Fiat", "Panda Special", ["Cerchi in Lega"], 1)
veicolo1super.mostra_informazioni()