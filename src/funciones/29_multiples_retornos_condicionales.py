def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"

    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"

    return "Insuficiente"