import streamlit as st
import pickle
import nltk
import numpy as np
import json
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
lemmatizer = WordNetLemmatizer()

# load the model from file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# load the intents file
with open('intents.json') as file:
    data = json.load(file)

# get a list of words from each intent
words = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        # lemmatize the words and remove duplicates
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        labels.append(intent['tag'])

# lemmatize and lower all the words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in '?']
words = sorted(list(set(words)))

# sort the labels
labels = sorted(labels)

def bag_of_words(sentence, words):
    # lemmatize and lower the words in the sentence
    sentence_words = [lemmatizer.lemmatize(w.lower()) for w in nltk.word_tokenize(sentence)]

    bag = [0 for _ in range(len(words))]

    for sw in sentence_words:
        for i, w in enumerate(words):
            if w == sw:
                bag[i] = 1
            
    return bag

def classify(sentence, words):
    # generate probability from the model
    prob_result = model.predict_proba(np.array([bag_of_words(sentence, words)]))[0]
    index = np.argmax(prob_result)
    tag = labels[index]

    if prob_result[index] > 0.7:
        for tg in data['intents']:
            if tg['tag'] == tag:
                responses = tg['responses']
        return random.choice(responses)

st.title("Intent Classifier")

sentence = st.text_input("Enter a sentence:")

if sentence:
    response = classify(sentence, words)

    if response:
        st.success(f"Response: {response}")
    else:
        st.error("Unable to classify the intent with high confidence. Please try a different sentence.")
