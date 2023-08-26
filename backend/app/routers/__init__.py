from .base_router import router as base_router
from .hugchat_router import router as hugchat_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(base_router)
router.include_router(hugchat_router)
