#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import random

import streamlit as st

def get_intents():
    with open("intents.json") as f:
        intents = json.load(f)
    return intents

intents = get_intents()

st.title("Chatbot")

while True:
    message = st.text_input("You:")
    if message.lower() == "quit":
        break

    responses = []
    for intent in intents["intents"]:
        if message.lower() in intent["patterns"]:
            responses = intent["responses"]

    if responses:
        st.text(random.choice(responses))
    else:
        st.text("I'm sorry, I don't know how to respond to that.")


# In[ ]:




