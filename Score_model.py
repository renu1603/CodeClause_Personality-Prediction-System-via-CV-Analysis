import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Read the data from CSV file
df = pd.read_csv('Score.csv')

# Verify if 'Final Personality' column exists in the DataFrame
if 'Personality' not in df.columns:
    print("Error: 'Final Personality' column not found in the CSV file.")
    print("Please ensure that the column name matches the header in the CSV file.")
    exit()

# Separate the scores (features) and final personality (target variable)
X = df.iloc[:, :-1]
y = df['Personality']
# print(X, y)

# Train a random forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X, y)

# Save the trained model
joblib.dump(clf, 'final_personality_model.pkl')

print("Model training completed. The trained model is saved as 'final_personality_model.pkl'.")
