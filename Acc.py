import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
import joblib

# Loading the data from CSV
data = pd.read_csv('Dataset/test_dataset.csv')

# Separate The data from dataset ( resume_text and personality )
X = data['resume_text']
Y = data['personality']
# print(X, "\n",  y_true)

# Load the trained model
big_five_model = joblib.load('Train_models/trained_model.pkl')

# Load the TF-IDF vectorizer
vectorizer = joblib.load('Train_models/vectorizer.pkl')

# Vectorize the text data
X_vectorized = vectorizer.transform(X)
# print(X_vectorized)

# Make predictions on the vectorized features
y_test = big_five_model.predict(X_vectorized)
# print(y_test)

# Calculate the accuracy score
accuracy = accuracy_score(Y, y_test)

print("Accuracy:", accuracy)
