## fai media voti per ogni alunno, prendi input nome e voti



def average(lista):
    totale = 0
    for elemento in lista:
        totale += int(elemento)
    return totale/len(lista)


dizionario = {}

inputbase = input("Scrivi nome per cominciare, media per fare la media degli alunni, oppure stop per terminare: ")
while inputbase != "stop":
    input1 = input("Prego inserire i voti, oppure fine per tornare indietro ")
    dizionario.update( {inputbase : []} )
    print(dizionario)
    print(dizionario.get(inputbase))

    if input1 != "fine":
        dizionario.get(inputbase).append(input1)
        input1 = input("Prego inserire i voti, oppure fine per tornare indietro ")

    
    if input1 == "media":
        for key in dizionario:
            print(key + average(dizionario[key]))

