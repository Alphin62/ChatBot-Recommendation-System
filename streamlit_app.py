#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
import streamlit as st
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from chatbot_model import *


# In[ ]:


# Load the intents file
with open('intents.json') as json_data:
    intents = json.load(json_data)

model = RandomForestClassifier()

# Load the trained chatbot model
model.load('path/to/chatbot_model.pkl')


# In[ ]:


def classify_text(text):
    text = np.array([text])
    return model.predict(text)[0]


def get_response(classification):
    
    for intent in intents['intents']:
        if intent['tag'] == classification:
            return intent['responses']
        


# In[ ]:


st.title('Chatbot')
st.image('Chatbot_image.jpg')
user_input = st.text_input('You :')

#if user_input:
    #classification = classify_text(user_input)
    #response = get_response(classification)
    #st.success(response)
    
if user_input:
    classification = classify_text(user_input)
    st.write("Classification: ", classification)

