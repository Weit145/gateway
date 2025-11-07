from fastapi import APIRouter

from app.admin.router import post, profile, user

router = APIRouter()
router.include_router(post.router)
router.include_router(profile.router)
router.include_router(user.router)
