def estadisticas(datos):
    """Calcula la suma, el promedio, el mínimo y el máximo de una lista de números."""
    suma = sum(datos)
    promedio = suma / len(datos) if datos else 0
    minimo = min(datos)
    maximo = max(datos)
    return suma, promedio, minimo, maximo

datos = [10, 20, 30, 42, 4, 2]  # Ejemplo de datos para que la suma sea 108 y el promedio 18.0

# Guardamos el retorno en la variable 'resultado'
resultado = estadisticas(datos)

print(type(resultado))  # Imprime: <class 'tuple'>
print(resultado)        # Imprime: (108, 18.0, 4, 42)
print(resultado[1])     # Imprime: 18.0 (accediendo al promedio)