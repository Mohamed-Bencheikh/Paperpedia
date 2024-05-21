import streamlit as st
def home():
    st.title("Paperpedia")
    st.subheader("A recommender System for Research Papers")
    st.markdown("""
    - Discover the latest publications in your field of interest
    - Get relevant results for your search
    - See detailed paper information
    - Chat with your paper.
    """)
    
    btns = st.columns([1,1])
    if st.button("Get Started", type="primary"):
            st.session_state.page = "login"
            st.rerun()
    if st.button("Read More"):
            st.session_state.page = "about"
            st.rerun()
    
