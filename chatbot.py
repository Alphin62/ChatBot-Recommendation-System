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
counter = 0

while True:
    user_input = st.text_input(f"Enter your message {counter}:", key=f'input{counter}')
    
    if user_input == "exit":
        break
    counter += 1

    response = chatbot.get_response(user_input)
    st.write("Chatbot: ", response)

    # Check if the response is in our intents and use the pre-defined response if it is
    for tag, response_list in responses.items():
        if str(response) in response_list:
            st.write("Chatbot: ", random.choice(response_list))
            break
