def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    # Aplicar mayúsculas si se solicita
    if mayusculas:
        texto = texto.upper()

    # Dividir el texto en palabras
    palabras = texto.split()

    # Aplicar prefijo y sufijo a cada palabra
    palabras_formateadas = [f"{prefijo}{palabra}{sufijo}" for palabra in palabras]

    # Unir las palabras con el separador especificado
    resultado = separador.join(palabras_formateadas)

    return resultado

# Ejemplos de uso
texto_original = "python es un lenguaje versátil"

# Uso básico sin modificaciones
print(formatear_texto(texto_original))
# Imprime: python es un lenguaje versátil

# Convertir a mayúsculas
print(formatear_texto(texto_original, mayusculas=True))
# Imprime: PYTHON ES UN LENGUAJE VERSÁTIL

# Añadir prefijo y sufijo
print(formatear_texto(texto_original, prefijo="«", sufijo="»"))
# Imprime: «python» «es» «un» «lenguaje» «versátil»

# Cambiar el separador
print(formatear_texto(texto_original, separador="-"))
# Imprime: python-es-un-lenguaje-versátil

# Combinación de opciones
print(formatear_texto(
    texto_original,
    mayusculas=True,
    prefijo="#",
    sufijo="!",
    separador="..."
))
# Imprime: #PYTHON!...#ES!...#UN!...#LENGUAJE!...#VERSÁTIL!