import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Loading the training data from my CSV file
df = pd.read_csv('Dataset/test_dataset.csv')

# Separate data
texts = df['resume_text']
labels = df['personality']
# print(texts, labels)

vectorizer = TfidfVectorizer()
train_features = vectorizer.fit_transform(texts)
print(train_features)

# Training RFC model
clf = RandomForestClassifier()
clf.fit(train_features, labels)

# Saving the model using JOBLIB
joblib.dump(clf, 'Train_models/trained_model.pkl')

# Save the vectorizer as a pikl file
joblib.dump(vectorizer, 'Train_models/vectorizer.pkl')

print('model saved successfully')
