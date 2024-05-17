# Streamlit app script
import streamlit as st
from recommend import get_latest_papers
# Main application code
def app():
        st.title(f"Welcome  {st.session_state.user['fullname']} :)")
        cols = st.columns([1,4,1])
        with cols[0]:
            st.toggle("Chat", help="enable chat mode")
        with cols[1]:
            query = st.text_input('Search here', placeholder="Describe what you're looking for", label_visibility="collapsed")
        with cols[2]:
            btn = st.button('Search')
        # if btn and query:
        #     with st.spinner('Searching...'):
        tabs = st.tabs(['Latest', 'Trending', 'Recommended'])
        with tabs[0]:
            display_latest_papers()
        with tabs[1]:
            st.write("Trending papers")
        with tabs[2]:
            st.write("Recommended papers")
        if st.sidebar.button("Logout"):
            st.session_state.page = "home"
            st.rerun()

def display_latest_papers(category="cat:cs.CV"):
    papers = get_latest_papers(category)
    for paper in papers:
        st.markdown(
            f"""
            <div class="paper-container">
                <div class="paper-header">
                    <h3><span class="emoji">📄</span> {paper['title']}</h3>
                    <div class="paper-meta">
                        <p><span class="emoji">🧑‍🔬</span> {', '.join(paper['authors'])}</p>
                        <p><span class="emoji">📅</span> {paper['date']}</p>
                        <p><span class="emoji">🏷️</span> {', '.join(paper['categories'])}</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# <div class="paper-actions">
#                         <a href="{paper['url']}" target="_blank" class="btn"><span class="emoji">🔗</span> Open</a>
#                         <button class="btn"><span class="emoji">📖</span> Abstract</button>
#                         <button class="btn"><span class="emoji">👁️</span> Preview</button>
#                     </div>