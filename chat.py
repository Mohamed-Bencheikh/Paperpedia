from langchain_community.document_loaders import PyPDFLoader
import google.generativeai as genai
import streamlit as st
from utils import return_back

def load_paper_content(url):
    loader = PyPDFLoader(url)
    doc = loader.load()
    content = []
    for page in doc:
        content.append(page.page_content)
    return " ".join(content)

def chat(query, context):
    prompt = f"""
    You are an AI assistant, answer the user question based on the context below, the context is retrieved from a SCIENTIFIC PAPER.
    if the context is not relevant to the user query, say that you does not find any relevant context to the question, but if you have a background knowledge about the user query answer based on your knowledge, but mention that.
    QUESTION: {query}
    CONTEXT: {context}
    """
    chat_model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = chat_model.generate_content(prompt)  
    return response.text

def display_chat(paper):
    pdf_text = load_paper_content(paper['url'])
    return_back()
    if pdf_text:
        st.info(paper['title'], icon="📄")
    if 'messages' not in st.session_state:
        ufname = st.session_state.user['fullname'].split(" ")[0]
        st.session_state.messages = [{'role': 'assistant', "content": "Hello "+ufname+" !\nWhat do you wanna know about this paper?"}] 
    user_prompt = st.chat_input("Your question here...")
    if user_prompt:
        st.session_state.messages.append({'role': 'user', "content": user_prompt})
        with st.spinner("..."):
            response = chat(user_prompt, pdf_text)
            st.session_state.messages.append({'role': 'assistant', "content": response})

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'], unsafe_allow_html=True)

    
