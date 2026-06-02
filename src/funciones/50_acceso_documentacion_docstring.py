def calcular_promedio(numeros):
    """
    Calcula el promedio aritmético de una lista de números.

    Args:
        numeros (list): Una lista de números enteros o flotantes.

    Returns:
        float: El promedio de los números, o 0.0 si la lista está vacía.
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

# Acceder al docstring directamente
print(calcular_promedio.__doc__)

# O usar la función help
help(calcular_promedio)