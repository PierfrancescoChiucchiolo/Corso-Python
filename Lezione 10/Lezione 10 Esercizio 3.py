'''

database scolastico in .txt, aggiungere alunni e voti, aggiungi alunni, aggiungi voto, media voti

formato del file:
aldo
4, 5, 6, 8, 10
giovanni
8, 9, 10, 9, 8
giacomo
1, 2, 1, 1, 2



'''


def read_text_db(filepath):
    with open(filepath, "r", encoding = "utf-8") as file:
        stringa = file.read()
    righe = stringa.splitlines()

    dizionario = {}
    for indice in range(0, len(righe) - 1 // 2, 2):
        newdict = {righe[indice].replace("/n", "") : righe[indice + 1].replace("/n", "")}
        dizionario.update(newdict)
    return dizionario


diz = read_text_db("text_db.txt")
print(diz)

def write_text_db(dizionario):
    with open("text_db2.txt", "w", encoding = "utf-8") as file:
        for key in dizionario.keys():
            stringa1 = key + "\n"
            stringa2 = dizionario.get(key) + "\n"
            file.write(stringa1)
            file.write(stringa2)
        


write_text_db(diz)