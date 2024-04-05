class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.num_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", self.notas)

    def set_edad(self, edad):
        self.edad = edad

    def set_notas(self, notas):
        self.notas = notas

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumno: ")
    num_registro = input("Ingrese el número de registro del alumno: ")
    
    alumno = Alumno(nombre, num_registro)
    
    alumno.set_edad(input("Ingrese la edad del alumno: "))
    notas = input("Ingrese las notas del alumno separadas por comas: ").split(',')
    alumno.set_notas(notas)
    
    alumno.display()
