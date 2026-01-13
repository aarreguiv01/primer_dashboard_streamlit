import streamlit as st
import pandas as pd
import plotly.express as px
import time

# Configuración de la página
st.set_page_config(page_title="Dashboard Tiempo Real", layout="wide")

st.title("📊 Dashboard de Ventas y Monitoreo Log")

# --- SECCIÓN 1: DATOS ESTÁTICOS (VENTAS) ---
with st.sidebar:
    st.header("Filtros de Ventas")
    year = st.selectbox("Selecciona el Año", [2022, 2023, 2024])

df_ventas = pd.DataFrame({
    "Año": [2022, 2022, 2023, 2023, 2024, 2024],
    "Mes": ["Ene","Feb","Ene","Feb","Ene","Feb"],
    "Ventas": [100,150,200,180,250,300]
})
df_filtrado = df_ventas[df_ventas["Año"] == year]

col1, col2 = st.columns(2)

with col1:
    st.metric("Ventas totales", f"{df_filtrado['Ventas'].sum()} €")
    fig = px.bar(df_filtrado, x="Mes", y="Ventas", title=f"Ventas por mes ({year})")
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN 2: ACTUALIZACIÓN EN TIEMPO REAL (LOGS) ---
st.divider()
st.subheader("📈 Monitoreo en Tiempo Real (log.csv)")

# Contenedor vacío para actualizar solo esta parte
placeholder = st.empty()

# Bucle de actualización
while True:
    try:
        # Leer el CSV (asegúrate de que log.csv esté en la misma carpeta)
        df_log = pd.read_csv("log.csv")
        
        with placeholder.container():
            kpi1, kpi2 = st.columns(2)
            
            # Último valor registrado
            ultimo_valor = df_log["valor"].iloc[-1]
            kpi1.metric("Último Valor Log", f"{ultimo_valor} unidades")
            
            # Gráfico de línea en tiempo real
            st.line_chart(df_log.set_index("timestamp")["valor"])
            
            # Mostrar las últimas filas
            st.write("Últimas entradas del log:")
            st.dataframe(df_log.tail(5), use_container_width=True)

    except Exception as e:
        st.error(f"Error leyendo log.csv: {e}")
    
    # Esperar 2 segundos antes de la próxima actualización
    time.sleep(2)
    st.rerun()