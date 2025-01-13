"""
Este programa calcula el área de un círculo dado su radio.
También verifica si el área es mayor que un valor de referencia.
"""

# Importamos el módulo math para usar el valor de PI
import math


# Función que calcula el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float o int)
    :return: Área del círculo (float)
    """
    area = math.pi * radio ** 2
    return area


# Función principal del programa
def main():
    """
    Solicita al usuario el radio del círculo, calcula el área
    y verifica si es mayor que un valor de referencia.
    """
    # Entrada: solicitamos el radio del círculo al usuario
    radio = float(input("Ingresa el radio del círculo: "))

    # Proceso: calculamos el área usando la función
    area_circulo = calcular_area_circulo(radio)

    # Mostramos el resultado del área
    print(f"El área del círculo con radio {radio} es: {area_circulo:.2f}")

    # Comparamos el área con un valor de referencia (por ejemplo, 50.0)
    valor_referencia = 50.0
    es_area_grande = area_circulo > valor_referencia  # Booleano que indica si el área es grande

    # Salida: mostramos si el área es mayor al valor de referencia
    if es_area_grande:
        print("El área es mayor que el valor de referencia.")
    else:
        print("El área es menor o igual al valor de referencia.")


# Llamada a la función principal
if __name__ == "__main__":
    main()
