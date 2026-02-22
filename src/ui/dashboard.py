import streamlit as st
import pandas as pd
import duckdb
import os

# --- Configuración de la Página ---
# Usamos st.set_page_config para definir el título de la pestaña del navegador y un ícono.
# 'wide' layout usa todo el ancho de la pantalla, lo que es mejor para dashboards.
st.set_page_config(page_title="Auditor Financiero", layout="wide", page_icon="💰")

# --- Título del Dashboard ---
# st.title() muestra un texto grande como el título principal de la aplicación.
st.title("Dashboard de Auditoría Financiera 🕵️‍♂️")

# --- Lógica de Carga de Datos ---
@st.cache_data
def cargar_datos_procesados():
    with duckdb.connect(database='data/database/auditor.db', read_only=True) as datos:
       query = "SELECT * FROM transacciones"
       df = datos.execute(query).df()
       return df 

# --- Cuerpo del Dashboard ---

# Primero, cargamos los datos
df_transacciones = cargar_datos_procesados()

# Si los datos se cargan correctamente, mostramos el dashboard
if not df_transacciones.empty:
    # --- KPIs (Indicadores Clave de Rendimiento) ---
    st.header("KPIs Principales")

    # Tarea: Calcula los siguientes valores usando Pandas
    ingreso_total = 0  # Reemplaza con tu cálculo
    gasto_total = 0    # Reemplaza con tu cálculo
    balance = 0        # Reemplaza con tu cálculo

    # Pista de Pandas para el gasto:
    # gasto_total = df_transacciones[df_transacciones['monto'] < 0]['monto'].sum()

    # Muestra los KPIs en 3 columnas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Ingreso Total", f"${ingreso_total:,.2f}")
    with col2:
        st.metric("Gasto Total", f"${gasto_total:,.2f}")
    with col3:
        st.metric("Balance", f"${balance:,.2f}")

    # Separador visual
    st.markdown("---")

    # --- Visor de Transacciones ---
    st.header("Visor de Transacciones")
    st.dataframe(df_transacciones)
else:
    st.warning("No se pudieron cargar los datos de las transacciones.")

# --- Siguientes Pasos (a modo de guía) ---
st.info(
    """
    **Próximos Pasos:**
    1.  Implementa la lógica en `cargar_datos_procesados` para leer desde DuckDB.
    2.  Una vez que la tabla se muestre, crearemos los KPIs (Indicadores Clave de Rendimiento).
    3.  Luego, añadiremos filtros interactivos (por categoría, por fecha, etc.).
    """
    
)
