import streamlit as st
import pickle
import nltk
import numpy as np
import json
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()

# load the intents file
with open('intents.json') as file:
    data = json.load(file)

# get a list of words from each intent
words = []
labels = []
docs_x = []
docs_y = []

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

# create a training and testing data set
training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []

    wrds = [lemmatizer.lemmatize(w) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

# convert the training and output data sets to numpy arrays
training = np.array(training)
output = np.array(output)

# create the model
model = SVC(kernel='linear', probability=True)

# fit the model to the training data
model.fit(training, np.argmax(output, axis=1))

# save the model to file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# load the model from file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

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

st.title("Chatbot & Recommendation")

sentence = st.text_input("Enter a sentence:")

if sentence:
    response = classify(sentence, words)

    if response:
        st.success(f"Response: {response}")
    else:
        st.error("Unable to classify the intent with high confidence. Please try a different sentence.")
