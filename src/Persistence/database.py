import duckdb
import pandas as pd

DB_FILE ="data/database/auditor.db"

def inicializar_base_datos():
    """
    Se conecta a la base de datos y crea la tabla 'transacciones' si no existe.
    """
    # 1. Conectar a la base de datos
    database = duckdb.connect(DB_FILE)
    # 2. Definir la estructura de la tabla
    creat_tabla_sql = """
    CREATE TABLE IF NOT EXISTS transacciones (
    Fecha TEXT,
    Descripcion TEXT,
    Monto REAL,
    Categoria TEXT
    );
    """
    # 3. Ejecutar el comando
    database.execute(creat_tabla_sql)

    # 4. Cerrar la conexión para liberar el archivo.
    database.close()
    print(f"Base de datos inicializada en {DB_FILE}")

def guardar_transacciones(df_transacciones):
    """
    Guarda un DataFrame de pandas en la tabla 'transacciones' de DuckDB
    :param df_transacciones: Un DataFram de pandas con las transacciones.
    """
    database = duckdb.connect(DB_FILE)
    # DuckDB puede insertar DataFrames de pandas directo en una tabla.
    # Usamos el df 'df_transacciones' como si fuera una tabla temporal
    # le decimos que inserte todo (*) desde ahi a la base de datos permanente
    database.execute("INSERT INTO transacciones SELECT * FROM df_transacciones")
    database.close()
    print(f"Se guardaron {len(df_transacciones)} transacciones en la base de datos.")

# TESTING

if __name__ == "__main__":
    print("Ejecutando inicializador de la base de datos...")
    inicializar_base_datos()
    print("\nCreando datos de prueba para guardar...")
    datos_de_prueba = {
        'Fecha': ['2026-01-05','2025-01-05'],
        'Descripcion': ['Cafeteria', 'Libreria'],
         'Monto': [5400, 15000],
         'Categoria': ['Alimentacion','Ocio']   
    }
    df_prueba =pd.DataFrame(datos_de_prueba)
    print("Probando función para guardar transacciones...")
    guardar_transacciones(df_prueba)
    print("\nProceso completado.")