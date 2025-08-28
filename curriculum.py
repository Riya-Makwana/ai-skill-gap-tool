from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def curriculum(data: dict):
    # Dummy curriculum plan
    return {
        "objectives": [
            {"id": "obj1", "skill_id": "math.fractions", "target_score": 0.8}
        ],
        "activities": [
            {"id": "act1", "label": "Practice Fractions", "estimated_minutes": 30, "skill_refs": ["math.fractions"]}
        ],
        "rationale": "Student needs improvement in fractions"
    }
