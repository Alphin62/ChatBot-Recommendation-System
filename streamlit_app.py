#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import random
import streamlit as st
from nltk.chat.util import Chat, reflections

# Load the intents file
with open('intents.json') as f:
    intents = json.load(f)

# Create the responses list
responses = []

# Loop through the intents and create a list of tuples
for intent in intents['intents']:
    for pattern in intent['patterns']:
        responses.append((pattern, intent['responses']))

# Create the chatbot
chatbot = Chat(responses, reflections)

# Set up the Streamlit interface
st.title("Chatbot")

while True:
    # Get the user's input
    message = st.text_input('You:')
    if message.strip().lower() == 'bye':
        st.text('Bot: Goodbye!')
        break

    # Get the chatbot's response
    response = chatbot.respond(message)
    st.text(f'Bot: {random.choice(response)}')

