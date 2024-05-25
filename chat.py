from langchain.document_loaders import PyPDFLoader
import streamlit as st
import google.generativeai as genai

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

def display_chat(paper_url):
    pdf_text = load_paper_content(paper_url)
    if len(pdf_text) > 10000:
        st.warning("The document is too long, the chatbot may not work properly.")
    if 'messages' not in st.session_state:
        st.session_state.messages = [{'role': 'assistant', "content": "Hello! let's get started."}] 
    user_prompt = st.chat_input("What do you wanna know about the paper?")
    if user_prompt:
        st.session_state.messages.append({'role': 'user', "content": user_prompt})
        with st.spinner("..."):
            response = chat(user_prompt, pdf_text)
            st.session_state.messages.append({'role': 'assistant', "content": response})

    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'], unsafe_allow_html=True)

    
