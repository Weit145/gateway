from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from app.auth.gateway.auth_gateway import AuthGateWay

from app.auth.utils.schemas import(
    UserCreate,
    Token,
)

router = APIRouter(prefix="/registration")

@router.post("/", status_code=status.HTTP_200_OK)
async def create_user_end_point(
    user_create: UserCreate,
) -> dict:
    await AuthGateWay().create_user(user_create)
    return {"message": "Email send"}


@router.get("/confirm/",status_code=status.HTTP_200_OK)
async def registration_confirmation_end_point(
    token_pod: str = Query(..., description="Токен подтверждения регистрации"),
)->JSONResponse:
    return await AuthGateWay().registration_user(Token(access_token=token_pod))
