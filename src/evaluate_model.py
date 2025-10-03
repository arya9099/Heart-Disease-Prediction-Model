import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Load test dataset
df = pd.read_csv("../data/heart_dataset.csv")
X = df.drop(columns=["target"])
y = df["target"]

# Load model and scaler
model = pickle.load(open("../models/model.pkl", "rb"))
scaler = pickle.load(open("../models/scaler.pkl", "rb"))

# Scale features
X_scaled = scaler.transform(X)

# Evaluate
y_pred = model.predict(X_scaled)
print("Accuracy:", accuracy_score(y, y_pred))
print("\nClassification Report:\n", classification_report(y, y_pred))
