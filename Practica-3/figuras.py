from math import pi
from punto import Punto

class Figura:
    def __init__(self, punto1, punto2):
        self.origen = punto1
        self.fin = punto2
        self.area = 0
        self.perimetro = 0
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def informar_propiedades(self):
        print("Tipo de figura es: ", str(type(self)).split(".")[1][:-2])
        print("El area es: ", self.area)
        print("El perimetro es: ", self.perimetro)
        
class Cuadrado(Figura):
    def calcular_area(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.area = lado * lado
    def calcular_perimetro(self):
        lado = self.origen.calcular_distancia(self.fin)
        self.perimetro = 4 * lado
        
class rectangulo(Figura):
    def calcular_area(self):
        base = self.calcular_distancia(Punto.fin.x, Punto.origen.y)
        altura = self.calcular_distancia(Punto.origen.x, Punto.fin.y)
        self.area = base * altura
    def calcular_perimetro(self):
        base = self.calcular_distancia(Punto.fin.x, Punto.origen.y)
        altura = self.calcular_distancia(Punto.origen.x, Punto.fin.y)
        self.perimetro = 2 * (base + altura)
        