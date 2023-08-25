from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import router
from .config import settings


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
)

app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)