import streamlit as st
from app import display_search_results
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