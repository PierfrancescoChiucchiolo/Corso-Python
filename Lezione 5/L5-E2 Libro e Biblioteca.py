'''

crea una biblioteca che stampa libri

'''

class Libro:

    def __init__(self, titolo, autore, genere, anno_pub, testo):
        self.titolo = titolo
        self.autore = autore
        self.genere = genere
        self.anno_pub = anno_pub
        self.testo = testo

    def print_dettagli(self):
        print("Questo libro si chiama: " + self.titolo + " è stato scritto da " + self.autore + " appartiene al genere "
            + self.genere + " pubblicato nell'anno: " + self.anno_pub)

    def print_testo(self):
        print(self.testo)

    def stampa(self):
        self.print_dettagli()
        self.print_testo()


class Biblioteca:

    def __init__(self):
        self.libri = []
    
    def aggiungi_libri(self, libro):
        self.libri.append(libro)

    def stampa_libri(self):
        for libro in self.libri:
            libro.stampa()



libro1 = Libro("Alla ricerca del tempo perduto", "Marcel Proust", "1927", "Narrativa", "Era nascosto dentro l'armadio")
libro2 = Libro("Cent'anni di solitudine", "Gabriel Garcia Marquez", "1967", "Narrativa", "Sono stati anni duri, ma ce l'ho fatta")
libro3 = Libro("Snow crash", "Neil Stephenson", "1992", "Cyberpunk", "Molto figo")
libro4 = Libro("Mirroshades", "Bruce Sterling", "1986", "Cyberpunk", "Molto figo anche questo")

libro1.stampa()
libro2.stampa()
libro3.stampa()
libro4.stampa()

biblioteca = Biblioteca()
biblioteca.aggiungi_libri(libro1)
biblioteca.aggiungi_libri(libro2)
biblioteca.aggiungi_libri(libro3)
biblioteca.aggiungi_libri(libro4)
biblioteca.stampa_libri()