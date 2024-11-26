'''

crea ristorante:
costruttore nome, tipo_cucina, aperto = false, dizionario piatti/prezzi

metodi:
descrivi() stampa la descrizione del ristorante
aperto() aperto o no
apri() stato -> aperto = true
chiudi() stato -> aperto = false
aggiungi_piatto()
togli_piatto()
stampa_menu()

crea istanza e testa


'''


class Ristorante:

    def __init__(self, nome, tipo_cucina, aperto = False):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.menu = {}
        self.aperto = aperto


    def descrivi(self):
        print("Il ristorante si chiama " + self.nome + ", serve cucina " + self.tipo_cucina)
        if self.aperto: print("Il ristorante è attualmente aperto")
        else: print("Il ristorante è attualmente chiuso")


    def stato_apertura(self):
        if self.aperto: print("Il ristorante " + self.nome + " è aperto")
        else: print("Il ristorante " + self.nome + " è chiuso")
    
    def apri(self):
        if self.aperto: print("Ristorante già aperto")
        else:
            self.aperto == True 
            print("Il ristorante " + self.nome + " sta aprendo")

    def chiudi(self):
        if self.aperto: print("Ristorante già chiuso")
        else:
            self.aperto == False
            print("Il ristorante " + self.nome + " sta chiudendo")

    def aggiungi_piatto(self, nome, prezzo):
        ## suppongo inserire di nuovo un piatto con lo stesso nome equivalga a sovrascriverlo/aggiornarlo
        self.menu.update( {nome : prezzo} )

    def rimuovi_piatto(self, nome):
        if nome in self.menu.keys():
            self.menu.pop(nome)
        else:
            print("Il piatto con il nome " + nome + "non è presente sul menu")

    def stampa_menu(self):
        for chiave in self.menu.keys():
            print("Piatto: " + chiave + " Prezzo: " + str(self.menu.get(chiave)))



ristorante1 = Ristorante("Da Mike il pazzo", "Cinese")
ristorante2 = Ristorante("Trattoria Nonna Papera", "Italiana")
ristorante3 = Ristorante("Sushi Chin Chan Pai", "Giapponese")

ristorante1.stato_apertura()

## è già chiuso di default
ristorante1.chiudi()

ristorante1.apri()
ristorante2.apri()
ristorante3.apri()

## è già aperto
ristorante1.apri()


ristorante1.descrivi()
ristorante2.descrivi()
ristorante3.descrivi()

ristorante1.aggiungi_piatto("Involtini primavera", 10)
ristorante1.aggiungi_piatto("Riso fritto", 15)

ristorante2.aggiungi_piatto("Spaghetti", 8)
ristorante2.aggiungi_piatto("Tagliata ai ferri", 10)

ristorante3.aggiungi_piatto("Nigiri di salmone", 5)
ristorante3.aggiungi_piatto("Sashimi di tonno", 4)

ristorante1.stampa_menu()
ristorante2.stampa_menu()
ristorante3.stampa_menu()

## OH NOH! ABBIAMO FINITO LA CARNE PRESSO LA TRATTORIA NONNA PAPERA
ristorante2.rimuovi_piatto("Tagliata ai ferri")
ristorante2.stampa_menu()









    
