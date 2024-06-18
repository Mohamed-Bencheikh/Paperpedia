from streamlit_extras.card import card
import time
import streamlit as st
from streamlit_extras.streaming_write import write
from streamlit_extras.row import row
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.tags import tagger_component
import pandas as pd
import numpy as np
def example(key = None):

    card(

        title="Hello World!",
        text="Some description",
        image= "https://wallpapertag.com/wallpaper/full/8/4/9/608783-cool-gothic-wallpapers-1920x1200-picture.jpg",
        url="https://www.google.com",
        key=key

    )


def stream_example():
    _LOREM_IPSUM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \n
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \n
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    
    for word in _LOREM_IPSUM.split():
        yield word + " "
        time.sleep(0.1)
    # Also supports any other object supported by `st.write`
    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )



    for word in _LOREM_IPSUM.split():

        yield word + " "

        time.sleep(0.05)


### Row Layout
def example():

    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])



    row1 = row(2, vertical_align="center")

    row1.dataframe(random_df, use_container_width=True)

    row1.line_chart(random_df, use_container_width=True)



    row2 = row([2, 4, 1], vertical_align="bottom")



    row2.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])

    row2.text_input("Your name")

    row2.button("Send", use_container_width=True)

## Stylable containers
def example():

    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            """,
    ):
        st.button("Green button")



    st.button("Normal button")



    with stylable_container(

        key="container_with_border",

        css_styles="""

            {

                border: 1px solid rgba(49, 51, 63, 0.2);

                border-radius: 0.5rem;

                padding: calc(1em - 1px)

            }

            """,

    ):

        st.markdown("This is a container with a border.")

def example():

    tagger_component("Here is a feature request", ["p2", "🚩triaged", "backlog"])

    tagger_component(

        "Here are colored tags",

        ["turtle", "rabbit", "lion"],

        color_name=["blue", "orange", "lightblue"],

    )

    tagger_component(

        "Annotate the feature",

        ["hallucination"],

        color_name=["blue"],

    )
if __name__ == "__main__":
    if st.button("Stream data"):
        write(stream_example)

#     st.markdown(
    #         f"""
    #         <div class="paper-container">
    #             <div class="paper-header">
    #                 <h5><span class="emoji">📄</span> {res['title']}</h5>
    #                 <div class="paper-meta">
    #                     <a href="{res['url']}"><span class="emoji"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link">
    #     <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
    #     <polyline points="15 3 21 3 21 9"></polyline>
    #     <line x1="10" y1="14" x2="21" y2="3"></line>
    #   </svg></span>
    #                 </div>
    #             </div>""", unsafe_allow_html=True)