# Clase Libro que representa un libro de la biblioteca
class Libro:
    def __init__(self, titulo, autor, disponible=True):
        """
        Constructor de la clase Libro.
        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param disponible: Indica si el libro está disponible para préstamo.
        """
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self):
        """
        Marca el libro como prestado si está disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        """
        Marca el libro como disponible.
        """
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def __str__(self):
        """
        Devuelve una representación en cadena del libro.
        """
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' de {self.autor} ({estado})"


# Clase Biblioteca que gestiona los libros
class Biblioteca:
    def __init__(self, nombre):
        """
        Constructor de la clase Biblioteca.
        :param nombre: Nombre de la biblioteca.
        """
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la biblioteca.
        :param libro: Objeto de tipo Libro.
        """
        self.libros.append(libro)
        print(f"Se ha agregado el libro '{libro.titulo}'.")

    def mostrar_libros(self):
        """
        Muestra todos los libros de la biblioteca.
        """
        print(f"Libros en la biblioteca '{self.nombre}':")
        for libro in self.libros:
            print(libro)

# Ejecución del programa
if __name__ == "__main__":
    # Crear una biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Universitaria")

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry")

    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)

    # Mostrar los libros disponibles
    mi_biblioteca.mostrar_libros()

    # Prestar un libro
    libro1.prestar()

    # Mostrar los libros después del préstamo
    mi_biblioteca.mostrar_libros()

    # Devolver el libro prestado
    libro1.devolver()

    # Mostrar los libros después de la devolución
    mi_biblioteca.mostrar_libros()
