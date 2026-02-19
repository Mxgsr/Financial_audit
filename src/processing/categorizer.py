REGLAS_CATEGORIZACION = {
    "Alimentación": ["supermercado", "restaurante", "comida", "cena"],
    "Transporte": ["taxi", "uber", "gasolina", "transporte"],
    "Ocio": ["cine", "concierto", "libro", "juego"],
    "Hogar": ["arriendo", "luz", "agua", "internet"]
}

def categorizar_transaccion(descripcion):
    """
    Dada la descripción de una transacción, devuelve la categoría correspondiente.
    """
    descripcion = descripcion.lower()
    for categoria, palabras_clave in REGLAS_CATEGORIZACION.items():
        for palabra_clave in palabras_clave:
            if palabra_clave in descripcion:
                return categoria

    return "Categoría Desconocida"


# Bloque de prueba para verificar que nuestra función hace lo que esperamos.
if __name__ == "__main__":
    descripcion_prueba = "Compra en supermercado Lider"
    categoria_resultado = categorizar_transaccion(descripcion_prueba)

    print(f"La descripción: '{descripcion_prueba}'")
    print(f"Ha sido clasificada como: '{categoria_resultado}'")

    descripcion_prueba_2 = "Carga de combustible en Copec"
    categoria_resultado_2 = categorizar_transaccion(descripcion_prueba_2)
    print(f"La descripción: '{descripcion_prueba_2}'")
    print(f"Ha sido clasificada como: '{categoria_resultado_2}'")
