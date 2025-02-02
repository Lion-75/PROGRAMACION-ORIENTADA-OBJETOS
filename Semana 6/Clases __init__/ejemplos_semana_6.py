# Programa para demostrar Herencia, Encapsulación y Polimorfismo en Python

# Clase base (Padre)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad  # Atributo privado (encapsulado)

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."

    # Método para acceder al atributo encapsulado
    def obtener_edad(self):
        return self.__edad

    # Método para modificar el atributo encapsulado
    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")

# Clase derivada (Hijo)
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.grado = grado  # Atributo adicional

    # Sobrescribir el metodo saludar (Polimorfismo)
    def saludar(self):
        return f"Hola, soy {self.nombre} y estoy en el grado {self.grado}."

# Clase adicional para demostrar polimorfismo con múltiples argumentos
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    # Sobrescribir el metodo saludar (Polimorfismo)
    def saludar(self):
        return f"Hola, soy el profesor {self.nombre} y enseño {self.asignatura}."

# Creación de instancias y demostración del programa
if __name__ == "__main__":
    # Crear una instancia de Persona
    persona = Persona("Carlos", 40)
    print(persona.saludar())
    print(f"Edad: {persona.obtener_edad()}")

    # Encapsulación: Modificar la edad
    persona.establecer_edad(45)
    print(f"Nueva Edad: {persona.obtener_edad()}")

    # Crear una instancia de Estudiante
    estudiante = Estudiante("Ana", 16, "10mo")
    print(estudiante.saludar())  # Demostración de polimorfismo

    # Crear una instancia de Profesor
    profesor = Profesor("María", 35, "Matemáticas")
    print(profesor.saludar())  # Demostración de polimorfismo