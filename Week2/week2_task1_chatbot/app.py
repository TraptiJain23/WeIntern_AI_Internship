"""
Career Guidance Chatbot

Features:

Intent Recognition using RapidFuzz
Context-Aware Multi-Turn Conversation
Conversation History Logging
Streamlit Chat Interface

"""


#import libraries
import streamlit as st
import json
import random
from rapidfuzz import fuzz
from datetime import datetime

from pathlib import Path
BASE_DIR = Path(__file__).parent


# Load intents dataset from JSON file
with open(BASE_DIR / "intents.json", "r") as file:
    intents = json.load(file)


# # Preprocess user input for matching
def preprocess(text):
    return text.lower().strip()

# Intent matching function(using RapidFuzz)

def get_response(user_input):

    user_input = preprocess(user_input)

    best_score = 0
    best_intent = None

    for intent in intents["intents"]:

        for pattern in intent["patterns"]:

            score = fuzz.ratio(
                user_input,
                pattern.lower()
            )

            if score > best_score:
                best_score = score
                best_intent = intent

    if best_score >= 60:
        return (
            random.choice(best_intent["responses"]),
            best_intent["tag"]
        )

    return (
        "Sorry, I didn't understand that. Please rephrase your question.",
        "fallback"
    )


# # Initialize session state variables

if "messages" not in st.session_state:
    st.session_state.messages = []

if "career" not in st.session_state:
    st.session_state.career = None



# Streamlit page title

st.title("🎯 Career Guidance Chatbot")

st.write(
    "Ask me about careers, internships, resumes, certifications, interviews, and more."
)


# Display previous chat messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])




# User input box

user_input = st.chat_input(
    "Type your question here..."
)


# Handle user input

if user_input:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)


    response, tag = get_response(user_input)
    # Store career preference for context memory

    if tag == "data_analyst":
        st.session_state.career = "Data Analyst"

    elif tag == "software_developer":
        st.session_state.career = "Software Developer"

    elif tag == "data_scientist":
        st.session_state.career = "Data Scientist"

    elif tag == "cybersecurity":
        st.session_state.career = "Cybersecurity Analyst"



    # Context-aware responses

    if "skills" in user_input.lower():

        if st.session_state.career == "Data Analyst":

            response = """
### Skills for Data Analyst

- Excel
- SQL
- Python
- Statistics
- Power BI
"""
        elif st.session_state.career == "Software Developer":

            response = """
### Skills for Software Developer

- Programming
- DSA
- Databases
- Git
- Web Development
"""
        elif st.session_state.career == "Data Scientist":

            response = """
  ### Skills for Data Scientist

  - Python
  - Statistics
  - Machine Learning
  - SQL
  - Data Visualization
  """

        elif st.session_state.career == "Cybersecurity Analyst":

            response = """
  ### Skills for Cybersecurity Analyst

  - Networking
  - Linux
  - Ethical Hacking
  - Security Tools
  - Incident Response
  """

    elif "certification" in user_input.lower():

        if st.session_state.career == "Data Analyst":

            response = """
### Recommended Certifications:

- Google Data Analytics
- IBM Data Science
"""

        elif st.session_state.career == "Software Developer":

            response = """
### Recommended Certifications:

- AWS Cloud Practitioner
- Microsoft Azure Fundamentals
"""

        elif st.session_state.career == "Data Scientist":

            response = """
### Recommended Certifications

- IBM Data Science
- Google Advanced Data Analytics
"""

        elif st.session_state.career == "Cybersecurity Analyst":

            response = """
### Recommended Certifications

- CompTIA Security+
- CEH (Certified Ethical Hacker)
"""

    # Save bot response

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Display latest response

    with st.chat_message("assistant"):
        st.markdown(response)

    # Save conversation to log file

    with open("chat_history.txt", "a") as file:

        file.write(
            f"{datetime.now()} | USER: {user_input}\n"
        )

        file.write(
            f"{datetime.now()} | BOT: {response}\n\n"
        )





