from math import sqrt
class Punto: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def informar(self):
        print("x = ", self.x, "y = ", self.y)
    def calcular_distancia(self, punto):
        return sqrt(((self.x- punto.x) ** 2)+((self.y - punto.y) **2))

if __name__ == "__main__":
    p1 = Punto(0,0)
    p2 = Punto(5,5)

    p1.informar()
    p2.informar()

    print(p1.calcular_distancia(p2))