import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Example dataset: student scores vs mastery
# 0 = needs improvement, 1 = good mastery
data = pd.DataFrame({
    "score": [10, 25, 40, 55, 65, 75, 85, 95],
    "label": [0, 0, 0, 0, 1, 1, 1, 1]
})

X = data[["score"]]
y = data["label"]

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Ensure folder exists
output_dir = "saved_models"
os.makedirs(output_dir, exist_ok=True)

# Save model
joblib.dump(model, os.path.join(output_dir, "diagnosis_model.pkl"))
print("✅ Diagnosis model saved at models/saved_models/diagnosis_model.pkl")
