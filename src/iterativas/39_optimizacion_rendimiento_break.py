# Definimos variables de prueba para que no marquen error
lista_grande = [1, 2, 3, 4, 5]
objetivo = 3

# Versión ineficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
# Seguimos recorriendo toda la lista aunque ya encontramos el objetivo

# Versión eficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
        break  # Terminamos inmediatamente