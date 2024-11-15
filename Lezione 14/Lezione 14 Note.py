'''

save to json
with open('mydata.json', 'w') as f:
    json.dump(team, f)

'''

import requests
import json


def request_dumper(link):
    response = requests.get(link)
    text_response = response.text
    json_response = json.loads(text_response)
    return json_response



pokejson = request_dumper("https://pokeapi.co/api/v2/pokemon?limit=1100")
print(pokejson)

## scrivi l'intero pokédex
with open("Pokédex.json", "w", encoding = "utf-8") as f:
    json.dump(pokejson, f, indent = 4)


## leggi l'intero pokédex
loaded_data = 0
with open("Pokédex.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data == pokejson)

## popola il Pokèdex
for pokemon in range(loaded_data.get("results")):
    data = request_dumper(loaded_data.get("results")[pokemon].get("url"))
    newdict = {"dati" : data}
    

charizard = loaded_data.get("results")[5]
print(charizard)
