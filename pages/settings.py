import streamlit as st
from modules.navigation import render_menu
import pandas as pd
from modules.sheet_connection import get_sheets
from streamlit_gsheets import GSheetsConnection
st.session_state["current_page"] = "settings"

render_menu()

st.markdown(
    f"<h2 style='text-align: center;'>Settings</h2>",
    unsafe_allow_html=True
)

st.title("⚙️ Configuración de Clientes y Tokens")

df= get_sheets("gsheets", "settings")
conn = st.connection("gsheets_conn", type=GSheetsConnection) 

if df is None or df.empty:
    df = pd.DataFrame(columns=["Cliente", "Token"])

# Formulario para agregar nuevo cliente
st.subheader("Agregar nuevo cliente")
col1, col2 = st.columns(2)
with col1:
    nuevo_cliente = st.text_input("Cliente")
with col2:
    nuevo_token = st.text_input("Token")

if st.button("➕ Agregar"):
    if nuevo_cliente and nuevo_token:
        # Agregar a DataFrame en memoria
        nuevo_dato = pd.DataFrame([[nuevo_cliente, nuevo_token]], columns=["Cliente", "Token"])
        df = pd.concat([df, nuevo_dato], ignore_index=True)

        # Guardar en el Sheet
        conn.update(worksheet="settings", data=df)
        st.success("Cliente y token guardados correctamente.")
        st.rerun()
    else:
        st.warning("Por favor completá ambos campos.")

# Mostrar datos existentes
st.subheader("Clientes configurados")
st.dataframe(df, use_container_width=True)
