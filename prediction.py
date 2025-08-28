from fastapi import APIRouter
import joblib
import os

router = APIRouter()

# Load trained prediction model
MODEL_PATH = os.path.join("..", "models", "saved_models", "prediction_model.pkl")
prediction_model = joblib.load(MODEL_PATH)

@router.post("/")
def predict(data: dict):
    """
    Example request:
    { "attendance": 85, "engagement": 70 }
    """
    X = [[data.get("attendance", 70), data.get("engagement", 50)]]
    prob = prediction_model.predict_proba(X)[0][1]

    if prob > 0.85:
        band = "A"
    elif prob > 0.7:
        band = "B"
    elif prob > 0.5:
        band = "C"
    else:
        band = "D"

    return {
        "subject": "Math",
        "horizon_days": 30,
        "prob_pass": round(float(prob), 2),
        "band": band
    }
