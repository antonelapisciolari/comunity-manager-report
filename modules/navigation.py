import streamlit as st

def get_current_page_name():
    return st.session_state.get("current_page", "")

def render_menu():
    with st.sidebar:
        st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            width: 200px;  /* Adjust the width to your preference */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        st.title("Menu")
        st.write(f"Hola! {st.user.name}!")
        st.write("")
        
        if st.user.is_logged_in:
            st.page_link("pages/reporte.py", label="Reporte")
            st.page_link("pages/settings.py", label="Config")
            st.write("")
            st.write("")

            if st.button("Logout"):
                st.logout()
           
        elif get_current_page_name() != "streamlit_app":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the login page
            st.switch_page("streamlit_app.py")

