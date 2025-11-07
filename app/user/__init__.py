from fastapi import APIRouter

from app.user.router import user

router = APIRouter()
router.include_router(user.router)
