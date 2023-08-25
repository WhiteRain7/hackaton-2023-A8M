
from fastapi import APIRouter


router = APIRouter(prefix="/presentation", tags=["presentation"])

@router.post("/")
async def create_presentation():
    """Метод создания презентации"""
    return {}
