from fastapi import APIRouter

from app.profile.router import profile

router = APIRouter()
router.include_router(profile.router)

