
## rubata da https://www.pythonpool.com/check-if-number-is-prime-in-python/
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True



## stampa fattori in comune di 2 numeri di input, se non ci sono restituisci 1 e "sono coprimi"
## caso simile se si tratta di stringhe e sono coprime, o uguali (cas e sac) ad esempio



input1 = (input("Inserisci un numero Intero, oppure una stringa: "))
input2 = (input("Inserisci un altro numero Intero, oppure un' altraa stringa: "))



if input1.isdigit() and input2.isdigit() and int(input1) > 0 and int(input2) > 0:
    comuni = []
    input1 = int(input1)
    input2 = int(input2)

    #mi garantisce che input1 sia >= input2
    if input1 < input2:
        appoggio = input1
        input1 = input2
        input2 = appoggio
    
    #trova fattori del minore, che è sempre input2, se dividono input1 allora li aggiungo
    for i in range(2, input2):
        if isprime(i):
            comuni.append(i+1)
    
    for primo in comuni:
        if input1 % primo == 0:
            print("i due numeri hanno il fattore " + str(primo) + " in comune")
            pass
        else:
            comuni.remove(primo)


elif isinstance(input1, str) and isinstance(input2, str):
    if len(input1) != len(input2):
        print("Stringhe di diversa lunghezza, non saranno mai complementari.")
    else:
        for index in range(len(input1)):
            if input1[index] in input2:
                input2.replace(input1[index], "")
                input1.replace(input1[index], "")
            else:
                print("le due stringhe non sono complementari")
                break
        print("le due stringhe sono complementari")


else:
    print("Errore di tipo")


