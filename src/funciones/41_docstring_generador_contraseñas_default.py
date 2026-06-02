def generar_contraseña(longitud=8):
    """
    Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))