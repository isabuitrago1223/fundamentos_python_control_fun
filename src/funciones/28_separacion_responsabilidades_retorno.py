# Mejor: separar la obtención del resultado de su presentación
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Uso
notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")  # La impresión se hace fuera de la función