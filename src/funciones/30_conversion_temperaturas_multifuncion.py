def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre diferentes unidades.

    Args:
        valor: El valor de la temperatura a convertir
        origen: Unidad de origen ('C', 'F' o 'K')
        destino: Unidad de destino ('C', 'F' o 'K')

    Returns:
        float: La temperatura convertida, o None si los parámetros son inválidos
    """
    # Validación de parámetros
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    # Si origen y destino son iguales, no hay conversión necesaria
    if origen == destino:
        return valor

    # Primero convertimos a Celsius como unidad intermedia
    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:  # origen es 'C'
        celsius = valor

    # Luego convertimos de Celsius a la unidad de destino
    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:  # destino es 'C'
        return celsius

# Ejemplos de uso
print(convertir_temperatura(25, 'C', 'F'))    # Imprime: 77.0
print(convertir_temperatura(98.6, 'F', 'C'))  # Imprime: 37.0
print(convertir_temperatura(0, 'C', 'K'))     # Imprime: 273.15
print(convertir_temperatura(20, 'X', 'Y'))    # Imprime: None