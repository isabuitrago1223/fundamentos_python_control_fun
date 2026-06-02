def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]
