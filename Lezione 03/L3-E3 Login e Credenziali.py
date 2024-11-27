
'''
1: inserisci username e password
2: verifica login
3: benvenuto o errore
4: cambia pw e chiedi domanda segreta, animale o colore preferito

'''

import random, string

## rubato da: https://stackoverflow.com/questions/2030053/how-to-generate-random-strings-in-python
def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def expander(lista):
    stringout = ''
    for elemento in lista:
        stringout += elemento
        stringout += ' '
    stringout[:-1]
    return stringout
    ##dovrebbe rimuovere l'ultimo ' ' che ho aggiunto

##dizionario con credenziali user/pw

credentials = {"Alice" : "123", "Admin" : "1234"}
secret_animal = {"Alice" : "Cavallo", "Admin" : "Cane"}
secret_color = {"Alice" : "Nero", "Admin" : "Rosso"}
animal_list = ["Cavallo", "Cane", "Gatto", "Serpente"]
color_list = ["Nero", "Rosso", "Bianco", "Grigio"]

pwchange = {}


inputuser = input("Digitare un username valido: ")
print(secret_animal.get(inputuser))

while inputuser not in credentials.keys():
    print("Username non valido")
    inputuser = input("Digitare la password corretta per l'utente " + inputuser + " : ")


inputpw = input("Digitare la password: ")
errorcounter = 0

while inputpw != credentials.get(inputuser):
    if errorcounter == 5:
        randompw = randomword(6)
        credentials.update({inputuser : randompw})
        pwchange.update({inputuser : True})
        print("password reset avvenuto, prego rispondere alla domanda segreta per ottenere la password: ")
        break

    errorcounter += 1
    print(errorcounter)
    print("Password non valida, errore numero: " + str(errorcounter) + " dopo 5 login errati si resetterà la password")
    inputpw = input("Digitare la password corretta per l'utente " + inputuser + " : ")

if inputpw == credentials.get(inputuser):
    print("Password accettata, Benvenuto utente: " + inputuser )


if inputuser in pwchange.keys():
    print("Rilevato reset della password effettuato, prego rispondere alla domanda segreta: ")
    inputchoice = input("Scegli tra Animale o Colore: ")
    if inputchoice == "Animale":
        inputchoice == input("Qual'è il tuo animale preferito tra i seguenti: " + str(expander(animal_list)))
        if str(inputchoice) == str(secret_animal.get(inputuser)):
            print("Account recuperato, la nuova password è: " + randompw)
        else:
            print("Account bloccato, contattare un amministratore")

    elif inputchoice == "Colore":
        inputchoice == input("Qual'è il tuo colore preferito tra i seguenti: " + expander(color_list))
        if str(inputchoice) == str(secret_color.get(inputuser)):
            print("Account recuperato, la nuova password è: " + randompw)
        else:
            print("Account bloccato, contattare un amministratore")
            
    else:
        inputchoice = input("Scegli tra Animale o Colore")


##L'ultima sezione non funziona per via di 70 e 77 non mi funziona
        
