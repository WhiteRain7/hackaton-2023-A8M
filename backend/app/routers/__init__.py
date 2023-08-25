from .base_router import router as base_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(base_router)
