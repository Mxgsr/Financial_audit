from src.ingestion.file_reader import leer_transacciones_csv
from src.processing.categorizer import categorizar_transaccion
from src.auditor.anomaly_detector import detectar_anomalias_por_monto, detectar_suscripciones
import pandas as pd
from src.persistence.database import inicializar_base_datos, guardar_transacciones, contar_transacciones


# --- CONFIGURACIÓN ---
# Es una buena práctica definir valores que pueden cambiar, como el umbral,
# en un solo lugar y en mayúsculas para indicar que son constantes.
UMBRAL_ANOMALIA = 25000.0



def main():
    """
    Función principal que orquesta la aplicación.
    """
    inicializar_base_datos()
    if contar_transacciones() > 0:
        print("La base de datos ya contiene valores. No se procesará el archivo")
        return
    else:
        print("Base de datos vacía. Iniciando primer procesamiento del archivo CSV...")
        # 1. Ingreso de datos
        ruta_archivo_transacciones = "data/raw/sample_transactions.csv"
        print(f"Iniciando el proceso de auditoría para el archivo: {ruta_archivo_transacciones}")

        transacciones = leer_transacciones_csv(ruta_archivo_transacciones)

        if not transacciones:
            print("No se pudieron leer las transacciones. Finalizando.")
            return

        # 2. Procesamiento de datos
        print("\n--- Procesando y Categorizando Transacciones ---")

        for transaccion in transacciones:
            descripcion = transaccion['Descripcion']
            categoria_obtenida = categorizar_transaccion(descripcion)
            transaccion['Categoria'] = categoria_obtenida

        print(f"Se procesaron y categorizaron {len(transacciones)} transacciones.")


        # 3. AUDITORÍA
        # Necesita dos argumentos: la lista de 'transacciones' y la constante 'UMBRAL_ANOMALIA'.
        # Guarda el resultado (la lista de anomalías) en una nueva variable 'anomalias'.
        anomalias = detectar_anomalias_por_monto(transacciones, UMBRAL_ANOMALIA)
        suscripciones = detectar_suscripciones(transacciones)


        # 4. REPORTE FINAL

        print(f"\nSe encontraron {len(suscripciones)} grupos de suscripciones:")
        for grupo in suscripciones:
            nombre_suscripcion = grupo[0]['Descripcion'].strip().lower()
            print(f"- Grupo '{nombre_suscripcion}': {len(grupo)} transacciones encontradas.")
            for transaccion in grupo:
                print(f"  - Monto: ${transaccion['Monto']}")
        if not suscripciones:
            print("- Ninguna.")

        print("\n--- Reporte de Auditoría: Anomalías de Monto ---")

        if len(anomalias) > 0:
            for anomalia in anomalias:
                print(f" - Alerta: Gasto de ${anomalia['Monto']} en {anomalia['Descripcion']}")
        else:
            print("No se encontraron gastos por encima del umbral.")

        # 5. PERSISTENCIA FINAL
        print("\nConvirtiendo datos para guardar en la base de datos...")
        df_transacciones = pd.DataFrame(transacciones)
        columnas = ['Fecha_Trans', 'Descripcion', 'Monto', 'Categoria', 'Tarjeta']
        df_final= df_transacciones[columnas]
        guardar_transacciones(df_final)



if __name__ == "__main__":
        main()
