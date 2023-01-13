import json
import streamlit as st

# Load intents data from json file
with open('intents.json') as f:
    intents = json.loads(f.read())

# Define a function to handle chatbot interactions

def chatbot():
    
    st.title("_*My Chatbot & Recommendation System*_")
    st.image('Chatbot_image.jpg')
    
    user_input = st.text_input("Type your text below")
        # Loop through intents to find a match
        
    for intent in intents:
        if user_input in intent["inputs"]:
            st.write(intent["response"])
            return
        
        # If no match is found
    st.write("Shalz: Sorry, I didn't understand your input.")        
        
        
# Run the Streamlit app
if __name__ == "__main__":
    chatbot()
