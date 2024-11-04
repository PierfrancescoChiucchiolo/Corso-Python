'''

1: di pari o dispari
2: stampa tutti gli interi positivi da n a 0 decrementando di 1
3: stampa quadrati di una lista di numeri
4: lista di interi, trova max con for, while per contare, if se è vuota stampa "lista vuota"
4.1: adegua alle stringhe


'''

interi = []


inputbase = input("Digitare qui i numeri interi da utilizzare, poi scrivere stop per continuare: ")
while inputbase != "stop":
    interi.append(inputbase)
    inputbase = input("Digitare un nuovo numero o scrivere stop: ")



input1 = input("Digitare 1 per Pari/Dispari, 2 per stampa discendente, 3 per quadrati, 4 per max/count/empty, stop per uscire: ")
while input1 != "stop":

    if input1 == "1":
        for numero in interi:
            if int(numero) % 2 == 0:
                print("Numero pari: " + str(numero) )
            else:
                print("Numero dispari: " + str(numero) )
        input1 = input("Digitare 1 per Pari/Dispari, 2 per stampa discendente, 3 per quadrati, 4 per max/count/empty, stop per uscire: ")


    elif input1 == "2":
        for numero in interi:
            for discendente in range(int(numero), 0, -1):
                print(discendente)
        input1 = input("Digitare 1 per Pari/Dispari, 2 per stampa discendente, 3 per quadrati, 4 per max/count/empty, stop per uscire: ")


    elif input1 == "3":
        for numero in interi:
            print(int(numero) * int(numero))
        input1 = input("Digitare 1 per Pari/Dispari, 2 per stampa discendente, 3 per quadrati, 4 per max/count/empty, stop per uscire: ")



    elif input1 == "4":

        max = 0
        for numero in interi:
            if int(numero) <= max:
                max = int(numero)
        print("il max è il numero: " + numero)

        sum = 0
        while len(interi) != 0:
            sum += int(interi.pop(-1))
        print("la somma dei valori è: " + str(sum))
        
        input1 = input("Digitare 1 per Pari/Dispari, 2 per stampa discendente, 3 per quadrati, 4 per max/count/empty, stop per uscire: ")


    else:
        print("input non riconosciuto")





