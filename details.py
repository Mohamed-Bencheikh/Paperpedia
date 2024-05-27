import streamlit as st
from streamlit_extras.stoggle import stoggle
from app import display_search_results
def display_paper_details(res):
    btns = st.columns([0.8,5.2])
    with btns[0]:
        if st.button("Back"):
            st.session_state.page = "app"
            st.rerun()
    with btns[1]:
        if st.button("Chat", type="primary"):
            st.session_state.page = "chat"
            st.rerun()
    cols = st.columns([4,3])
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
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        # st.expander("Abstract").markdown(res['abstract'])
        stoggle("Abstract", res['abstract'])
    with cols[1]:
        tabs = st.tabs(['Similar Papers', 'Same Authors', 'Citations'])
        with tabs[0]:
            display_search_results(res['title'])
        with tabs[1]:
            st.markdown("This section contains papers from the same authors")
        with tabs[2]:
            st.markdown("This section contains papers that cited this paper")
        # <p><span class="emoji">📰</span> {res['comment']}</p>
