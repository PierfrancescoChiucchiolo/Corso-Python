'''
Descrizione: utente inserire un numero intero positivo n

Utilizzare un ciclo while un numero positivo altrimenti continua
Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
Utilizzare una struttura if per determinare se n è un numero primo.

'''

## rubata da https://www.pythonpool.com/check-if-number-is-prime-in-python/
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True


inputbase = input("Digitare un numero intero: ")
while str(int(inputbase)) != inputbase:
    inputbase = input("Digitare un numero intero: ")

numero = int(inputbase)

somma = 0
for addendo in range(0, numero+1):
    somma += addendo
print("La somma di tutti gli addendi da 0 a " + str(numero) + " è uguale a: " + str(somma))

for dispari in range(0, numero):
    if dispari % 2 != 0:
        print("Il numero " + str(numero) + " ha come numero dispari precedente: " + str(dispari))

if isprime(numero):
    print("Il numero " + str(numero) + " è un numero primo")
else:
    print("Il numero " + str(numero) + " NON è un numero primo")

