import streamlit as st
from user import login_signup_dialog
from app import app
st.set_page_config(page_title="Paperpedia", page_icon=":books:")
styles = "<style>"
with open("styles.css") as f:
    styles += f.read()
styles += "</style>"
st.markdown(styles, unsafe_allow_html=True)
def main_page():
    st.title("Paperpedia")
    st.write("Welcome to Paperpedia! Your recommender system for research papers.")
    if st.button("Get Started"):
        st.session_state.page = "login"
        st.rerun()

if not "page" in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    main_page()

elif st.session_state.page == "login":
    login_signup_dialog()

elif st.session_state.page == "app":
    app()