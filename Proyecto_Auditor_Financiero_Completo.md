# Roadmap y Arquitectura: Auditor de Gastos Personales

## 📅 1. Roadmap del Proyecto
- [ ] **Fase 1: Ingesta y Limpieza:** Normalización de cartolas bancarias con Pandas.
- [ ] **Fase 2: Motor de Clasificación:** Reglas Regex y clasificación asistida por IA local (Ollama).
- [ ] **Fase 3: Inteligencia de Auditoría:** Detección de anomalías (Z-Score) y suscripciones recurrentes.
- [ ] **Fase 4: Interfaz y Almacenamiento:** Dashboard en Streamlit y persistencia en DuckDB.

## 🏗️ 2. Arquitectura Lógica (Flujo de Datos)
1. **Capa de Ingesta (Adaptadores):** Módulos específicos que leen archivos crudos y entregan un estándar único.
2. **Capa de Transformación (Enriquecimiento):** Categorización y cálculo de variables financieras.
3. **Capa de Auditoría (El Analista):** Ejecución de algoritmos para detectar variaciones de precios y gastos atípicos.
4. **Capa de Persistencia:** Base de datos analítica local para consultas históricas rápidas.
5. **Capa de Presentación:** Visualización interactiva enfocada en hallazgos y alertas.

## 📁 3. Estructura de Carpetas Sugerida
```text
.
├── data/               # Datos privados (No subir a la nube)
│   ├── raw/            # Cartolas originales
│   ├── processed/      # Datos normalizados
│   └── database/       # Archivo .duckdb o .db
├── src/                # Lógica del sistema
│   ├── ingestion/      # Scripts de lectura por banco
│   ├── processing/     # Motores de categorización
│   ├── auditor/        # Lógica de detección de anomalías
│   └── ui/             # Dashboards de Streamlit
├── config/             # Reglas de negocio y diccionarios
├── tests/              # Validación de cálculos
├── requirements.txt    # Librerías necesarias
└── main.py             # Ejecución principal
```

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.x
- **Análisis:** Pandas, NumPy
- **Base de Datos:** DuckDB
- **Interfaz:** Streamlit
- **Auditoría:** SciPy (para análisis estadístico)
