import math

def calcular_area_circulo():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        area = math.pi * (radio ** 2)
        print("El área del círculo es:", area)
    except ValueError:
        print("Error: Ingrese un número válido para el radio.")

def calcular_area_rectangulo():
    try:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print("El área del rectángulo es:", area)
    except ValueError:
        print("Error: Ingrese un número válido para la base o la altura.")

def calcular_area_cuadrado():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = lado ** 2
        print("El área del cuadrado es:", area)
    except ValueError:
        print("Error: Ingrese un número válido para el lado.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            calcular_area_circulo()
        elif opcion == "2":
            calcular_area_rectangulo()
        elif opcion == "3":
            calcular_area_cuadrado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
