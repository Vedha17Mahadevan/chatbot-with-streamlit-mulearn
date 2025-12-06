# bot_logic.py

import random

GREETINGS = [
    "Hey there! 👋",
    "Hello! 😊",
    "Hi! How’s it going?",
    "Namaste! 🙏"
]

GOODBYES = [
    "Bye! See you soon 👋",
    "Goodbye! Take care 😊",
    "See you later! 👋",
    "It was nice chatting with you! 🌟"
]

JOKES = [
    "Why don't programmers like nature? It has too many bugs 🐛.",
    "Why do Java developers wear glasses? Because they don’t C# 🤓.",
    "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.' 😴"
]

MOTIVATION = [
    "You’re doing better than you think. Keep going! 💪",
    "Every expert was once a beginner. Don’t give up. 🚀",
    "Small steps every day lead to big changes. 🌱",
    "You are capable of amazing things. ✨"
]


def get_intent(message: str) -> str:
    """Very simple rule-based intent detection using keywords."""
    msg = message.lower()

    if any(word in msg for word in ["hi", "hello", "hey", "namaste"]):
        return "greeting"
    if any(word in msg for word in ["bye", "goodbye", "see you", "cya"]):
        return "goodbye"
    if any(word in msg for word in ["joke", "funny", "laugh"]):
        return "joke"
    if any(word in msg for word in ["motivate", "motivation", "inspire", "sad", "tired"]):
        return "motivation"
    if any(word in msg for word in ["who are you", "what can you do", "about you"]):
        return "about_bot"
    return "unknown"


def generate_response(message: str) -> str:
    """Return a chatbot response based on detected intent."""
    intent = get_intent(message)

    if intent == "greeting":
        return random.choice(GREETINGS)

    if intent == "goodbye":
        return random.choice(GOODBYES)

    if intent == "joke":
        return random.choice(JOKES)

    if intent == "motivation":
        return random.choice(MOTIVATION)

    if intent == "about_bot":
        return (
            "I'm a simple rule-based chatbot 🤖 built in Python. "
            "I can greet you, tell you jokes, share motivation, and have basic conversations!"
        )

    # Fallback
    return (
        "Hmm, I’m not sure how to respond to that yet 😅.\n"
        "Try asking me for a joke, some motivation, or just say hi!"
    )
