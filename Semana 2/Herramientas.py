#Técnicas de Programación

#Tecnica de abstracion
from abc import ABC, abstractmethod


# Clase abstracta
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


# Implementaciones concretas
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2


class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto


# Uso
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Área del rectángulo: {rectangulo.calcular_area()}")

"________________________________________________________________"

#Tecnica Encapsulamiento

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        return self.__saldo


# Uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
print(f"Saldo disponible: {cuenta.consultar_saldo()}")

"_________________________________________________________________"

#Tecnica Herencia

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"


# Uso
perro = Perro("Fido")
gato = Gato("Whiskers")
print(perro.hacer_sonido())
print(gato.hacer_sonido())

"________________________________________________________"

#Tecnica Polimorfismo

class Ave:
    def volar(self):
        return "Esta ave vuela."

class Aguila(Ave):
    def volar(self):
        return "El águila vuela alto."

class Pinguino(Ave):
    def volar(self):
        return "El pingüino no puede volar, pero nada."

# Uso polimórfico
aves = [Aguila(), Pinguino()]

for ave in aves:
    print(ave.volar())
