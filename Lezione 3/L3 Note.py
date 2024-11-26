'''

la funzione è un pezzo isolato di codice con sua proprietà
rendono il codice più manutenibile e modulare, a patto di una buona implementazione
unitarie: una singola responsabilità
controllabili: con output per errore
generiche: utilizzabili in più contesti

funzione vs procedura (qui non esiste davvero la distinzione, ma ci sono con e senza return semplicemente)


parametro vs argomento
stampa("Alice") vs stampa(stringa)

dizionario: dict = {nome: "Alice", cognome: "Aliciani"}
keys() lista chiavi
values() lista valori
items() lista coppia-valore
get() ottieni valore da chiave, anche se chiave non esiste
update(key value) per aggiungere

decoratore: funzione che modifica una funzione o metodo senza modificarlo
servono per aggiungere logging, caching, access control
DEVE avere @ sopra la funzione che incapsula

def decoratore
    def wrapper()
        print()
        funzione()
        print()
    return wrapper

il wrapper esegue codice prima e dopo la funzione, può modificare argomenti e keywords con *args e **kwargs
i decoratori funzionano perché le funzioni possono essere fornite come argomento ad una funzione, assegnate a variabili, o in output


'''