import pickle
from sklearn.ensemble import RandomForestClassifier
from data_preprocessing import preprocess_data

# Train and save model
def train_model(data_path):
    X_train, _, y_train, _ = preprocess_data(data_path)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    train_model("data/interactions.csv")
