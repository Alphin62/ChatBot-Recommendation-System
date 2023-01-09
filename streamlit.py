import streamlit as st
import pickle
import nltk
import numpy as np
import json
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

import warnings
warnings.filterwarnings('ignore')


# load the model from file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# load the intents file
with open('intents.json') as file:
    data = json.load(file)


def bag_of_words(sentence, words):
    # lemmatize and lower the words in the sentence
    sentence_words = [lemmatizer.lemmatize(w.lower()) for w in nltk.word_tokenize(sentence)]

    bag = [0 for _ in range(len(words))]

    for sw in sentence_words:
        for i, w in enumerate(words):
            if w == sw:
                bag[i] = 1
            
    return bag

st.title("Intent Classifier")

sentence = st.text_input("Enter a sentence:")

if sentence:
    prob_result = model.predict_proba(np.array([bag_of_words(sentence, words)]))[0]
    index = np.argmax(prob_result)
    tag = labels[index]
    probability = prob_result[index]

    if probability > 0.7:
        for tg in data['intents']:
            if tg['tag'] == tag:
                responses = tg['responses']
        st.success(f"Intent: {tag} ({probability:.2f})\n\nResponse: {random.choice(responses)}")
    else:
        st.error("Unable to classify the intent with high confidence. Please try a different sentence.")
