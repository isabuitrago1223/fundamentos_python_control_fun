def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []

    # Verificar campos requeridos
    for campo in campos_requeridos:
        if campo not in datos:
            errores.append(f"Falta el campo requerido: {campo}")
            break
        elif not datos[campo]:  # Campo vacío
            errores.append(f"El campo {campo} no puede estar vacío")
            break
    else:
        # Solo llegamos aquí si todos los campos requeridos existen y no están vacíos
        # Ahora validamos el formato de cada campo

        # Validar email
        if "@" not in datos["email"]:
            errores.append("Email inválido")

        # Validar edad
        try:
            edad = int(datos["edad"])
            if edad < 18 or edad > 120:
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")

    # Validaciones opcionales
    if "telefono" in datos:
        if not datos["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Explícitamente indicamos que es opcional

    # Resultado final
    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True}

# Probamos con diferentes formularios
formulario1 = {
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",  # Falta @
    "edad": "17"  # Menor de edad
}

print(validar_formulario(formulario1))
print(validar_formulario(formulario2))