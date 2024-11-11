'''

15min per gruppo: pier carlo / roberta / simone

Create un file.txt con uno script python e testo preso da https://it.lipsum.com/ , dopo
averlo fatto scrivete un programma che legge il documento e ci restituisce il numero di parole, righe e caratteri.


## paragrafi 5 / 440 parole


'''

file = open("lorem_ipsum.txt", "r", encoding = "utf-8")

testo = file.readlines()
print("numero di righe = " + str(len(testo)) )


parole = []
for riga in testo:
    parole_riga = riga.split(" ")
    for parola in parole_riga:
        parola.replace("\n", "")
        parole.append(parola)


print("numero di parole = " + str(len(parole)) )

counter = 0
for parola in parole:
    counter += len(parola)

print("numero di caratteri = " + str(counter))
file.close()
