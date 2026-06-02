def dividir_seguro(a, b):
    # Verificación de seguridad
    if b == 0:
        print("Error: División por cero")
        return None  # Salida anticipada

    # Este código solo se ejecuta si b no es cero
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   # Imprime: 5.0
print(dividir_seguro(10, 0))   # Imprime: Error: División por cero y luego None