def dividir_seguro(a, b):
    """
    Realiza una división segura entre dos números.

    Args:
        a: El numerador
        b: El denominador

    Returns:
        El resultado de la división a/b, o None si b es cero

    Ejemplo:
        >>> dividir_seguro(10, 2)
        5.0
        >>> dividir_seguro(10, 0)
        None
    """
    if b == 0:
        return None
    return a / b