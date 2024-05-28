import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def return_back():
    with stylable_container(
            key="back",
            css_styles="""
                button {
                    background-image: url('https://previews.123rf.com/images/faysalfarhan/faysalfarhan1502/faysalfarhan150200725/36414619-back-arrow-icon-glassy-blue-button.jpg');
                    background-size: cover;
                    background-position: center;
                    border: none;
                    width: 30px;
                    height: 30px;
                }
                """):
            if st.button(""):
                if 'user' in st.session_state:
                    st.session_state.page = "app"
                else:
                    st.session_state.page = "home"
                st.rerun()