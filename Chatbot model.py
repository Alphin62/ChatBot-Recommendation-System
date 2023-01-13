import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import json


# Load the intents file
with open('intents.json') as json_data:
    intents = json.load(json_data)


# Get the patterns and the corresponding tags
patterns = []
tags = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])


# Perform text pre-processing
lemmatizer = WordNetLemmatizer()

# Perform text pre-processing
def pre_process(text):
    text = nltk.word_tokenize(text)
    text = [lemmatizer.lemmatize(token) for token in text]
    return text


# Create the TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(tokenizer=pre_process)

# Transform the patterns
X = tfidf_vectorizer.fit_transform(patterns)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, tags, test_size=0.2)

# Train the model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)


# Save the model
joblib.dump(model, 'chatbot_model.pkl')
