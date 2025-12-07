from typing import Annotated

from fastapi import APIRouter, Cookie, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.gateway.auth_gateway import AuthGateWay
from app.auth.utils.schemas import (
    Token,
    UserLogin,
)

router = APIRouter()

@router.get("/refresh/", status_code=status.HTTP_200_OK)
async def refresh_access_token_end_point(
    refresh_token: Annotated[str,Cookie(...)]
)->Token:
    return await AuthGateWay().refresh_token(refresh_token)


@router.post("/token/", status_code=status.HTTP_200_OK)
async def authenticate_user_end_point(
    form: OAuth2PasswordRequestForm = Depends(),
) -> JSONResponse:
    user_login = UserLogin(
        login = form.username,
        password = form.password,
    )
    return await AuthGateWay().authenticate_user(user_login)
