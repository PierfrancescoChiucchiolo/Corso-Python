'''
scrivi 5 numeri casuali su un txt
utente deve indovinare almeno 2 numeri sul file


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


'''

import random


def genera( n ):
    numeri = ""

    for i in range (0, n):
        numero = random.randint(0, 100)
        numeri += str(numero) + " "

    file = open("numeri_casuali.txt", "w", encoding = "utf-8")
    file.write(numeri)
    file.close()




while True:
    input1 = input("Indovina i numeri, dimmi quanti numeri casuali devo generare, quit per uscire: ")
    if input1 == "quit": exit
    genera(int(input1))
    print("Ho generato un totale di " + str(input1) + " numeri tra 0 e 100, indovinali:")
    tentativi = 10
    indovinate = 0
    print("Hai a disposizione: " + str(tentativi) + " tentativi")

    file = open("numeri_casuali.txt", encoding = "utf-8")
    text = file.read()
    file.close()

    input1 = input("Indovina i numeri, dimmi quanti numeri casuali devo generare: ")
    if input1 == "quit": exit

    if tentativi >= 0:
        for valore in text:
            if input1 == valore:
                print("Numero correttamente indovinato, il tentativo non sarà bruciato")
                print("Hai a disposizione: " + str(tentativi) + " tentativi")
                indovinate += 1
            else:
                print("Hai a disposizione: " + str(tentativi) + " tentativi")
                tentativi += -1


    else:
        print("Gioco terminato, hai indovinato un totale di " + str(indovinate) + " numeri casuali")

