'''

io mi occuperò di I/O
iPython è la shell interattiva di python, viene chiamata anche REPL (read eval print loop)
supporto per autocompletamento usando il tasto tab per scorrere i suggerimenti
storia dei comandi: freccia su/giu scorre gli ultimi comandi inseriti
rich output: si possono visualizzare direttamente nella shell grafici e tabelle
supporto OS: si possono richiamare comandi del sistema operativo con ! seguito dai comandi
estensioni: supporta l'utilizzo di plugin

spyder è un IDE (ambiente di sviluppo integrato) per python
editor di codice avanzato / console interattiva / esploratore di variabili (step by step) / debugger step by step / esplora risorse

I/O:
lettura: si usa open con 2 parametri, path e modalità
(read "r" / write "w" / append only "a" / read and write "w+)

file = open("PATH DEL FILE.ESTENSIONE", "r")
contenuto = file.read() legge tutto il file
riga = file.readline() legge di riga in riga

scrittura: si usa sul file aperto con "w" il comando file.write("stringa")
file = open("PATH DEL FILE.ESTENSIONE", "w")
file.write("STRINGA DA SCRIVERE NEL NUOVO FILE")
file.writelines("STRINGA1", "STRINGA2", ...)
file.writelines(L) for L = [str1, str2, str3]
per l'andata a capo usa "stringa \n" alla fine per carattere di endline



chiusura: è importante chiudere il file in modo da liberare le risorse impiegate per aprire il file e la memoria assegnata ad esso
file.close()

with open: funzione che automaticamente chiude il file finito il blocco
with open("PATH DEL FILE.ESTENSIONE", "w") as file:
    contenuto = file.read()
    ## codice
## qui la variabile file viene liberata

lambda / funzioni anonime (inline functions)
non usano def, ma bensì lambda, sono utili soprattutto quando abbiamo piccole funzioni magari da applicare in map/filter/reduce
sono limitate ad una singola linea di codice
square = lambda x**2
result = square(5)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x % 2 == 0, numbers))
print(even)

filter(funzione di filtro, sequenza)
restituisce un iteratore, prendendo gli elementi da sequenza, se true vanno nella variabile

is_even = lambda x % 2 == 0
even = list(filter(is_even, numbers))

sicurezza:
è importante aggiornare i softare, sanificare gli input utente per prevenire l'iniezione di codice
usare input() / rawinput() / escape() per input da tastiera
bcrypt o argon2 sono algoritmi di hashing sicuri per criptare password (python offre libreria cryptography)
usare 2FA laddove necessario
considerare l'affidabilità delle librerie di terze parti, quanto sono diffuse e supportate, aggiornate
logging e monitoraggio del codice e delle risorse
usare pip-check per controllare le vulnerabilità delle librerie
fare audit del codice con strumenti come bandit o pylint
usare django o flask come framework che resistono a  XSS cross site scripting / CSRF cross site request forgery / iniezione di codice
protezione da ddos come firewall o sistemi 3rd party
limitare accesso a file e socket solo a processi autorizzati
esegui penetration tests o vulnerability tests 

co-authoring: collaborazione con altri utenti
usare branches dalla branch master e poi fare merge
pull request: richiesta di implementare un branch nel master
CI continuous integration: strumenti come jenkins o travis ci per automatizzare i check di analisi e rilascio
convenzioni: assicurarsi di mantenere un codice coerente


monitoring: monitoraggio delle prestazioni
risorse di sistema: psutil per moonitorare cpu/memoria/disco/rete
prestazioni dell'applicazione: time e datetime per rilevare ritardi ed inefficienze
monitoraggio dei log: contengono errori, eccezioni e anomalie
metriche personalizzate: Prometeus o StatD per ricevere statistiche su numero richieste elaborate, tempo di risposta
errori: Sentry o Rollbar tengono traccia degli errori dell'applicazione
API: Swagger o OpenAPI generano documentazione e log sulle API come numero richieste elaborate, tempo di risposta
infrastruttura: se distribuita o su un cloud usiamo Docker per monitorare i cluster 



'''








'''
## rubato da https://www.geeksforgeeks.org/create-a-new-text-file-in-python/:

from pathlib import Path
import io


# Using open() function
file_path = "new_file.txt"

# Open the file in write mode
with io.open(file_path, "w", encoding="utf-8") as file:
    # Write content to the file
    file.write("Hello, this is a new text file created using open() function")
    
print( "File '{file_path}' created successfully")




## rubato da https://www.geeksforgeeks.org/writing-to-file-in-python/

# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()


'''
## elemento della lista è formato così
{"username": "stringa", "password": "stringa", "score": 0.9, "id": 0}
class User():
    def __init__(self, username, password, score=0):
        self.username = username
        self.password = password
        self.score = score

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_score(self):
        return self.score

    def set_score(self, new_score : float):
        pass


## output in lista di dizionari
outputoof = [
    {"username": "Gianni", "password": "1234", "score": 0.9, "id": 1},
    {"username": "Morand", "password": "567", "score": 0.8, "id": 2},
    {"username": "Aldo", "password": "1111", "score": 0.7, "id": 3},
    {"username": "Giovanni", "password": "2222", "score": 0.6, "id": 4},
    {"username": "Giacomo", "password": "3333", "score": 0.5, "id": 5},
    {"username": "Lupo Lucio", "password": "0000", "score": 1.0, "id": 6},

]

user1 = User("Gianni", "1234", 0.9)
user2 = User("Morand", "567", 0.8)
user3 = User("Aldo", "2222", 0.6)
user4 = User("Giovanni", "2222", 0.6)
user5 = User("Giacomo", "3333", 0.5)
user6 = User("Lupo Lucio", "0000", 0.4)

output = {user1.get_score : user1, user2.get_score : user2, user3.get_score : user3, 
          user4.get_score : user4, user5.get_score : user5, user1.get_score : user5,
          user6.get_score : user6}


'''
def key_swap(dizionario):
    newdict = {}
    for elemento in dizionario.values():
        pezzo = {elemento.get_score() : elemento}
        newdict.update(pezzo)
    return newdict

def ordinatore(dizionario):
    lista = []
    for elemento in dizionario.values():
        pass
'''

def deconstructor(dizionario):
    stringa = ""
    for elemento in dizionario.values():
        parziale = "Giocatore: " + elemento.get_username() + " punteggio: " + str(elemento.get_score()) + " \n"
        stringa += parziale
    return stringa


def io_classifica(stringa):
    file1 = open("classifica.txt", "w", encoding = "utf-8")

    # Writing multiple strings
    # at a time
    file1.writelines(stringa)

    # Closing file
    file1.close()



stringa = deconstructor(output)
print("questo è il decostruttore")
print(stringa)


file1 = open("classifica.txt", "w", encoding = "utf-8")

# Writing multiple strings
# at a time
file1.writelines(stringa)

# Closing file
file1.close()

# Checking if the data is
# written to file or not
file1 = open("classifica.txt", "r")
print(file1.read())
file1.close()



