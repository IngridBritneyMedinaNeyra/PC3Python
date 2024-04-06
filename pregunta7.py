import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 and self.y > 0:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        elif self.x > 0 and self.y < 0:
            return "Cuadrante IV"
        elif self.x == 0 and self.y != 0:
            return "Sobre eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre eje X"
        else:
            return "Origen"
    
    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    
    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        print(f"La distancia entre {self} y {otro_punto} es {distancia}")

class Rectangulo:
    def __init__(self, punto_ini=Punto(), punto_fin=Punto()):
        self.punto_ini = punto_ini
        self.punto_fin = punto_fin
    
    def base(self):
        return abs(self.punto_fin.x - self.punto_ini.x)
    
    def altura(self):
        return abs(self.punto_fin.y - self.punto_ini.y)
    
    def area(self):
        return self.base() * self.altura()

# Solicitar entrada al usuario
x1 = float(input("Ingrese la coordenada X del Punto 1: "))
y1 = float(input("Ingrese la coordenada Y del Punto 1: "))
x2 = float(input("Ingrese la coordenada X del Punto 2: "))
y2 = float(input("Ingrese la coordenada Y del Punto 2: "))

# Crear los objetos Punto
punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)

# Ejemplos de uso
print("\nPunto 1:", punto1)
print("Cuadrante de Punto 1:", punto1.cuadrante())
print("Vector entre Punto 1 y Punto 2:", punto1.vector(punto2))
punto1.distancia(punto2)

rectangulo = Rectangulo(punto1, punto2)
print("\nBase del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())
