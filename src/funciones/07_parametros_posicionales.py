def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)  # 100 va a precio_base, 0.21 va a impuesto
print(f"Precio final: {total}")  # Imprime: Precio final: 121.0