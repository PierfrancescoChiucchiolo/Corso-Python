
import math

class punto:

    def __init__(self, x = 0, y = 0):
        self.xcoord = x
        self.ycoord = y

    def muovi(self, dx, dy):
        self.xcoord += dx
        self.ycoord += dy

    def distanza(self, punto):
        xdist = self.xcoord - punto.xcoord
        ydist = self.ycoord - punto.ycoord
        dist = math.sqrt( xdist * xdist + ydist * ydist )
        return dist
    
    def print_me(self):
        print(" Le mie coordinate sono: " + str(self.xcoord) + "," + str(self.ycoord))


punto1 = punto(5, 2)
punto1.print_me()
punto2 = punto(4, 7)
punto1.muovi(1, 1)
punto1.print_me()
punto2.print_me()

print( str(punto1.distanza(punto2)) )