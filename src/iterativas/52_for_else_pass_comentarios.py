# Versión más explícita con comentarios
for item in coleccion:
    if condicion(item):
        # Procesamiento normal
        procesar(item)
    else:
        pass  # Intencionalmente no hacemos nada con estos elementos
else:
    # Este bloque se ejecuta si el bucle termina normalmente (sin break)
    print("Procesamiento completado sin interrupciones")