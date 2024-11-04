'''


pierfrancesco, quasi 29 anni, laureato in informatica triennale in sapienza
Python, Java, Assembler, C++, SQL/MySQL/PL-SQL, HTML, CSS
conosco poco il machine learning, ma ho frequentato un corso di AI all'università, esame che ho poi sostituito dal mio corso di studi
si trattava principalmente di modellazione e CSP
constraints satisfaction problems

docente: Tommaso Muraca / corsi.online.muraca@gmail.com


f stringa
print(f "io ho " {29} " anni")
oppure metti le virgole "io ho ", 29, " anni"
string escape: "\


while(espressione booleana):
    todo
else:
    POSSO INSERIRE ELSE QUI

slicing di liste
lista[1:5] da 1 a 5
lista[:-1] togli ultimo
lista[::-1] reverse con step -1


set = {1, 2, 3, "stella"}


'''


eta = input("quanti anni hai? ")
patente = input("hai la patente? si o no? ")
tasso_alcool = input("tasso alcolemico alto o basso? ")

if eta < 18:
    print("non sei maggiorenne, non puoi guidare")
elif patente != "si":
    print("non hai la patente, non puoi guidare")
elif tasso_alcool == "alto":
    print("sei ubriaco, non puoi guidare")
else:
    print("puoi guidare")
