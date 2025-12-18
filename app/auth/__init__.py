from fastapi import APIRouter

from app.auth.router import auth, registration

router = APIRouter()
router.include_router(registration.router)
router.include_router(auth.router)
