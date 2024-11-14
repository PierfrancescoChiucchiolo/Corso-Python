'''

consegna della modifica del file di ieri

all'avvio del programma si crea un utente amministratore
nel menù ci sarà la possibilità di aggiungere gli utenti
ogni utente vede solo i suoi voti e medie, solo l'amministratore può aggiungere voti e studenti e visualizzare tutti gli studenti

md5 algoritmo di criptazione
import hashlib

result = hashlib.md5("ciao".encode.hexdigest())
si confronta se l'input criptato sia uguale al dato criptato sul db




SELECT CASE WHEN ( (SELECT isadmin from users) not false )
    THEN /// query di update ///
    ELSE select 1 from dual where false
END


query con return set vuoto
select 1
from dual
where false


## costruisci la query python per stampare i suoi voti da studente

query = "select * from voti join studenti on voti.id = studenti.id where studenti.id in select users.id from studenti join users on studenti.id = users.id where studenti.name = " + nome


## rendi admin un utente

query = "update users set isadmin where user.id = select users.id from users join studenti on users.id = studenti.id where users.username = " + username


#stampa user

query = "select users.id, users.name, users.isadmin from users"


## inserisci in studenti admin admin



'''



import json

## vuole per forza ' esterno ' e " interno "
filejson = '{"chiave1" : "valore1", "chiave2" : "valore2"}'
filejsonconvertito = json.loads(filejson)
fileestratto = json.dumps(filejsonconvertito, indent = 4)


##API servono per far communicare diversi servizi e linguaggi tra di loro

link1 = "https://open-meteo.com"
link2 = "https://web.postman.co/"

## pip install requests
import requests

response = requests.get("www.google.it")


risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=45.5921&longitude=9.5734&hourly=temperature_2m,precipitation_probability")
"""
print(risposta.json()['latitude'])
"""

risposta_text = risposta.text

risposta_json = json.loads(risposta_text)

print(risposta_json['latitude'])

