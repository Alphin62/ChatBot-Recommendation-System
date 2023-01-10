import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import streamlit as st

# Create a new chat bot
bot = ChatBot("Streamlit Bot")

# Load the intents file
with open("intents.json") as file:
    intents = json.load(file)

# Create a list of responses for each intent
responses = []
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        responses.append(pattern)
    for response in intent["responses"]:
        responses.append(response)

# Train the bot with the responses
bot.set_trainer(ListTrainer)
bot.train(responses)

st.title("Chatbot")

user_input = st.text_input("Your message:")

if user_input:
    response = bot.get_response(user_input)
    st.write("Bot:", response)
