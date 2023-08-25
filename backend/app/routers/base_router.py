
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from ..service.base_service import BaseSevice

router = APIRouter(prefix="/presentation", tags=["presentation"])

@router.post("/", response_class=FileResponse)
async def create_presentation(
    service = Depends(BaseSevice)
):
    """Метод создания презентации"""
    return await service.create_presentation()
