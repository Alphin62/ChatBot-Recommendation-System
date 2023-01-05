#!/usr/bin/env python
# coding: utf-8

# In[4]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import streamlit as st


# In[ ]:


chatbot = ChatBot("My Chatbot")

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")


# In[ ]:


import json

with open('intents.json') as json_data:
    intents = json.load(json_data)

responses = {}

for intent in intents['intents']:
    responses[intent['tag']] = intent['responses']


# In[ ]:


st.title("My Chatbot")

while True:
    user_input = st.text_input("Enter your message:", key='input')

    if user_input == "exit":
        break

    response = chatbot.get_response(user_input)
    st.write("Chatbot: ", response)

    # Check if the response is in our intents and use the pre-defined response if it is
    for tag, response_list in responses.items():
        if str(response) in response_list:
            st.write("Chatbot: ", random.choice(response_list))
            break


# In[ ]:



st.write("Chatbot: ", response)


# In[ ]:





# In[ ]:





# In[ ]:




