#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import json

with open('intents.json','r') as f:
    intents = json.load(f)

# Create a list of input messages and corresponding categories
messages = []
tag = []
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        messages.append(pattern)
        tag.append(intent["tag"])

# Create a training dataset
df = pd.DataFrame({"message": messages, "tag": tag})

# Vectorize the messages using a bag-of-words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["message"])

# Train a support vector machine classifier
model = SVC()
model.fit(X, df["tag"])


# In[2]:


import pickle

# Save the trained model to a file
with open("chatbot_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Load the trained model from a file
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

# Use the model to classify an input message
classification = model.predict(vectorizer.transform(["Bye"]))
print(classification)  # Output: "greeting"


# In[ ]:




