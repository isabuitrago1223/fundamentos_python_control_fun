# Usando while
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# Equivalente con for
suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")