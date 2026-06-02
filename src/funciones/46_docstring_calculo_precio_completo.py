def calcular_precio_final(precio_base, descuento=0, impuesto=0.21):
    """
    Calcula el precio final de un producto aplicando descuento e impuesto.

    Primero aplica el descuento sobre el precio base y luego
    añade el impuesto sobre el precio con descuento.

    Args:
        precio_base (float): Precio original del producto
        descuento (float, opcional): Porcentaje de descuento (0-100). Predeterminado: 0
        impuesto (float, opcional): Tasa de impuesto (0-1). Predeterminado: 0.21

    Returns:
        float: Precio final después de aplicar descuento e impuesto

    Raises:
        ValueError: Si alguno de los parámetros tiene un valor negativo

    Ejemplos:
        >>> calcular_precio_final(100)
        121.0
        >>> calcular_precio_final(100, 10)
        108.9
        >>> calcular_precio_final(100, 10, 0.1)
        99.0
    """
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")

    precio_con_descuento = precio_base * (1 - descuento/100)
    precio_final = precio_con_descuento * (1 + impuesto)

    return precio_final