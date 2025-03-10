class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)  # Tupla para título y autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} de {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {[libro.info[0] for libro in self.libros_prestados]}"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave
        self.usuarios = {}  # Diccionario con ID de usuario como clave
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.usuarios[usuario.user_id] = usuario
            self.ids_usuarios.add(usuario.user_id)
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            self.ids_usuarios.remove(user_id)
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro en préstamo.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}: {[libro.info[0] for libro in usuario.libros_prestados]}")
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "123456789")
libro2 = Libro("1984", "George Orwell", "Distopía", "987654321")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "U001")
biblioteca.registrar_usuario(usuario1)

# Prestar un libro
biblioteca.prestar_libro("U001", "123456789")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")

# Devolver un libro
biblioteca.devolver_libro("U001", "123456789")

# Buscar libro por categoría
biblioteca.buscar_libro("categoria", "Novela")
