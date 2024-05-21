import streamlit as st
import database as db
import time
def login():
    with st.form(key="login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login", type='primary', use_container_width=True):
            user = db.fetch_user({"email": email, "password": password})
            if user:
                st.session_state.user = user
                st.session_state.page = "app"
                st.rerun()
            else:
                st.error("Invalid username or password.")

def signup():
    with st.form(key="signup_form"):
        fullname = st.text_input("Name")
        email = st.text_input("Email")     
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Sign Up", type='primary', use_container_width=True) and fullname and email and password:
            try:
                user = db.create_user(fullname, email, password)
                st.success("Signed up.")
                time.sleep(1)
                st.session_state.user = db.fetch_user({"email": email, "password": password})
                st.session_state.page = "profile"
                st.rerun()
            except Exception as e:
                st.error(str(e))

@st.experimental_dialog("Login/Sign Up")
def login_signup_dialog():
    tabs = st.tabs(['Login', 'Sign Up'])
    with tabs[0]:
        login()
    with tabs[1]:
        signup()