## scrivi riconoscitore di palindromo


## rubato da https://stackoverflow.com/questions/5843518/remove-all-special-characters-punctuation-and-spaces-from-string
##  ''.join(e for e in string if e.isalnum())
# filtra per soli caratteri alfanumerici


# questa versione toglie anche gli spazi oltre che i caratteri non alfanumerici
def clean(string):
    string = ''.join(lettera for lettera in string if lettera.isalnum())
    string = string.lower()
    print(string)
    return string


input1 = input("dammi una frase o parola palindroma e ti dirò se lo è! ")
parola = input1

input1 = clean(input1)

palindromo = False

if len(input1) % 2 == 0:
    print("frase pari")
    print( input1[0 : len(input1)//2] )
    print( input1[len(input1) : len(input1)//2 : -1])
    palindromo = input1[0 : len(input1)//2] == input1[ len(input1) : len(input1)//2 : -1]
else:
    print("frase dispari")
    print( input1[0 : len(input1)//2] )
    print( input1[ len(input1) : len(input1)//2   : -1] )
    palindromo = input1[0 : len(input1)//2] == input1[ len(input1) : len(input1)//2  : -1]


if palindromo:
    print("La parola/frase " + parola + " è palindroma")
else:
    print("La parola/frase " + parola + " NON è palindroma")

