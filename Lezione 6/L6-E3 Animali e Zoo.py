'''

crea classe base animale e classi derivate che rappresentano animali
animale: nome eta
metodi: fai suono

animale figlio:
attributi e metodi specifici

classe zoo stampa tutti gli animali

'''

class Canide():
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def presentazione(self):
        stringa = "Sono " + self.nome + " e ho " + str(self.eta) + " anni"
        return stringa


class Cane(Canide):
    def __init__(self, nome, eta, abbaio):
        Canide.__init__(self, nome, eta)
        self.abbaio = abbaio

    def presentazione(self):
        presentazione = super().presentazione() + " " + self.abbaio
        return presentazione


class Lupo(Canide):
    def __init__(self, nome, eta, ululato):
        Canide.__init__(self, nome, eta)
        self.ululato = ululato

    def presentazione(self):
        presentazione = super().presentazione() + " " + self.ululato
        return presentazione


class Volpe(Canide):
    def __init__(self, nome, eta, urlo):
        Canide.__init__(self, nome, eta)
        self.urlo = urlo

    def presentazione(self):
        presentazione = super().presentazione() + " " + self.urlo
        return presentazione


class Zoo():
    def __init__(self, nome, animali):
        self.nome = nome
        self.animali = animali

    def appello(self):
        for animale in self.animali:
            print(animale.presentazione())

animale1 = Cane("Braccobaldo", 10, "BAU")
animale2 = Lupo("Lucio", 30, "AU-AAAUUUUU")
animale3 = Volpe("Volpe", 20, "We, io mica urlo come le volpe normali, eh")
animale4 = Volpe("Nove Code", 1000, "AAAAAAAAA")

animali = [animale1, animale2, animale3, animale4]
zoo1 = Zoo("Zoo comunale del Fantabosco", animali)
zoo1.appello()