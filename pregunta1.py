def solicitar_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y (donde X e Y son enteros): ")
            numerador, denominador = map(int, fraccion.split('/'))
            if denominador == 0 or '.' in fraccion:
                raise ValueError
            if numerador > denominador:
                print("El numerador debe ser menor o igual al denominador.")
                continue
            return numerador, denominador
        except ValueError:
            print("Formato incorrecto o fracción inválida. Por favor, ingrese nuevamente.")

def calcular_porcentaje(numerador, denominador):
    porcentaje = (numerador / denominador) * 100
    porcentaje_redondeado = round(porcentaje)
    if porcentaje_redondeado < 1:
        return 'E'
    elif porcentaje_redondeado > 99:
        return 'F'
    else:
        return str(porcentaje_redondeado) + '%'

if __name__ == '__main__':
    while True:
        try:
            numerador, denominador = solicitar_fraccion()
            resultado = calcular_porcentaje(numerador, denominador)
            print("Cantidad de combustible en el tanque:", resultado)
            break
        except ZeroDivisionError:
            print("El denominador no puede ser cero. Por favor, ingrese nuevamente.")
