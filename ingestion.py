from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def ingest(data: dict):
    # Example: count student responses
    return {"status": "success", "records": len(data.get("responses", []))}
