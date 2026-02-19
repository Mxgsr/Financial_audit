# Este diccionario contendrá nuestras reglas de clasificación.
# La "clave" es el nombre de la categoría (ej: "Alimentación").
# El "valor" es una lista de palabras clave que buscaremos en las descripciones.
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
    # Pista 1: Convierte la descripción a minúsculas para que la búsqueda
    # de palabras clave no distinga entre "Supermercado" y "supermercado".
    # Un string tiene un método útil para esto.
    descripcion = descripcion.lower()

    # Pista 2: Necesitamos recorrer nuestro diccionario de reglas.
    # Un bucle "for" que itere sobre los items de REGLAS_CATEGORIZACION
    # te dará la categoría y su lista de palabras clave en cada pasada.
    # Por ejemplo: for categoria, palabras_clave in REGLAS_CATEGORIZACION.items():
    for categoria, palabras_clave in REGLAS_CATEGORIZACION.items():
        # Pista 3: Dentro del primer bucle, necesitas otro bucle "for"
        # para recorrer cada "palabra_clave" en la lista "palabras_clave".
        for palabra_clave in palabras_clave:

            # Pista 4: Dentro del segundo bucle, comprueba si la "palabra_clave"
            # se encuentra dentro de la descripción (ya en minúsculas).
            # Python tiene un operador muy simple para ver si un texto contiene a otro. (if ... in ...)

                # Pista 5: Si encuentras una coincidencia, ¡genial!
                # Has encontrado la categoría. Usa "return" para devolver
                # el nombre de la "categoria" actual y terminar la función.
            if palabra_clave in descripcion:
                return categoria


    # Pista 6: Si el bucle termina y no se encontró ninguna categoría,
    # debemos devolver un valor por defecto.
    # Retorna el texto "Categoría Desconocida".
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
