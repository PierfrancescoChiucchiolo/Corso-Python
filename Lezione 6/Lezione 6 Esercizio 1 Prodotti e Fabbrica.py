'''

sistemi di gestione fabbrica con classe prodotto e classi derivate per diversi prodotti

qui torna estremamente utile l'ereditarietà, con classi padri e figlie

classe prodotto: nome stringa / costo_produzione float / prezzo vendita float
metodo calcola_profitto: differenza tra prezzo di vendita e costo di produzione

classi derivate da prodotto:
elettronica e abbigliamento (garanzia e materiale rispettivamente)

classe fabbrica: inventario (collezione di prodotti)
metodi:
aggiungi_prodotto: aggiungi all'inventario
vendi_prodotto: diminuisci quantità in inventario e stampa il profitto
resi_prodotto: aumenta la quantità di un prodotto in inventario



'''

def descrivi_prodotto(prodotto):
    return prodotto.descrivi()

class Prodotto():
    def __init__(self, nome, costo, prezzo):
        self.nome = nome
        self.costo = costo
        self.prezzo = prezzo

    def profitto(self):
        return self.prezzo - self.costo
    
    def descrivi(self):
        stringa = "Il prodotto si chiama " + self.nome + ", ha un costo di produzione pari a: " + str(self.costo) + " e si vende a: " + str(self.prezzo)
        return stringa    
    
class Biglia(Prodotto):
    def __init__(self, nome, costo, prezzo, colore):
        super().__init__(nome, costo, prezzo)
        self._colore_ = colore

    def _get_colore(self):
        return self._colore_
    
    def set_colore(self, colore2):
        self._colore = colore2

    def descrivi(self):
        descrizione = super().descrivi() + " ed è del colore: " + self._colore_
        return descrizione

class Biglietto(Prodotto):
    def __init__(self, nome, costo, prezzo, titolo):
        super().__init__(nome, costo, prezzo)
        self._titolo_ = titolo

    def get_titolo(self):
        return self._titolo_
    
    def set_titolo(self, titolo2):
        self._titolo_ = titolo2
    
    def descrivi(self):
        descrizione = super().descrivi() + " ambito di utilizzo: " + self._titolo_
        return descrizione
        

class Bottiglia(Prodotto):
    def __init__(self, nome, costo, prezzo, capacita):
        super().__init__(nome, costo, prezzo)
        self._capacita_ = capacita

    def get_capacita(self):
        return self._capacita_
    
    def set_colore(self, capacita2):
        self._capacita_ = capacita2

    def descrivi(self):
        descrizione = super().descrivi() + " ha capacità pari a: " + self._capacita_
        return descrizione

class Fabbrica():
    def __init__(self, nome, titolare, p_iva, gruppo = "Senza Gruppo"):
        self.nome = nome
        self.titolare = titolare
        self.p_iva = p_iva
        self.gruppo = gruppo
        self.inventario = {}

    def descrivi(self):
        stringa = "La Fabbrica si chiama: " + self.nome + ", il Titolare è " + self.titolare + ", con Partiva Iva: " + self.p_iva + ", appartiene al gruppo " + self.gruppo
        return stringa

    def aggiungi_prodotto(self, prodotto, quantita):
        lista = [ prodotto, quantita ]
        ## lista contiene prodotto che contiene già il nome, ma mi è utile non spacchettare tutto e lista è facilmente estensibile
        newset = {prodotto.nome : lista}
        self.inventario.update( newset )


        ## torna utile avere un metodo di appoggio per leggibilità codice e per riutilizzabilità in altri metodi
    def get_quantita_prodotto(self, nome_prodotto):
        if nome_prodotto in self.inventario.keys():
            return self.inventario.get(nome_prodotto)[1]
        else:
            print("Prodotto " + nome_prodotto + " non presente")
            return False

        ## anche questo come sopra
    def get_prodotto(self, nome_prodotto):
        if nome_prodotto in self.inventario.keys():
            return self.inventario.get(nome_prodotto)
        else:
            print("Prodotto " + nome_prodotto + " non presente")
            return False

    def set_quantita_prodotto(self, nome_prodotto, quantita):
        attuale = self.get_quantita_prodotto(nome_prodotto)
        if attuale != False:
            self.inventario.get(nome_prodotto)[1] = quantita
        else:
            print("Prodotto " + nome_prodotto + " non presente")
            return False
        


    def vendi_prodotto(self, nome_prodotto, quantita = 1):
            attuale = self.get_quantita_prodotto(nome_prodotto)
            if attuale != False:
                if attuale >= quantita:
                    ## qui posso usare il prodotto in input siccome dovrebbero essere uguali, ma devo necessariamente controllare l'inventario
                    lista = [ self.get_prodotto(nome_prodotto), self.get_quantita_prodotto(nome_prodotto) - quantita ]
                    newset = { nome_prodotto : lista}
                    self.inventario.update(newset)
            



    def resi_prodotto(self, nome_prodotto, numero = 1):
        attuale = self.get_quantita_prodotto(nome_prodotto)
        if attuale != False:
            self.inventario.get(nome_prodotto)[1] = attuale + numero
        else:
            print("Prodotto " + nome_prodotto + " non presente")
            return False
        

    def get_inventario(self):
        stringa = ""
        for key in self.inventario.keys():
            prodotto = self.inventario.get(key)[0]
            quantita = self.get_quantita_prodotto(prodotto.nome)
            stringa += str(key) + ": " + prodotto.descrivi() + " totale in stock: " + str(quantita) + " END"
        return stringa.split("END")
    
    def print_inventario(self):
        stringa = self.get_inventario()
        for linea in stringa:
            print(linea)


prodotto1 = Biglia("Biglie", 1, 2, "Rosso")
prodotto2 = Biglietto("Biglietti", 3, 5, "Trasporto Pubblico Locale")
prodotto3 = Bottiglia("Bottiglie", 1, 3, "1 Litro")

print(prodotto1.descrivi())
print(prodotto2.descrivi())
print(prodotto3.descrivi())

print(prodotto1.profitto())
print(prodotto2.profitto())
print(prodotto3.profitto())

fabbrica1 = Fabbrica("B&B&B", "Benedetto Baglioni", "123456 partita iva", "B Incorporated")
print(fabbrica1.descrivi())

fabbrica1.aggiungi_prodotto(prodotto1, 50)
fabbrica1.aggiungi_prodotto(prodotto2, 2000)
fabbrica1.aggiungi_prodotto(prodotto3, 1000)

fabbrica1.print_inventario()

print("Attualmente ci sono : " + str(fabbrica1.get_quantita_prodotto("Biglie")) + " Biglie")
print("Sto vendendo 10 Biglie")
fabbrica1.vendi_prodotto("Biglie", 10)
print("Attualmente ci sono : " + str(fabbrica1.get_quantita_prodotto("Biglie")) + " Biglie")

print("Sto facendo il reso di 5 Biglie")
fabbrica1.resi_prodotto("Biglie", 5)
print("Attualmente ci sono : " + str(fabbrica1.get_quantita_prodotto("Biglie")) + " Biglie")

print(descrivi_prodotto(prodotto1))
