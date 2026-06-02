def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"# Diferentes formas de llamar a la función
pago1 = calcular_pago(40)  # 40 horas, tarifa predeterminada, moneda predeterminada
pago2 = calcular_pago(35, 20)  # 35 horas, tarifa de 20, moneda predeterminada
pago3 = calcular_pago(30, moneda="USD")  # 30 horas, tarifa predeterminada, moneda USD
pago4 = calcular_pago(horas=25, tarifa=18, moneda="GBP")  # Todo especificado por nombre

print(pago1)  # Imprime: 600 EUR
print(pago2)  # Imprime: 700 EUR
print(pago3)  # Imprime: 450 USD
print(pago4)  # Imprime: 450 GBP