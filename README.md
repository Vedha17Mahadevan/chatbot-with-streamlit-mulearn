# Simple Chatbot 🤖

A simple **rule-based chatbot** built with **Python + Streamlit** for the µLearn task  
`#cl-ai-chatbot` (Build a Simple Chatbot – 250 Karma Points).

---

## 🎯 Objective

This project implements a basic chatbot that:
- Greets the user
- Answers simple “about you” questions
- Tells programming jokes
- Shares motivational quotes
- Handles unknown queries with a friendly fallback response

The focus is on **simplicity**, **clarity**, and **learnability**.

---

## 🧠 Approach

**Type:** Rule-based chatbot (no external API)

- The chatbot analyzes the user’s message using simple **keyword-based intent detection**.
- Intents include:
  - `greeting` – e.g., “hi”, “hello”, “hey”
  - `goodbye` – e.g., “bye”, “see you”
  - `joke` – e.g., “tell me a joke”
  - `motivation` – e.g., “motivate me”, “I feel sad”
  - `about_bot` – e.g., “who are you?”
- Each intent is mapped to a set of predefined responses.
- If no intent matches, a default “I don’t understand yet” message is returned.

This makes the chatbot:
- Easy to understand
- Easy to extend (add more intents + responses)
- Fully offline (no API keys required)

---

## 🛠️ Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **Interface:** Streamlit Chat UI (`st.chat_message`, `st.chat_input`)

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/simple-chatbot.git
cd simple-chatbot
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.Start the Chatbot Web App
```bash
streamlit run app.py
```

---

## 🎥 Demo
Deployed App: [Try it out here](https://chatbot-with-app-mulearngit-musegqhhfysfsagdv5jv5j.streamlit.app/)
