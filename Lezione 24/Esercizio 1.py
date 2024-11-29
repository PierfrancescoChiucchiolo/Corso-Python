## gestore libri

class libro():
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def descrivi():
        stringa = "Il libro si chiama " + self.titolo + ", scritto da: " + self.autore + " nell'anno " + self.anno
        return stringa

    
class libreria():
    def __init__(self):
        self.lista = []
        self.quantita = []

    def aggiungi(libro, quantita):
        if cerca( libro.nome ):
            indice = lista.index(libro.nome)
            self.quantita[indice] += quantita
        else:
            self.lista.append(libro)
            self.quantita.append(quantita)

    def rimuovi(libro, quantita):
        if cerca( libro.nome ):
            indice = lista.index(libro.nome)
            self.quantita[indice] = max(0, self.quantita[indice] - quantita) 
        else:
            print("Libro non presente")        


    def mostra():
        return self.lista
    
    def cerca(stringa):
        for libro in self.lista:
            if libro.titolo == stringa: return libro
            else: return False
    

def menu():
    print("Scrivere Aggiungi per aggiungi libro ")
    print("Scrivere Visualizza per visualizza libri ")
    print("Scrivere Cerca per cerca libro ")
    print("Scrivere Gestione per aggiungi libro ")
    print("Scrivere Esci per aggiungi libro ")


libreria1 = libreria()

while(True):
    menu()
    input1 = input("Prego inserire un comando: ")
    if input1 == "Aggiungi":
        input2 = input("Prego inserire il titolo")
        input3 = input("Prego inserire l'autore")
        input4 = input("Prego inserire l'anno di pubblicazione")
        input5 = input("Prego inserire la quantità desiderata")
        libro1 = libro(input2, input3, input4)
        libreria1.aggiungi(libro1, int(input5))


    elif input1 == "Visualizza":
        for i in len(self.lista):
            descrizione = self.lista[i].descrivi()
            print(descrizione + " in quantità pari a " + str(self.quantità(i)) )

    elif input1 == "Cerca":
        input2 = input("Prego inserire il titolo")
        libro1 = libreria1.cerca(input2)
        if libro1 != False:
            print("Il libro è presente nella libreria")
            descrizione = libro1.descrivi()
            indice = self.lista.index(libro.nome)
            print(descrizione + " in quantità pari a " + str(self.quantità(indice)) )
        else: print("Libro non presente")


    elif input1 == "Gestione":
        input2 = input("Prego inserire il titolo del libro da modificare")
        libro1 = libreria1.cerca(input2)
        if libro1 != False:
            print("Il libro è presente nella libreria")
            descrizione = libro1.descrivi()
            indice = self.lista.index(libro.nome)
            print(descrizione + " in quantità pari a " + str(self.quantità(indice)) )

            input2 = input("Prego inserire il titolo")
            input3 = input("Prego inserire l'autore")
            input4 = input("Prego inserire l'anno di pubblicazione")
            input5 = input("Prego inserire la quantità desiderata")
            
            del self.lista[indice]
            del self.quantita[indice]

            libro1 = libro(input2, input3, input4)
            libreria1.aggiungi(libro1, int(input5))

        else: print("Libro non presente")

    elif input1 == "Esci":
        break

