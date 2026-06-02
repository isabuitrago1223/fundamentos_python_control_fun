def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

pares = crear_lista_pares(10)
print(pares)  # Imprime: [2, 4, 6, 8, 10]

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
print(cuadrados)  # Imprime: {1: 1, 2: 4, 3: 9, 4: 16}