# Programación Tradicional
# Ejemplo: Temperaturas Diarias

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingresa la temperatura diaria de la semana:")
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        temp = float(input(f"{dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()


print("_____________________________________________________________________")
print("Programación Orientada a Objetos")

class Clima:
    def __init__(self):
        self.temperaturas = []  # Atributo privado para almacenar temperaturas

    # Método para ingresar temperaturas diarias
    def ingresar_temperaturas(self):
        print("Ingresa la temperatura diaria de la semana:")
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
            temp = float(input(f"{dia}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = Clima()  # Crear instancia de la clase Clima
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()