import json
import streamlit as st
from sklearn.externals import joblib


# Load the intents file
with open('intents.json') as json_data:
    intents = json.load(json_data)
    
# Load the trained chatbot model
model = joblib.load('chat_model.pkl')



def classify_text(text):
    
    return model.predict([text])[0]

def get_response(classification):
    
    for intent in intents['intents']:
        if intent['tag'] == classification:
            return intent['responses']
        

st.title('Chatbot')

user_input = st.text_input('You :')

if user_input:
    classification = classify_text(user_input)
    response = get_response(classification)
    st.success(response)
