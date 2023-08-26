from fastapi import APIRouter, Depends
from ..service.chekko_service import ChekkoService

router = APIRouter(prefix="/info", tags=["chekko"])


@router.get("/")
async def get_dop_info(ogrn: str, service=Depends(ChekkoService)):
    """Метод создания презентации"""
    return await service.get_dop_info(ogrn)
