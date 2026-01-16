import streamlit as st
import pandas as pd
from streamlit_autorefresh import st_autorefresh # Importación necesaria

st.set_page_config(page_title="Streaming Log Dashboard")

# 1. Configurar el refresco automático cada 2000 milisegundos (2 segundos)
st_autorefresh(interval=2000, key="refresh")

st.title("Dashboard en streaming desde un archivo CSV")

try:
    # 2. Leer el archivo (usamos tail para que no sea pesado si el archivo crece mucho)
    # Esto lee todo el CSV y luego se queda con los últimos 500
    df = pd.read_csv("log.csv").tail(500)

    # 3. Visualizaciones en tiempo real
    st.subheader("Gráfico de valores en vivo")
    st.line_chart(df["valor"])

    st.subheader("Últimos registros")
    st.dataframe(df.tail(5))

except FileNotFoundError:
    st.error("No se encuentra el archivo 'log.csv'. Por favor, créalo en la carpeta del proyecto.")
except Exception as e:
    st.warning(f"Esperando datos válidos... {e}")