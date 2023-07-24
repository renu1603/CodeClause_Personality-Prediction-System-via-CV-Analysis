import joblib
import pandas as pd
import pdfplumber

# Load the trained model for predicting Big Five scores
big_five_model = joblib.load('Train_models/trained_model.pkl')
vectorizer = joblib.load('Train_models/vectorizer.pkl')

personality_mapping = {
    0: 'Openness',
    1: 'Neuroticism',
    2: 'Conscientiousness',
    3: 'Agreeableness',
    4: 'Extraversion'
}

# Load the trained model for predicting final personality
final_personality_model = joblib.load('Train_models/final_personality_model.pkl')


def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def predict_personality_from_resume(resume):
    # Extract text from the PDF resume
    resume_text = extract_text_from_pdf(resume)
    resume_vectorized = vectorizer.transform([resume_text])
    personality_probs = big_five_model.predict_proba(resume_vectorized)[0]
    percentiles = pd.Series(personality_probs).rank(pct=True).values

    personality_dict = {
        personality_mapping[i]: round(percentile * 10, 2)  # Convert percentile to the range of 0 to 10
        for i, percentile in enumerate(percentiles)
    }
    return personality_dict


def predict_final_personality(personality_scores):
    # Convert personality scores to a DataFrame
    scores_df = pd.DataFrame([personality_scores])
    # print(scores_df)

    # Predict the final personality the score model
    predicted_personality = final_personality_model.predict(scores_df)[0]

    return predicted_personality


add_resume = "Resume/Aksh_CV.pdf"
predicted_personality_scores = predict_personality_from_resume(add_resume)
# print(predicted_personality_scores)
print("Predicted Big Five Personality Scores:")
for trait, score in predicted_personality_scores.items():
    print(f"{trait}: {score}")

predicted_final_personality = predict_final_personality(predicted_personality_scores)
print("Predicted Final Personality:", predicted_final_personality)
