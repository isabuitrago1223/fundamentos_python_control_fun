def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")        # Imprime: Suma: 108
print(f"Promedio: {media}")   # Imprime: Promedio: 18.0
print(f"Mínimo: {menor}")     # Imprime: Mínimo: 4
print(f"Máximo: {mayor}")     # Imprime: Máximo: 42