from src.ingestion.file_reader import leer_transacciones_csv
from src.processing.categorizer import categorizar_transaccion



def main():
    """
    Función principal que orquesta la aplicación.
    """
    ruta_archivo_transacciones = "data/raw/sample_transactions.csv"
    print(f"Iniciando el proceso de auditoría para el archivo: {ruta_archivo_transacciones}")

    transacciones = leer_transacciones_csv(ruta_archivo_transacciones)

    if not transacciones:
        print("No se pudieron leer las transacciones. Finalizando.")
        return

    print("\n--- Procesando y Categorizando Transacciones ---")
    # Pista 2: Necesitamos procesar cada transacción que leímos.
    # Inicia un bucle 'for' para recorrer cada 'transaccion' en la lista 'transacciones'.
    # for transaccion in transacciones:
    for transaccion in transacciones:

        # Pista 3: Dentro del bucle, por cada 'transaccion' (que es un diccionario),
        # necesitamos obtener su descripción.
        # Guarda el valor de la clave 'Descripcion' en una variable.
        descripcion = transaccion['Descripcion']
        # Pista 4: Con la descripción en una variable, es hora de usar nuestro nuevo módulo.
        # Llama a la función 'categorizar_transaccion()' y pásale la descripción.
        # Guarda el resultado en una variable llamada 'categoria_obtenida'.
        categoria_obtenida = categorizar_transaccion(descripcion)
        # Pista 5: ¡Ahora vamos a enriquecer nuestros datos!
        # Añade una nueva clave al diccionario 'transaccion'.
        # La clave debe ser 'Categoria' y su valor debe ser 'categoria_obtenida'.
        # La sintaxis es: diccionario['nueva_clave'] = valor
        transaccion['Categoria'] = categoria_obtenida

    # Finalmente, imprimimos los datos enriquecidos.
    print("\n--- Transacciones Enriquecidas con Categoría ---")
    for transaccion in transacciones:
        print(transaccion)
    print("------------------------------------")
    print(f"Se procesaron y categorizaron {len(transacciones)} transacciones.")


if __name__ == "__main__":
    main()
