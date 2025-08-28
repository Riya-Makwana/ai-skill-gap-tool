from fastapi import APIRouter
import joblib
import os

router = APIRouter()

# Load trained diagnosis model
MODEL_PATH = os.path.join("..", "models", "saved_models", "diagnosis_model.pkl")
diagnosis_model = joblib.load(MODEL_PATH)

@router.post("/")
def diagnose(data: dict):
    """
    Example request:
    { "score": 75 }
    """
    score = [[data.get("score", 50)]]
    prediction = diagnosis_model.predict(score)[0]

    severity = "low" if prediction == 1 else "high"

    return {
        "mastery_vector": [{"skill_id": "math.fractions", "score": float(score[0][0] / 100)}],
        "gaps": [{"skill_id": "math.fractions", "severity": severity}]
    }
