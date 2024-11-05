'''
crea tramite punto grafico cartesiano
'''

import math

class Punto():

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        self.x += dx
        self.y += dy

    def distanza(self, punto):
        distanza = math.sqrt( ((self.x - punto.x) * (self.x - punto.x)) + ((self.y - punto.y) * (self.y - punto.y)) )
        return distanza

class Cartesiano():

    def __init__(self, punto1, punto2, punto3):
        self.punti = [punto1, punto2, punto3]
        self.matrice = []

    def lista_punti(self):
        return self.punti

    def aggiungi(self, punto):
        self.punti.append(punto)

    def is_valid(self):
        return len(self.punti) >= 3

    def genera_matrice(self):
        min_x = 0
        max_x = 0
        min_y = 0
        max_y = 0
        print(str(min_x), str(max_x), str(min_y), str(max_y))

        for punto in self.punti:
            if self.is_valid():
                if punto.x < min_x : min_x = punto.x
                elif punto.x > max_x : max_x = punto.x
                elif punto.y < min_y : min_y = punto.y
                elif punto.y > max_y : max_y = punto.y

        print(str(min_x), str(max_x), str(min_y), str(max_y))
        righe = max_x - min_x
        colonne = max_y - min_y
        matrice = []

        for i in range(0, colonne +1, 1):
            lista = []
            for j in range(0, righe +1, 1):
                lista.append(0)
            matrice.append(lista)
        
        for punto in self.lista_punti():
            matrice[punto.y][punto.x] = 1
    
    def illustra(self):
        for i in range(0, len(self.matrice)):
            print(self.matrice[i])


origine = Punto()
punto1 = Punto(1, 2)
punto2 = Punto(4, 3)
punto3 = Punto(3, 3)

print(punto1.distanza(origine))
print(punto1.distanza(punto1))
print(punto1.distanza(punto2))


piano1 = Cartesiano(punto1, punto2, punto3)
## print(piano1.lista_punti())

piano1.genera_matrice()
piano1.illustra()