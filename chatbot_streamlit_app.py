import streamlit as st
from nltk.chat.util import Chat, reflections

st.title('_*Chatbot & Recommendation System*_')
st.image('Chatbot_image.jpg')
st.write("""
         ## About
         
         ### _*By Alphin Gnanaraj I*_
         """)
pairs = [    ["my name is (.*)", ["Hello %1, how are you today?"]],
    ["hi|hello|hey", ["Hello!", "Hi there!"]],
    ["what is your name?", ["My name is Chatty and I'm a chatbot!"]],
    ["how are you?", ["I'm doing great!"]],
    ["(.*) age?", ["I'm a computer program, so I don't have an age."]],
    ["(.*) (location|city)", ["I'm located in the cloud."]],
    ["(.*) (weather|temperature)", ["The weather is great!"]],
    ["(.*)", ["Sorry, I didn't understand you. Could you please rephrase your question?"]]
]

chatbot = Chat(pairs, reflections)

def chatbot_ui():
  message = st.text_input("Enter your message:")
  if message:
    response = chatbot.respond(message)
    st.write(f"Chatbot: {response}")

st.title("Chatbot")
chatbot_ui()
