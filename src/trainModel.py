from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle
from dataset import df

# Create a model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model on the initial dataset
model.fit(df["question"], df["answer"])

# Save the model to a file
with open("qa_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Initial model trained and saved.")
