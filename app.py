# Streamlit app script
import streamlit as st

# Main application code
def app():
        st.title(f"Welcome :)!")
        cols = st.columns([3,1])
        with cols[0]:
            query = st.text_input('Search here', placeholder="Describe what you're looking for", label_visibility="collapsed")
        with cols[1]:
            btn = st.button('Search')
        # if btn and query:
        #     with st.spinner('Searching...'):
                 
        if st.sidebar.button("Logout"):
            st.session_state.page = "home"
            st.rerun()

