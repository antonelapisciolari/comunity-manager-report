import streamlit as st
import pandas as pd
from modules.sheet_connection import get_google_sheet
from google.oauth2.service_account import Credentials
from modules.navigation import render_menu
st.set_page_config(page_title="Reporte", layout="wide")
st.session_state["current_page"] = "report"

render_menu()

st.markdown(
    f"<h2 style='text-align: center;'>Reporte</h2>",
    unsafe_allow_html=True
)

def getInfo():
    sheet_id = '1mJ4aXamKDJXDzv5R31iEmwPOti21yrmTg2wYNE0773s'
    df = get_google_sheet('gsheets',sheet_id)
    return df
df = getInfo()


# Mostrar DataFrame en Streamlit
st.title("📈 Reporte desde Google Sheets")
st.dataframe(df, use_container_width=True)
