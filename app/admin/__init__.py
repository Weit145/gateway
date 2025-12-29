from fastapi import APIRouter

from app.admin.router import post, user

router = APIRouter()
router.include_router(post.router)
router.include_router(user.router)
