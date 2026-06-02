def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Más fácil de leer con argumentos por nombre
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)