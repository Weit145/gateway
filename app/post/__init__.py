from fastapi import APIRouter

from app.post.router import post

router = APIRouter()
router.include_router(post.router)
