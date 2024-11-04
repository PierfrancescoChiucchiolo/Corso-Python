## chiedi all'utente un numero e fai conto alla rovescia fino a zero, stampa ogni numero, poi chiedi un altro numero
## se il numero è primo lo salva e restituisce "numero primo", quando si arriva a 5 numeri primi exit



def primo(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return True
            break
    else:
        return False

## rubata da https://www.pythonpool.com/check-if-number-is-prime-in-python/
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

## inizializzo la lista vuota
primi = []

while len(primi) <= 4:
    n = (input("Inserisci un numero Intero, oppure exit per uscire: "))
    if n == "exit":
        break
    
    n = int(n)
    if isprime(n):
        print("Numero di input è primo: hai inserito un totale di " + str(len(primi) + 1) + " numeri primi.")
        primi.append(n)
    for i in range(n, 0, -1):
        print(i)

