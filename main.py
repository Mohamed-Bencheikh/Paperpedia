import streamlit as st
from streamlit_extras.colored_header import colored_header
from user import login_signup_dialog
from app import app
from about import description
from uprofile import profile
   
st.set_page_config(page_title="Paperpedia", page_icon=":books:")
styles = "<style>"
with open("styles.css") as f:
    styles += f.read()
styles += "</style>"
st.markdown(styles, unsafe_allow_html=True)
def main_page():
    colored_header(
        label="Paperpedia",
        description="A recommender system for Research papers",
        color_name="violet-70",
    )
    # st.title("Paperpedia")
    # st.write("Welcome to Paperpedia! Your recommender system for research papers.")
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

elif st.session_state.page == "about":
    description()

elif st.session_state.page == "profile":
    profile()