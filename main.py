from src.ingestion.file_reader import leer_transacciones_csv
from src.processing.categorizer import categorizar_transaccion
from src.auditor.anomaly_detector import detectar_anomalias_por_monto


# --- CONFIGURACIÓN ---
# Es una buena práctica definir valores que pueden cambiar, como el umbral,
# en un solo lugar y en mayúsculas para indicar que son constantes.
UMBRAL_ANOMALIA = 25000.0



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

    for transaccion in transacciones:
        descripcion = transaccion['Descripcion']
        categoria_obtenida = categorizar_transaccion(descripcion)
        transaccion['Categoria'] = categoria_obtenida

    print(f"Se procesaron y categorizaron {len(transacciones)} transacciones.")


    # 3. AUDITORÍA
    # Pista 2: Llama a la función 'detectar_anomalias_por_monto'.
    # Necesita dos argumentos: la lista de 'transacciones' y la constante 'UMBRAL_ANOMALIA'.
    # Guarda el resultado (la lista de anomalías) en una nueva variable 'anomalias'.
    anomalias = detectar_anomalias_por_monto(transacciones, UMBRAL_ANOMALIA)


    # 4. REPORTE FINAL

    print("\n--- Reporte de Auditoría: Anomalías de Monto ---")

    if len(anomalias) > 0:
        for anomalia in anomalias:
            print(f" - Alerta: Gasto de ${anomalia['Monto']} en {anomalia['Descripcion']}")
    else:
        print("No se encontraron gastos por encima del umbral.")



if __name__ == "__main__":
    main()
