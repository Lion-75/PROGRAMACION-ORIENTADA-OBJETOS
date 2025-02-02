import os
import json

class Producto:
    """Clase que representa un producto en el inventario."""
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte el objeto Producto a un diccionario para facilitar el almacenamiento en archivos."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class Inventario:
    """Clase que gestiona el inventario y maneja la persistencia en archivos."""
    ARCHIVO = "inventario.txt"

    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo al iniciar el programa."""
        if not os.path.exists(self.ARCHIVO):
            return
        try:
            with open(self.ARCHIVO, "r") as file:
                self.productos = [Producto(**json.loads(line)) for line in file]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: El archivo de inventario está corrupto o no se puede leer.")

    def guardar_en_archivo(self):
        """Guarda los productos en un archivo después de cada modificación."""
        try:
            with open(self.ARCHIVO, "w") as file:
                for producto in self.productos:
                    file.write(json.dumps(producto.to_dict()) + "\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un producto nuevo al inventario si el ID es único."""
        if any(p.id_producto == id_producto for p in self.productos):
            print("Error: Ya existe un producto con este ID.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print(f"Producto '{nombre}' agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print(f"Producto con ID {id_producto} eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o precio de un producto por su ID."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                self.guardar_en_archivo()
                print(f"Producto con ID {id_producto} actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre (puede haber coincidencias parciales)."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: ${p.precio:.2f}")
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(f"ID: {p.id_producto}, Nombre: {p.nombre}, Cantidad: {p.cantidad}, Precio: ${p.precio:.2f}")

def menu():
    """Interfaz de usuario en la consola."""
    inventario = Inventario()
    while True:
        print("\n📦 MENÚ DE INVENTARIO 📦")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto,
                                           cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
