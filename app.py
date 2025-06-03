import streamlit as st
from modules.navigation import render_menu
st.set_page_config(page_title="Login", page_icon="cm.png")
st.session_state["current_page"] = "login"

if hasattr(st, "user") and st.user and st.user.is_logged_in:
    render_menu()

st.markdown(
    f"<h1 style='text-align: center;'>CM Reporte</h1>",
    unsafe_allow_html=True
)
st.subheader('')
col1,col2,col3 = st.columns(3)
with col2:
    if st.button("Iniciar sesión con Google"):
        st.login("google")
 