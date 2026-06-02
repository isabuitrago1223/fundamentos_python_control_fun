numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    # Ignoramos múltiplos de 3
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    # Sumamos el número
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    # Si la suma supera el límite, terminamos
    if suma > limite:
        print(f"Límite de {limite} superado")
        break