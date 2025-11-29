import grpc
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.auth.gateway.iauth_gateway import IAuthGateWay
from app.auth.grpc.auth_service import AuthService
from app.auth.utils.schemas import(
    UserCreate,
    Token,
    UserLogin,
    UserBase,
    UserCurrent,
)
from app.auth.utils.check import(
    check_code,
)
from app.auth.utils.converter import(
    converter_cookie,
)


class AuthGateWay(IAuthGateWay):


    async def create_user(self, user_create: UserCreate) -> None:
        try:
            response = await AuthService().create_user(user_create)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
    
    async def registration_user(self, token: Token) -> JSONResponse:
        try:
            response = await AuthService().registration_user(token)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        response_ready = converter_cookie(response)
        return response_ready
    
    async def refresh_token(self, refresh_token: str) -> Token:
        try:
            response = await AuthService().refresh_token(refresh_token)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        return Token(access_token=response.access_token)
    
    async def authenticate_user(self, user_login: UserLogin) -> JSONResponse:
        try:
            response = await AuthService().authenticate_user(user_login)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        response_ready = converter_cookie(response)
        return response_ready
    
    async def current_user(self, token: str) -> UserCurrent:
        try:
            response = await AuthService().current_user(token)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        return response