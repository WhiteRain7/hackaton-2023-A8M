from .base_router import router as base_router
from .hugchat_router import router as hugchat_router
from .chekko_router import router as chekko_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(base_router)
router.include_router(hugchat_router)
router.include_router(chekko_router)
