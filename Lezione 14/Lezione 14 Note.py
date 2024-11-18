'''

save to json
with open('mydata.json', 'w') as f:
    json.dump(team, f)

    


selenium è un package python che si struttura similarmente ad html con i tag < body />
scraping è una funzione che scarica massivamente i dati
pip install selenium
'''

import requests
import json
import time

def request_dumper(link):
    response = requests.get(link)
    text_response = response.text
    json_response = json.loads(text_response)
    return json_response


pokejson = request_dumper("https://pokeapi.co/api/v2/pokemon?limit=1100")
##print(pokejson)

## scrivi l'intero pokédex
with open("Pokédex.json", "w", encoding = "utf-8") as f:
    json.dump(pokejson, f, indent = 4)


## leggi l'intero pokédex
loaded_data = 0
with open("Pokédex.json", "r") as file:
    loaded_data = json.load(file)

##print(loaded_data == pokejson)

## il file generato è 384MB ed è troppo pesante, visual studio è crashato nel gestire 7kk righe di json
'''
## popola il Pokèdex
for pokemon in range(len(loaded_data.get("results"))):
    time.sleep(1)
    print("sto dormendo per la volta numero:" + str(pokemon))
    data = request_dumper(loaded_data.get("results")[pokemon].get("url"))
    ##print(data)
    newdict = {"dati" : data}
    ##print("sono nel for numero " + str(pokemon))
    loaded_data.get("results")[pokemon].update(newdict)
## QUI PROBABILMENTE IL SITO NON PERMETTE SCRAPING, SE METTIAMO NUMERI INFERIORI COME RANGE(10) FA UN DUMP COMPLETO DI QUEI 10

'''
with open("PokédexCompleto.json", "w", encoding = "utf-8") as f:
    json.dump(loaded_data, f, indent = 4)


print("ho finito")

'''charizard = loaded_data.get("results")[5]
print(charizard)'''
