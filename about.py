import streamlit as st
from utils import return_back, social

def description():
    return_back()    
    st.markdown(
        """
        ## About
        Paperpedia is a comprehensive platform that connects researchers, students, and professionals with the most relevant and up-to-date research papers in their field of interest. The goal of this project is to create a smart recommendation system that leverages machine learning and natural language processing techniques to suggest research papers tailored to the user's preferences and research interests.

        ## Features
        1. **Personalized Recommendations**: The system analyzes the user's profile, including their research interests, areas of expertise, and previous interactions with the platform, to provide personalized recommendations of research papers that align with their needs.
        2. **Multimodal Search**: Users can search for research papers using a variety of criteria, such as keyword, author, publication year, and discipline. The system also supports the ability to search by uploading a research paper, and the system will provide recommendations based on the content and themes of the uploaded paper.
        3. **Collaboration and Sharing**: Users can save their favorite research papers, create custom reading lists, and share them with colleagues or research groups. This feature facilitates the sharing of knowledge and encourages collaboration within the research community.
        4. **Notification System**: Users can set up alerts to receive notifications about new research papers, conferences, or events relevant to their interests, ensuring they stay up-to-date with the latest developments in their field.
        5. **Analytical Insights**: The platform provides users with analytical insights, such as trending research topics, influential authors, and emerging research areas, to help them stay informed about the latest trends and developments in their respective fields.
    
        Paperpedia is built using the following technologies:
        - **Frontend**: Streamlit, a Python-based web framework for building interactive web applications
        - **Backend**: Python, with libraries such as scikit-learn, TensorFlow, and spaCy for machine learning and natural language processing
        - **Database**: MongoDB, a NoSQL database, to store user profiles, research paper metadata, and recommendation data
        - **Deployment**: Docker and cloud-based hosting platforms, such as AWS or Google Cloud, for scalable and reliable deployment
      
        Paperpedia is an open-source project, and we welcome contributions from the research community. If you're interested in contributing, please check our [GitHub repository](https://github.com/Mohamed-Bencheikh) for more information on how to get started.

        
        
        ## Diagram
        """
    )


    st.markdown("""
    <div style="width: 710px; height: 480px; margin: 10px; position: relative;">
        <iframe allowfullscreen frameborder="0" style="width:640px; height:480px" src="https://lucid.app/documents/embedded/c681383a-f2f7-479b-9be9-60e815525a2c" id="AF7CBCR5hu9B">
    </iframe></div>
    """, unsafe_allow_html=True)

    st.markdown("""## Contact
For any inquiries or feedback, please feel free to reach out to us at [bencheikhmohamed811l@gmail.com](mailto:your-email@example.com)
                """)
    social()