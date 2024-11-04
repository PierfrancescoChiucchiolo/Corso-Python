## dichiaro una lista e la inizializzo
lista = ["Ciao", "Arrivederci", "Ciaone", "ciao", "Buongiorno"]

print("il numero di volte che l'elemento 'ciao' è presente nella lista è " + str( lista.count("ciao") ))

print("rendo ogni elemento nella lista minuscolo")
for i in range(len(lista)):
    lista[i] = lista[i].lower()

print("ordiniamo gli elementi")
lista.sort()

print("il numero di volte che l'elemento 'ciao' è presente nella lista è " + str( lista.count("ciao") ))

print("printo ogni elemento")
for elemento in lista:
    print(elemento)

## per convenzione dovrei inserire questa funzione in cima, tenendo distinte funzioni e codice, ma pazienza
def my_count(my_list, target):
    counter = 0
    for my_element in my_list:
        if my_element == target:
            counter = counter + 1
    return counter

print("il numero di volte che l'elemento 'ciao' è presente nella lista è " + str( my_count(lista, "ciao") ))



print("AYO IT'S WORKING")




