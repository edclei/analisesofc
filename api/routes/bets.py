
from fastapi import APIRouter
router = APIRouter()

@router.post("/place")
def place_bet(payload: dict):
    return {"status":"ok","payload": payload}
