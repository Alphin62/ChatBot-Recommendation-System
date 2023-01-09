#!/usr/bin/env python
# coding: utf-8

# In[4]:


import nltk
import numpy as np
import random
import json
import pickle

from nltk.stem import WordNetLemmatizer
from sklearn.svm import SVC

lemmatizer = WordNetLemmatizer()

# load the intents file
with open('intents.json') as inten:
    data = json.load(inten)

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
        docs_x.append(wrds)
        docs_y.append(intent['tag'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

# lemmatize and lower all the words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in '?']
words = sorted(list(set(words)))

# sort the labels
labels = sorted(labels)

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


# In[ ]:




