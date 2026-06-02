def filtrar_pares(lista):
    """Filtra los números pares de una lista."""
    return [num for num in lista if num % 2 == 0]

# Pasando el argumento de forma posicional (directamente la lista)
numeros_ejemplo = [1, 2, 3, 4, 5, 6]
resultado = filtrar_pares(numeros_ejemplo)

print(resultado)  # Imprime: [2, 4, 6]
