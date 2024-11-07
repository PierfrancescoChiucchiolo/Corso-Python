'''
operaio muratore e carpentiere

classe astratta: operaio, cazzuola, martello
'''

from abc import ABC, abstractmethod


class Operaio(ABC):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    @abstractmethod
    def lavora(self):
        pass

class Cazzuola(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def usa_cazzuola():
        pass

class Martello(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def usa_martello():
        pass


class Muratore(Operaio, Cazzuola, Martello):
    def __init__(self, nome):
        super().__init__(nome)

    def usa_cazzuola(self):
        print("Sono il muratore " + self.nome + " e sto usando la mia cazzuola per stuccare un muro")
        
    def usa_martello(self):
        print("Sono il muratore " + self.nome + " e sto usando il mio martello per rompere un muro")

    def lavora(self):
        self.usa_martello()
        self.usa_cazzuola()

class Carpentiere(Operaio, Cazzuola, Martello):
    def __init__(self, nome):
        super().__init__(nome)

    def usa_cazzuola(self):
        print("Sono il carpentiere " + self.nome + " e sto usando la mia cazzuola per fare un muro di mattoni")
        
    def usa_martello(self):
        print("Sono il muratore " + self.nome + " e sto usando il mio martello per inchiodare delle assi di legno")

    def lavora(self):
        self.usa_martello()
        self.usa_cazzuola()


bob = Muratore("bob")
bob.lavora()

rob = Carpentiere("rob")
rob.lavora()