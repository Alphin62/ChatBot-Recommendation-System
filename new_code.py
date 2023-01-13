import json
import streamlit as st

# Load intents data from json file
with open('intents.json') as f:
    intents = json.loads(f.read())

# Define a function to handle chatbot interactions
def chatbot():
    st.set_page_config(page_title="My Chatbot", page_icon=":guardsman:", layout="wide")
    st.title("My Chatbot")
    user_input = st.text_input("What can I help you with?")
    if st.button("Submit"):
        # Loop through intents to find a match
        for intent in intents:
            if user_input in intent["inputs"]:
                st.write(intent["response"])
                return
        # If no match is found
        st.write("I'm sorry, I didn't understand your input.")

# Run the Streamlit app
if __name__ == "__main__":
    chatbot()
