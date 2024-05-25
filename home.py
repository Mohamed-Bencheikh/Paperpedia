import streamlit as st
from streamlit_card import card
def home():
        
                # st.markdown("<h5>A Recommender System for Research Papers</h5>", unsafe_allow_html=True)
        # with header[2]:
        body = st.columns([3.5, 2.5])
        with body[0]:
                st.markdown("""
                <div class="home-list">
                <li><b>Get recommendations based on your preferences</li>
                <li><b>Get relevant results for your search</li>
                <li><b>See detailed paper information</li>
                <li><b>Discover the latest publications in your field of interest</li>
                </div>
                """, unsafe_allow_html=True)
                btns = st.columns([1, 2.6])
                with btns[0]:
                        if st.button("Get Started", type="primary"):
                                st.session_state.page = "login"
                                st.rerun()
                with btns[1]:
                        if st.button("Read More"):
                                st.session_state.page = "about"
                                st.rerun()
        with body[1]:
                st.image("media/Publish article-rafiki.png", width=400)

        
        
        
    
