import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Example dataset: attendance % + engagement score → pass/fail
# 0 = fail, 1 = pass
data = pd.DataFrame({
    "attendance": [40, 55, 60, 70, 75, 85, 90, 95],
    "engagement": [20, 35, 40, 55, 65, 70, 80, 90],
    "label":      [0,   0,   0,   1,   1,   1,   1,   1]
})

X = data[["attendance", "engagement"]]
y = data["label"]

# Train random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Ensure folder exists
output_dir = "saved_models"
os.makedirs(output_dir, exist_ok=True)

# Save model
joblib.dump(model, os.path.join(output_dir, "prediction_model.pkl"))
print("✅ Prediction model saved at models/saved_models/prediction_model.pkl")
