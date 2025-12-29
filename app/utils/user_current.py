from typing import Annotated
from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer

from app.auth.gateway.auth_gateway import AuthGateWay
from app.utils.schemas import UserCurrent
from app.utils.converter import converter_UserCurrent

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token/")


async def get_current_user(
    login: Annotated[str, Depends(oauth2_scheme)],
) -> UserCurrent:
    response = await AuthGateWay().current_user(login)
    return converter_UserCurrent(response)

async def get_admin_user(
    login:Annotated[str, Depends(oauth2_scheme)],
)-> UserCurrent:
    response = await AuthGateWay().current_user(login)
    if response.role != "admin":
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Not allowed")
    return converter_UserCurrent(response)