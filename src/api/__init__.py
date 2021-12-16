from fastapi import APIRouter

from src.api import question

router = APIRouter()

router.include_router(
    router=question.router, prefix="/question", tags=["questions"]
)
