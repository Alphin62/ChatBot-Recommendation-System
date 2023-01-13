import json
import streamlit as st
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

#from chatbot_model import *


st.title('_*Chatbot & Recommendation System*_')
st.image('Chatbot_image.jpg')

# Load the intents file
with open('intents.json') as json_data:
    intents = json.load(json_data)

model = RandomForestClassifier()

# Load the trained chatbot model
model.load('path/to/chatbot_model.pkl')


def classify_text(text):
    text = np.array([text])
    return model.predict(text)[0]


def get_response(classification):
    
    for intent in intents['intents']:
        if intent['tag'] == classification:
            return intent['responses']
        
user_input = st.text_input('You :')

#if user_input:
    #classification = classify_text(user_input)
    #response = get_response(classification)
    #st.success(response)
    
if user_input:
    classification = classify_text(user_input)
    st.write("Classification: ", classification)

