
##usa decoratore per ripetere le seguenti funzioni salvando i valori in una lista


rettangoli = []
triangoli = []
quadrati = []


def triangle_decorator(area_triangolo):
    def tri_dec(*args, **kwargs):
        argument1, argument2 = kwargs
        print("stop per chiamare la funzione area_triangolo su " + str(argument1) + " e " + str(argument2))

        triangoli.append(area_triangolo(argument1, argument2))

        print("ho chiamato la funzione, ha aggiunto a triangoli il valore: " + str(rettangoli[-1]) )

        return triangoli[-1]
    return tri_dec


def area_rettangolo(base, altezza):
    return base * altezza

@triangle_decorator
def area_triangolo():
    return prendidati()

def area_quadrato(lato):
    return area_rettangolo(lato, lato)

def inizio():
    pass

def prendidati(base, altezza):
    base = input("dammi base)")
    altezza = input("dammi altezza")
    return base, altezza

