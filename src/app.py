import pickle
from dataset import df

# Load the model
with open("qa_model.pkl", "rb") as f:
    model = pickle.load(f)


# Function to predict or save new data for retraining
def answer_question(question):
    prediction = model.predict([question])[0]
    confidence = max(model.predict_proba([question])[0])
    if confidence < 0.3:  # Adjust based on your needs
        print("I don't know the answer to that question.")
        new_answer = input("Please provide the correct answer, and I will learn it: ")
        df.loc[len(df)] = [question, new_answer]  # Add to dataset
        retrain_model()
        return new_answer
    else:
        return prediction


def retrain_model():
    global model
    model.fit(df["question"], df["answer"])
    with open("qa_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model retrained with new data.")


# Test the function
question = input("enter the question:")
print(answer_question(question))
