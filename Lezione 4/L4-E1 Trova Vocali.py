## input parola da utente e output con vocali e indice


vocali = ["a", "e", "i", "o", "u"]

indici = []

input1 = input("Immetti una parola: ")
input2 = input1

## vocal_lists = [vocale for vocale in input1 if vocale in vocali]

for vocale in vocali:
    while input2.find(vocale) != -1 :

        index = [input2.find(vocale)]
        input2 = input2.replace(vocale, " ")
        indici.append(index)
    
    print("Nella stringa di inizio ci sono " + str(len(indici[-1])) + " volte la vocale " + vocale)



## non funziona rip
