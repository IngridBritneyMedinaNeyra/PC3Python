def obtener_calificaciones():
    while True:
        calificaciones = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones_lista = calificaciones.split(',')
        try:
            calificaciones_enteros = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            return calificaciones_enteros
        except ValueError:
            print("Error: Las calificaciones deben ser números enteros. Inténtelo de nuevo.")

if __name__ == '__main__':
    lista_calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", lista_calificaciones)
