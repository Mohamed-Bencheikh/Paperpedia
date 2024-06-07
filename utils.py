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
def display_paper_card(paper):
     st.markdown(
            f"""
            <hr>
    <div class="paper-container">
    <div class="bookmark-checkbox">
    <input
      type="checkbox"
      id="bookmark-toggle"
      class="bookmark-checkbox__input"
    />
    <label for="bookmark-toggle" class="bookmark-checkbox__label">
      <svg class="bookmark-checkbox__icon" viewBox="0 0 24 24">
        <path
          class="bookmark-checkbox__icon-back"
          d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"
        ></path>
        <path class="bookmark-checkbox__icon-check" d="M8 11l3 3 5-5"></path>
      </svg>
    </label>
    </div>
    <div class="paper-header">
        <h5><span class="emoji">📄</span> {paper['title']}</h5>
        <div class="paper-meta">
        <p><span class="emoji">✒️</span> {', '.join(paper['authors'])}</p>
        <p><span class="emoji">📅</span> {paper['date']}</p>
        <p><span class="emoji">🏷️</span> {', '.join(paper['categories'])}</p>
        </div>
    </div>
    </div>
            """,
            unsafe_allow_html=True
        )

def social():
    st.markdown(f"""
        <footer>
        <div class="social-links">
        <a href="https://medbc.me" class="social-link" target="_blank">
            <img src="https://w7.pngwing.com/pngs/222/282/png-transparent-computer-icons-internet-world-wide-web-text-trademark-logo.png" alt="Portfolio">
        </a>
        <a href="https://linkedin.com/in/mohamed-bencheikh" class="social-link" target="_blank">
            <img src="https://cdn3d.iconscout.com/3d/free/thumb/free-linkedin-4059209-3364061@0.png?f=webp" alt="LinkedIn">
        </a>
        <a href="https://github.com/Mohamed-Bencheikh" class="social-link" target="_blank">
            <img src="https://img.icons8.com/material-outlined/24/000000/github.png" alt="GitHub">
        </a>
        <a href="https://huggingface.co/Mohamed-BC" class="social-link" target="_blank">
            <img src="https://workable-application-form.s3.amazonaws.com/advanced/production/61557f91d9510741dc62e7f8/c3635b59-a3d2-444a-b636-a9d0061dcdde" alt="Hugging Face">
        </a>
        </div>
        </footer>
        """,
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def test():
    with stylable_container(
        key="card",
        css_styles="""
            .card {
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
        """):
        st.markdown(
            """
            <div class="card">
                <h2>Card</h2>
                <p>This is a card component.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    preview_button = """
    <div class="col-span-1">
          <button class="rounded-md bg-slate-300 hover:bg-slate-600 hover:text-slate-200 duration-300 p-2">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
              <polyline points="15 3 21 3 21 9"></polyline>
              <line x1="10" y1="14" x2="21" y2="3"></line>
            </svg>
          </button>
        </div>
"""

