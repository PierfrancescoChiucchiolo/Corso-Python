
## usiamo replit.com

## programma che chiede in input un numero e stampa il numero è pari o dispari


numero = 10

if numero % 2:
    print("Numero Pari")
else:
    print("Numero Dispari")



numero = 1

if numero % 2:
    print("Numero Dispari")
else:
    print("Numero Pari")


##input di valore da terminale user
n = int(input("Inserisci un numero Intero"))


'''
anno bisestile:
divisibile per 4, ma non 100, a meno che non sia divisibile per 400
'''

anno = int(input("Inserisci un numero Intero"))

if(not anno % 400): print("Anno bisestile")
elif(anno % 4):
    if(anno % 100): print("Anno non bisestile")
    else: print("Anno bisestile")





## crea un sistema di login User / PW  user: admin pw: 1234

username = "Admin"
pw = "1234"
risposta = "5"

print("Benvenuto, prego inserire il nome dell'account:")
data = input("Username:")

if(data == username): print("Utente Admin Riconosciuto")
else: print("Utente Non Riconosciuto")

print("Benvenuto Utente ADMIN, prego digitare la password")
data = input("Inserire la password:")

if(data == pw): print("Credenziali Corrette")
else: print("Credenziali Errate")
    
print("Prego inserire la risposta alla seguente domanda.")
data = input("Quanto fa 2+2?")

if(data == risposta): print("Prego reimpostare la password")
pw = input("Inserire la nuova password:")

print("Password attuale: " + pw)


'''

esercizio su negozio e inventario, gestire e supervisionare le operazioni:

clienti (visualizza articoli / acquista articoli / acquisti effettuati)
inventario nome, prezzo, quantità (nuovo / modifica / rimuovi)
admin (rapporto vendite / stato inventario / guadagni)

'''

user1 = "pippo"
pw1 = "password"
admin1 = "admin"
pw_admin1 = "admin"

'''
prodotto1 = [ prodotto1_nome = "pane", prodotto1_prezzo = 4, prodotto1_quantita = 50, prodotto1_vendite = 0 ]
prodotto2 = [ prodotto2_nome = "acqua", prodotto1_prezzo = 1, prodotto1_quantita = 100, prodotto2_vendite = 0 ]
prodotto3 = [ prodotto3_nome = "bistecca", prodotto1_prezzo = 10, prodotto1_quantita = 5, prodotto3_vendite = 0 ]

prodotti = [prodotto1, prodotto2, prodotto3]

'''


'''

prodotti = ["pane", 4, 50, 0, "acqua", 1, 100, 0, "bistecca", 10, 5, 0]

print("Benvenuto, accesso Admin o Utente?")
data = input("Prego scrivere Admin o Utente:")

if(data == "User"):
    print("Benvenuto, prego inserire il nome dell'account User:")
    data = input("Username:")

    if(data == user1):
        print("Utente Riconosciuto")
        print("Benvenuto Utente, prego digitare la password")
        data = input("Inserire la password:")

        if(data == pw1): print("Credenziali Corrette, login effettuato.")
        else: print("Credenziali Errate")


        ## metti qui il resto
        print("Operazioni disponibili: Visualizza Articoli / Aggiungi Articoli Lista / Rimuovi Articoli Lista")
        data = input("Prego Selezionare: VA / AA / RA")
        if(data == "VA"):
        	for( i in len(prodotti)/4 ):
        		print(prodotti[i] + " pezzi disponibili: " + prodotti[i + 2] + " ogni pezzo costa: " prodotti[i + 1])
        elif(data == "AA"):
        	print("TODO 1")
        elif(data == "RA"):
        	print("TODO 2")
        else: print("Scelta non valida")



    else: print("Utente Non Riconosciuto")

elif(data == "Admin"):
    print("Benvenuto, prego inserire il nome dell'account Admin:")
    data = input("Username:")

    if(data == admin1): print("Admin Riconosciuto")
        print("Benvenuto Admin, prego digitare la password")
        data = input("Inserire la password:")

        if(data == pw_admin1): print("Credenziali Corrette, login effettuato.")
        else: print("Credenziali Errate")


        ## metti qui il resto
        print("Operazioni disponibili: Visualizza Articoli / Aggiungi Articoli / Rimuovi Articoli")
        data = input("Prego Selezionare: VA / AA / RA")
        if(data == "VA"):
        	for( i in len(prodotti)/4 ):
        		print(prodotti[i] + " pezzi disponibili: " + prodotti[i + 2] + " ogni pezzo costa: " prodotti[i + 1])

        elif(data == "AA"):
        	print("Inserimento di nuovo articolo:")
        	prodotti.append(input("Inserire Nome Articolo"))
        	prodotti.append(input("Inserire Prezzo Articolo"))
        	prodotti.append(input("Inserire Quantità Articolo"))
        	prodotti.append(0)        	
        elif(data == "RA"):
        	print("TODO 3")
        else: print("Scelta non valida")



    else: print("Admin Non Riconosciuto")


else: print("Errore nella tipologia di richiesta login")


'''