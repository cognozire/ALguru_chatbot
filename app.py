import streamlit as st
import pathlib
import textwrap
import google.generativeai as genai

genai.configure(api_key='AIzaSyCBkKSe9dtzeQCVW5Of07_QyngJAGONtlQ')

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

import docx2txt

file_path = pathlib.Path('WA_chatbot.docx')
content = docx2txt.process(file_path)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("system"):
    st.write("Hi there!👋I'm ready to answer your questions. Ask me anything!")
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your query"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt.lower() in ("hi", "hello", "hey"):  # Handle multiple greetings
        response = "How can I help you today?😊"
    elif prompt.lower() in ("what is algooru","what services do you offer?","can you give me an overview of your platform","who do you serve?","what does your platform provide?","what are your services?"):
        response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
    elif prompt.lower() in ("where is alguru located","where is your headquarters?","where is your location?","where is your company?","where do you conduct sessions?","what are your services?"):
        response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
    elif prompt.lower() in ("how can i work with you?","how can i work with you"):
        response = "AlGooru is an educational platform that connects parents and students with qualified and vetted tutors, offering in-person and online sessions in 20 core subjects that cover all educational levels, along with some university and professional fields."
    elif prompt.lower() in ("is there a limit to the number of packages i'm allowed to have?","is there a limit to the number of packages i'm allowed to have"):
        response = "You can subscribe to multiple packages simultaneously, and our team will assist you with your request."
    elif prompt.lower() in ("how much do you charge for a session?","how much do you charge for a session"):
        response = "Our prices per hour range from 88 to 152 SAR, depending on your chosen package. Our experts will recommend a package that best fits your needs and preferences."

    else:
        # context_truncated = textwrap.shorten(content, width=1000)
        response1 = model.generate_content([
            "You are an expert customer assistant from AlGooru Team. I'll give you question and context and you'll return the answer. Answer in 50 words in a paragraph. Also do not answer any questions related to LGBTQ+, Homosexuality, religion, politics. Try to make answers sound more humanistic",
            f"Question: {prompt}",
            f"Context: {content}"
        ])
        response = f"{response1.text}"

    # st.write(response)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
