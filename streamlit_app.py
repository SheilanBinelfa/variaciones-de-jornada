import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Simulador de Variaciones de Jornada",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargar el HTML
with open("simulador-variaciones.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Renderizar el simulador
components.html(html_content, height=1200, scrolling=True)
