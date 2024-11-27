'''
indovina un numero da 1 a 100, printa se maggiore o minore, continua finché non indovini o exit

fibonacci fino ad n
'''

import random

def fibonacci(numero):
    fib = [0, 1]
    num1 = 0
    num2 = 1

    while numero >= num2 + num1:
        appoggio = num1
        num1 = num2
        num2 += appoggio
        fib.append(num2)

    return fib



numero = random.randint(1, 100)
inputbase = input("Scegli indovina oppure fibonacci, altrimenti stop: ")
while inputbase != "stop":

    if inputbase == "indovina":

        guess = input("Indovina il numero tra 1 e 100 ")
        if guess.isdigit():
            if int(guess) != numero:
                if int(guess) < numero:
                    print("Il numero cercato è maggiore di " + guess + " ")
                else:
                    print("Il numero cercato è minore di " + guess + " ")
        elif guess == "stop":
            print( "peccato, il numero è " + str(numero) )
            quit()
            
        else:
            inputbase = input("Corretto, il numero è " + str(numero) + ". Scegli indovina oppure fibonacci, altrimenti stop: ")
    
    elif inputbase == "fibonacci":
        fibnum = input("Inserisci il numero di cui estrarre la sequenza di fibonacci ")
        if not fibnum.isdigit():
            quit()
        fiblist = fibonacci(int(fibnum))
        for elemento in fiblist:
            print(elemento)
    
    elif inputbase == "stop":
        quit()

