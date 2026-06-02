def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Podemos pasar cualquier cantidad de argumentos
print(sumar(1, 2))  # Imprime: 3
print(sumar(1, 2, 3, 4, 5))  # Imprime: 15
print(sumar())  # Imprime: 0