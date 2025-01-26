# Programa que demuestra el uso de constructores (__init__) y destructores (__del__)

class ArchivoTemporal:
    """
    Clase que simula la creación y eliminación de un archivo temporal.
    Utiliza el constructor para inicializar el nombre del archivo y el destructor para simular su eliminación.
    """

    def __init__(self, nombre):
        """
        Constructor que inicializa el objeto ArchivoTemporal.
        Crea un archivo simulado con el nombre proporcionado.
        """
        self.nombre = nombre
        print(f"Archivo '{self.nombre}' creado.")

    def __del__(self):
        """
        Destructor que se llama cuando el objeto es eliminado o el programa finaliza.
        Simula la eliminación del archivo temporal.
        """
        print(f"Archivo '{self.nombre}' eliminado.")

# Clase adicional para demostrar el uso de varios objetos
class Sesion:
    """
    Clase que simula una sesión de usuario en un sistema.
    """

    def __init__(self, usuario):
        """
        Constructor que inicializa la sesión con el nombre de usuario.
        """
        self.usuario = usuario
        print(f"Sesión iniciada para el usuario: {self.usuario}")

    def __del__(self):
        """
        Destructor que finaliza la sesión y libera los recursos.
        """
        print(f"Sesión finalizada para el usuario: {self.usuario}")

# Ejemplo de uso
def main():
    print("\n--- Inicio del programa ---")

    # Crear un archivo temporal
    archivo = ArchivoTemporal("temp.txt")

    # Crear una sesión de usuario
    sesion = Sesion("Juan Perez")

    print("Realizando algunas operaciones...\n")

    # Eliminar referencias manualmente para invocar los destructores
    del archivo
    del sesion

    print("\n--- Fin del programa ---")

# Llamar a la función principal
if __name__ == "__main__":
    main()
