import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st

# Load the intents file
with open('intents.json') as file:
    intents = json.load(file)

# Create a list of texts and a list of corresponding labels
texts = []
labels = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(intent['tag'])

# Create a feature vector using the CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Create a random forest classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, labels)

# Define the main function
def main():
    st.title("My Chatbot & Recommendation")
    message = st.text_input("Enter your message:")
    if st.button('Send'):
        # Use the classifier to predict the label for the input message
        pred = clf.predict(vectorizer.transform([message]))
        st.success(f'Bot : {pred[0]}')

if __name__=='__main__':
    main()
