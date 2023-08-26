from fastapi import APIRouter, Depends, Body
from ..service.hugchat_service import HugChatSevice

router = APIRouter(prefix="/hugchat", tags=["ai"])


@router.post("/", response_model=str)
async def create_presentation(value: str = Body(), service=Depends(HugChatSevice)):
    """Метод вызова генеративной сети (hugingface chat) по апи"""
    return service.call_api_hugchat(value)
