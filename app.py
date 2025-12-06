# app.py

import streamlit as st
from bot_logic import generate_response

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("Simple Chatbot 🤖")
st.write("A tiny rule-based chatbot built with Python + Streamlit.")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]

    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(content)

# Chat input box (new in Streamlit)
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot reply
    bot_reply = generate_response(user_input)

    # Add bot reply to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Display bot reply immediately
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
