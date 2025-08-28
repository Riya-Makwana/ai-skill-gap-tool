from fastapi import FastAPI
from ingestion import router as ingestion_router
from diagnosis import router as diagnosis_router
from curriculum import router as curriculum_router
from prediction import router as prediction_router

app = FastAPI(title="AI Skill Gap Analysis Tool")

app.include_router(ingestion_router, prefix="/ingest", tags=["Ingestion"])
app.include_router(diagnosis_router, prefix="/diagnose", tags=["Diagnosis"])
app.include_router(curriculum_router, prefix="/curriculum", tags=["Curriculum"])
app.include_router(prediction_router, prefix="/progress", tags=["Prediction"])

@app.get("/")
def home():
    return {"message": "AI Skill Gap Analysis Tool Running 🚀"}
