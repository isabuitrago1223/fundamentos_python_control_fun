def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Asignar una función a una variable
convertir = celsius_a_fahrenheit
temperatura_f = convertir(25)  # Equivalente a celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_f}°F")  # Imprime: 25°C equivalen a 77.0°F