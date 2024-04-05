class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Año: {self.año}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        print(f"Productos del año {año}:")
        for producto in self.productos:
            if producto.año == año:
                print(producto)


if __name__ == "__main__":
    catalogo = Catalogo()

    # Agregar productos al catálogo
    catalogo.agregar_producto(Producto("Llantas", 100, 2022))
    catalogo.agregar_producto(Producto("Frenos", 150, 2023))
    catalogo.agregar_producto(Producto("Batería", 200, 2022))
    catalogo.agregar_producto(Producto("Aceite", 50, 2024))

    # Mostrar todos los productos en el catálogo
    catalogo.mostrar_productos()

    # Filtrar productos por año
    catalogo.filtrar_por_año(2024)
