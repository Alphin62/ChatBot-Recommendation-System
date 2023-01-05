from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import streamlit as st

chatbot = ChatBot("My Chatbot")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations")


import json

with open('intents.json') as json_data:
    intents = json.load(json_data)

responses = {}

for intent in intents['intents']:
    responses[intent['tag']] = intent['responses']


st.title("My Chatbot")

while True:
    user_input = st.text_input("Enter your message:", key = "input")
    
    if user_input == "exit":
        break

    responses = chatbot.get_response(user_input)
    st.write("Chatbot : ", responses)

    for tag, response_list in responses.items():
        if str(responses) in response_list:
            st.write("Chatbot: ", random.choice(response_list))
            break

st.write("Chatbot: ", responses)
