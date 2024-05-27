import streamlit as st
from user import login_signup_dialog
from app import app
from home import home
from about import description
from uprofile import profile
from details import display_paper_details
from chat import display_chat

st.set_page_config(page_title="Paperpedia", page_icon="media/image.png")
header = st.columns([1, 5])
with header[0]:
        st.image("media/image.png", width=90)
with header[1]:
        st.title("Paperpedia")

styles = "<style>"
with open("styles.css") as f:
    styles += f.read()
styles += "</style>"
st.markdown(styles, unsafe_allow_html=True)


if not "page" in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home()

elif st.session_state.page == "login":
    login_signup_dialog()

elif st.session_state.page == "app":
    app()

elif st.session_state.page == "about":
    description()

elif st.session_state.page == "profile":
    profile()

elif st.session_state.page == "details":
    display_paper_details(st.session_state.paper)

elif st.session_state.page == "chat":
    display_chat(st.session_state.paper["url"])
    
