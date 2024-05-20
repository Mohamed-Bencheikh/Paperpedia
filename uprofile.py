import streamlit as st
import database as db
import pandas as pd
import time
@st.experimental_dialog("Profile")
def profile():
    st.write("Tell more about yourself")
    role = st.selectbox("Role", ["Student", "Researcher", "Engineer", "Other"])
    df = pd.read_csv('arxiv_categories.csv')
    categories = df.groupby('Category')['Subcategory name'].apply(list).to_dict()   
    field = st.selectbox("Field", list(categories.keys()))
    subfield = st.multiselect("Subfield", categories[field])
    interests = st.multiselect("Interests", ["Healthcare", "Education", "Entertainement", "Business", "Technology"])
    cols = st.columns(2)
    with cols[0]:
        if st.button("Save", type="primary", use_container_width=True):
            user = st.session_state.user
            data = {
                "role": role,
                "field": field,
                "subfield": subfield,
                "interests": interests
            }
            try:
                db.update_user(user["email"], data)
                st.success("Profile updated!")
                time.sleep(1)
                st.session_state.page = "app"
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")
    with cols[1]:
        if st.button("Cancel", use_container_width=True):
            st.session_state.page = "app"
            st.rerun()