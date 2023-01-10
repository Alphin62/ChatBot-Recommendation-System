import json
import nltk
from nltk.tokenize import word_tokenize
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the intents.json file
with open("intents.json") as file:
    intents = json.load(file)

# Extract the patterns and responses from the intents
patterns = []
responses = []
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        responses.append(intent["responses"])

# Preprocess the patterns using a CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, responses, test_size=0.2)

# Train a logistic regression model on the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

# Define a function to get the response for a user input
def get_response(user_input):
    user_input = word_tokenize(user_input)
    user_input = vectorizer.transform([user_input])
    prediction = model.predict(user_input)[0]
    return prediction

if __name__ == '__main__':
    st.title("Chatbot")
    st.text("Type something to start the conversation")
    user_input = st.text_input("")
    if user_input:
        response = get_response(user_input)
        st.success(response)
