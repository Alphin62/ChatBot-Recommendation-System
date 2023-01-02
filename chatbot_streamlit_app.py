import streamlit as st
import json
import pickle
import chatbot

# Load the intents file
with open("intents.json", "r") as f:
    intents = json.load(f)

# Load the trained model from a file
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

def chatbot_ui():
    message = st.text_input("Enter your message:")
    if message:
        response = chatbot.get_response(message, model, intents)
        st.write(f"Chatbot: {response}")

st.title("Chatbot")
chatbot_ui()

def get_response(message, model, intents):
    # Use the model to predict the class of the input message
    classification = model.predict(message)

    # Loop through the intents and find the matching response
    for intent in intents["intents"]:
        if intent["tag"] == classification:
            return random.choice(intent["responses"])
    
    # Return a default response if no matching intent is found
    return "I'm sorry, I didn't understand your message."
