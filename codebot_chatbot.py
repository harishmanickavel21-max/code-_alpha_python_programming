# ============================================================
# TASK 4: Basic Rule-Based Chatbot
# CodeAlpha Python Programming Internship
# ============================================================

import random
import re
from datetime import datetime

# ─────────────────────────────────────────────────────────────
# Response rules: each entry maps a regex pattern → replies
# The bot picks a random reply from the list for variety.
# ─────────────────────────────────────────────────────────────

RULES = [
    # Greetings
    (r"hello|hi|hey|howdy|greetings",
     ["Hi there! 👋", "Hello! How can I help you?", "Hey! Great to see you!"]),

    # How are you
    (r"how are you|how r u|how do you do|you ok",
     ["I'm doing great, thanks for asking! 😊", "All good on my end! How about you?",
      "Running perfectly! How can I assist?"]),

    # What's your name
    (r"what('s| is) your name|who are you",
     ["I'm CodeBot 🤖 — your friendly Python chatbot!", "They call me CodeBot!",
      "I'm CodeBot, built for the CodeAlpha internship!"]),

    # What can you do
    (r"what can you do|help|features",
     ["I can chat with you, answer basic questions, and tell you the time! 🕐",
      "I'm a rule-based chatbot — ask me about time, jokes, or just say hi!"]),

    # Tell a joke
    (r"joke|funny|make me laugh",
     ["Why do programmers prefer dark mode? Because light attracts bugs! 🐛😄",
      "Why did the Python programmer wear glasses? Because he couldn't C! 😂",
      "I told a joke about a UDP packet once. You might not get it. 😏"]),

    # Time/date
    (r"time|what time|current time",
     [f"Current time: {datetime.now().strftime('%I:%M %p')} ⏰"]),

    (r"date|today|what('s| is) the date",
     [f"Today is {datetime.now().strftime('%A, %B %d, %Y')} 📅"]),

    # About Python
    (r"python|coding|programming",
     ["Python is awesome! 🐍 It's one of the most versatile languages out there.",
      "Love your Python enthusiasm! Keep coding! 💻"]),

    # Thank you
    (r"thank(s| you)|thx",
     ["You're welcome! 😊", "Happy to help!", "Anytime! 🙌"]),

    # Goodbye
    (r"bye|goodbye|exit|quit|see you",
     ["Goodbye! 👋 Have a great day!", "See you later! Take care! 😊",
      "Bye! Keep coding! 💻"]),
]

# Default replies when nothing matches
DEFAULT_REPLIES = [
    "I'm not sure I understand. Could you rephrase that?",
    "Hmm, I didn't get that. Try asking something else!",
    "I'm still learning! Could you try asking differently?",
    "That's beyond my current knowledge. Ask me something else! 🤔",
]


def get_response(user_input: str) -> str:
    """
    Match user input against rules and return an appropriate reply.
    Returns a default reply if no pattern matches.
    """
    text = user_input.lower().strip()

    for pattern, replies in RULES:
        if re.search(pattern, text):
            return random.choice(replies)

    return random.choice(DEFAULT_REPLIES)


def chat():
    """Main chatbot conversation loop."""
    print("=" * 50)
    print("   🤖 CodeBot — Rule-Based Chatbot")
    print("   Type 'bye' to exit at any time.")
    print("=" * 50)
    print("\nCodeBot: Hello! I'm CodeBot. How can I help you today?\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nCodeBot: Goodbye! 👋")
            break

        if not user_input:
            print("CodeBot: Please type something so I can help!\n")
            continue

        response = get_response(user_input)
        print(f"CodeBot: {response}\n")

        # Exit condition
        if re.search(r"bye|goodbye|exit|quit|see you", user_input.lower()):
            break


if __name__ == "__main__":
    chat()
