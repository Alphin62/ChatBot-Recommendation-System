#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing necessary libraries

import numpy as np
import json
import random
import pickle
import warnings
warnings.filterwarnings('ignore')

# import library for charbot

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.optimizers import legacy

#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('omw-1.4')

# library for model training

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


# In[2]:


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?','!','.',',']


# In[3]:


for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
print(documents)


# In[4]:


words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
words = sorted(set(words))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl','wb'))
pickle.dump(classes, open('classes.pkl','wb'))


# In[5]:


training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
        
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
    
random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])


# In[6]:


# deploying tensorflow.keras model

model = Sequential()
model.add(Dense(128, input_shape = (len(train_x[0]), ), activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = 'softmax'))

sgd = legacy.SGD(learning_rate = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)

model.compile(loss = 'categorical_crossentropy', optimizer = sgd, metrics = ['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs = 200, batch_size = 5, verbose = 1)
model.save('Chatbot_Model.h5', hist)


# In[ ]:




