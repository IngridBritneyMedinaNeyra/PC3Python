# Archivo operaciones.py
def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        else:
            return a / b
    except TypeError:
        return "Error: Tipo de dato no válido."
        

# Archivo calculos.py
import operaciones

def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        print("Suma:", operaciones.suma(num1, num2))
        print("Resta:", operaciones.resta(num1, num2))
        print("Producto:", operaciones.producto(num1, num2))
        print("División:", operaciones.division(num1, num2))
    except ValueError:
        print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()
