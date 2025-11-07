from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/registration")

@router.post("/", status_code=status.HTTP_200_OK)
async def create_user_end_point(
    user: str,
) -> dict:
    return {"message": "Email send"}


@router.get("/confirm/",status_code=status.HTTP_200_OK)
async def registration_confirmation_end_point(
    token_pod: str = Query(..., description="Токен подтверждения регистрации"),
)->None:
    return 
