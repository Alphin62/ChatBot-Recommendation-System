import json
import streamlit as st

# Load intents data from json file
with open('intents.json') as f:
    intents = json.loads(f.read())

# Define a function to handle chatbot interactions

def chatbot():
    
    st.title("_*My Chatbot & Recommendation System*_")
    st.image('Chatbot_image.jpg') 
    st.write("""
         ## About
         A chatbot is a computer program that is designed to simulate conversation with human users. It uses natural language processing (NLP) and machine learning (ML) technologies to understand and respond to user inputs. Chatbots can be integrated into various platforms such as websites, mobile apps, and messaging apps, and can be used to perform a wide range of tasks such as answering questions, providing customer support, and even completing transactions. They are becoming increasingly popular as they can save time and resources for businesses and provide 24/7 availability for users. Essentially, chatbot is a computer program that can chat with people in a way similar to a human conversation.
         
         ##### Rule Based Approach : 
         A rule-based chatbot is a type of computer program that uses pre-defined rules to determine how to respond to users' inputs based on keywords or phrases, it's a simple chatbot that can handle a limited set of tasks and can't understand more complex or nuanced inputs.
         
         _**By Alphin Gnanaraj I**_
         """)
    
    user_input = st.text_input("Type your text below")
        # Loop through intents to find a match
        
    for intent in intents:
        if user_input in intent["inputs"]:
            st.write(intent["response"])
            return
        
        # If no match is found
    st.write("Sorry, I didn't understand your input.")        
   
        
# Run the Streamlit app
if __name__ == "__main__":
    chatbot()
