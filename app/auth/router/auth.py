from typing import Annotated

from fastapi import APIRouter, Cookie, Depends, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/refresh/", status_code=status.HTTP_200_OK)
async def refresh_access_token_end_point(
    refresh_token: Annotated[str,Cookie(...)]
)->None:
    return

@router.post("/token/", status_code=status.HTTP_200_OK)
async def authenticate_user_end_point(
    user: str,
) -> None:
    return 
