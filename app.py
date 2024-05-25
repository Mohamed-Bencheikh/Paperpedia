# Streamlit app script
import streamlit as st
from streamlit_option_menu import option_menu
from recommend import get_latest_papers, get_relevant_passage, get_chat_response

def display_latest_papers():
    fields = st.session_state.user['subfields']
    results = []
    for field in fields:
        papers = get_latest_papers(category="cat:"+field)
        results.extend(papers)
    for res in results:
        st.markdown(
            f"""
            <hr>
            <div class="paper-container">
                <div class="paper-header" >
                    <h5><span class="emoji">📄</span> {res['title']}</h5>
                    <div class="paper-meta">
                        <p><span class="emoji">✒️</span> {', '.join(res['authors'])}</p>
                        <p><span class="emoji">📅</span> {res['date']}</p>
                        <p><span class="emoji">🏷️</span> {', '.join(res['categories'])}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        btns = st.columns([.7,5.2])
        with btns[0]:
            if st.button('Details', type='primary', key=res['Id']):
                st.session_state.paper = res 
                st.session_state.page = "details"       
        with btns[1]:
            st.link_button('View', url=res['url'])
            

def display_search_results(query):
    results = get_relevant_passage(query)
    for res in results:
        st.markdown(
            f"""
            <div class="paper-container">
                <div class="paper-header">
                    <h5><span class="emoji">📄</span> {res['title']}</h5>
                    <div class="paper-meta">
                        <a href="{res['url']}"><span class="emoji">Open</span>
                    </div>
                </div>""", unsafe_allow_html=True
                )
        
        
def display_chat_response(query):
    with st.chat_message(name='user'):
        st.write(query)
    with st.chat_message(name='ai'):
        response = get_chat_response(query)
        st.markdown(response) 

# @st.experimental_dialog(title="Paper Details")
def display_paper_details(res):
    cols = st.columns([4,2])
    with cols[0]:
        st.markdown(
            f"""
            <div id="paper-container">
                <div id="paper-header">
                    <h5><span class="emoji">📄</span> {res['title']}</h5>
                    <div id="paper-meta">
                        <p><span class="emoji">✒️</span> {', '.join(res['authors'])}</p>
                        <p><span class="emoji">📅</span> {res['date']}</p>
                        <p><span class="emoji">🏷️</span> {', '.join(res['categories'])}</p>
                        <p><span class="emoji">📰</span> {res['journal']}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.expander("Abstract").write(res['abstract'])
    with cols[1]:
        display_search_results(res['title'])

def app():
        cols = st.columns([1,4.5,1])
        with cols[0]:
            chat = st.toggle("Chat")
        with cols[1]:
            query = st.text_input('Search here', placeholder="Describe what you're looking for", label_visibility="collapsed")
        with cols[2]:
            btn = st.button('Search', type='primary')
        with st.container():
            if btn and query:
                with st.spinner('Searching...'):
                    if chat:
                        display_chat_response(query)
                    else:
                        display_search_results(query)
            tabs = st.tabs(['Latest', 'Trending', 'Recommended'])
            with tabs[0]:
                display_latest_papers()
            with tabs[1]:
                st.write("Trending papers")
            with tabs[2]:
                st.write("Recommended papers")
            with st.sidebar:
                st.write(f"**{st.session_state.user['fullname']}**")
                options = option_menu(None, ["Home", "Profile", "About", "Settings", "Logout"])
                if options == "Profile":
                    st.session_state.page = "profile"
                    st.rerun()
                elif options == "About":
                    st.session_state.page = "about"
                    st.rerun()
                elif options == "Logout":
                    del st.session_state.user
                    st.session_state.page = "home"
                    st.rerun()






