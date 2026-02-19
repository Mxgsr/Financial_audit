## Historial de Avances

### Sesión del 17-02-2026: Creación del Módulo de Ingestión

-   **Objetivo Cumplido:** Leer datos de transacciones desde un archivo CSV y prepararlos para el análisis.
-   **Logros:**
    1.  **Creación de Datos de Prueba:** Se generó el archivo `data/raw/sample_transactions.csv` para simular datos bancarios reales, incluyendo formatos "sucios" (ej: `'$15.000'`).
    2.  **Módulo de Ingestión (`src/ingestion/file_reader.py`):**
        -   Se implementó la función `leer_transacciones_csv` para leer archivos CSV usando el `csv.DictReader`, convirtiendo cada fila en un diccionario para mayor robustez.
        -   Se creó una función de apoyo (`limpiar_monto`) para limpiar y convertir los montos (de texto a número), manejando símbolos monetarios y separadores de miles.
        -   El módulo ahora entrega una lista de diccionarios con datos limpios, lista para ser procesada por otras partes del sistema.
    3.  **Prácticas de Desarrollo Adquiridas:**
        -   Implementación de manejo de errores con `try-except` para `FileNotFoundError`.
        -   Uso del bloque `if __name__ == "__main__"` para pruebas a nivel de módulo.
        -   Depuración de errores comunes (`TypeError`, `NoneType` por falta de `return`).
        -   Se realizó el primer `git commit` del proyecto para versionar el código.
-   **Próximos Pasos:**
    -   Hacer que `main.py` sea el punto de entrada principal de la aplicación.
    -   **Tarea:** Modificar `main.py` para que:
        1.  Importe la función `leer_transacciones_csv` desde el módulo `src.ingestion.file_reader`.
        2.  Llame a la función para obtener la lista de transacciones limpias.
        3.  Imprima el resultado en la terminal para confirmar que la orquestación funciona.

### Sesión del 18-02-2026: Pipeline de Auditoría de 3 Etapas

-   **Objetivo Cumplido:** Orquestar un pipeline completo que ingiere, procesa y audita datos de transacciones.
-   **Logros:**
    1.  **Orquestación en `main.py`:** Se convirtió a `main.py` en el orquestador principal, llamando a los diferentes módulos en secuencia.
    2.  **Módulo de Procesamiento (`src/processing/categorizer.py`):**
        -   Se implementó la función `categorizar_transaccion` para asignar una categoría a cada transacción basada en palabras clave en su descripción.
        -   Se practicó el "desempaquetado de tuplas" y el uso de nombres de variables claros (plural/singular).
    3.  **Módulo de Auditoría (`src/auditor/anomaly_detector.py`):**
        -   Se implementó la función `detectar_anomalias_por_monto` para identificar transacciones que superen un umbral configurable.
        -   Se reforzó el principio de "Cero Hardcoding" al usar parámetros en lugar de valores fijos.
    4.  **Integración Completa:** Se integraron los tres módulos (`ingestion`, `processing`, `auditor`) en `main.py` para crear un pipeline funcional que lee, enriquece y reporta sobre los datos.
    5.  **Prácticas de Desarrollo Adquiridas:**
        -   Refuerzo de la arquitectura modular ("Lego").
        -   Uso de constantes para valores de configuración (ej: `UMBRAL_ANOMALIA`).
        -   Creación y prueba de módulos de forma aislada antes de la integración.
        -   Uso continuo de `git commit` para versionar cada avance significativo.
-   **Próximos Pasos:**
    -   Hacer el auditor más inteligente (ej: detectar suscripciones recurrentes).
    -   Persistir los datos procesados en una base de datos.
    -   Crear una interfaz de usuario con Streamlit.
