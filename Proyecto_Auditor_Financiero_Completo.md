# Hoja de Ruta del Proyecto: Auditor Financiero

## Fase 1: Fundación y Producto Mínimo Viable (MVP) - `(Completada)`
*   **Objetivo:** Probar que el concepto funciona. Crear un pipeline que pueda leer, entender y auditar datos de forma básica.
*   **Funcionalidades:**
    *   ✅ Módulo de Ingestión (Lector de CSV).
    *   ✅ Módulo de Procesamiento (Categorizador por palabras clave).
    *   ✅ Módulo de Auditoría (Detector de anomalías por monto).
    *   ✅ Orquestación del pipeline completo en `main.py`.

## Fase 2: Inteligencia del Auditor
*   **Objetivo:** Hacer que nuestro auditor sea más "inteligente" y nos dé insights más valiosos que solo gastos grandes.
*   **Funcionalidades Propuestas:**
    *   **Detector de Gastos Recurrentes:** Identificar suscripciones (Netflix, Spotify) o pagos mensuales (gimnasio, arriendo) que se repiten en descripción y monto.
    *   **Auditor de Presupuesto por Categoría:** Permitir definir un límite mensual por categoría (ej: "no más de $100.000 en 'Ocio'") y que el sistema alerte si nos pasamos.
    *   **Detector de Transacciones Duplicadas:** Buscar transacciones que parezcan idénticas (mismo monto y descripción en un corto periodo de tiempo), que suelen ser errores de cobro.

## Fase 3: Persistencia y Eficiencia
*   **Objetivo:** Darle "memoria" al programa para que no dependa de leer los archivos CSV cada vez. Esto es clave para manejar grandes volúmenes de datos.
*   **Funcionalidades Propuestas:**
    *   **Integración de Base de Datos:** Configurar una base de datos analítica local (DuckDB, como se mencionó en la visión original).
    *   **Módulo de Persistencia:** Crear funciones para guardar las transacciones procesadas y enriquecidas en la base de datos.
    *   **Lógica de "Caché":** Modificar `main.py` para que, antes de leer un archivo CSV, compruebe si los datos de ese archivo ya fueron procesados y guardados en la base de datos.

## Fase 4: Conexión con el Mundo Real
*   **Objetivo:** Adaptar el sistema para que ingiera y procese datos de formatos de bancos reales.
*   **Funcionalidades Propuestas:**
    *   **Adaptadores de Ingestión:** Crear un "adaptador" específico en el módulo de ingestión para cada formato de archivo de banco que queramos soportar (ej: `leer_banco_santander.py`, `leer_banco_chile.py`).
    *   **Manejo Avanzado de Errores:** Implementar una lógica más robusta para manejar fechas en distintos formatos, columnas con nombres diferentes, etc.

## Fase 5: Visualización e Interacción
*   **Objetivo:** Presentar los resultados de una forma amigable y útil para el usuario final.
*   **Funcionalidades Propuestas:**
    *   **Dashboard con Streamlit:** Crear una interfaz de usuario web simple.
    *   **KPIs y Métricas Clave:** Mostrar tarjetas con "Gasto Total del Mes", "Categoría con Mayor Gasto", "Total de Suscripciones", etc.
    *   **Tablas y Gráficos Interactivos:** Usar gráficos de barra/torta para visualizar gastos por categoría y una tabla para explorar todas las transacciones.
