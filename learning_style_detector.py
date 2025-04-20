import pickle
from sklearn.ensemble import RandomForestClassifier

# Load pre-trained model
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

# Predict learning style based on interaction data
def predict_learning_style(data):
    model = load_model()
    prediction = model.predict([data])
    return prediction[0]
