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
    check_response,
)
from app.auth.utils.converter import(
    converter_cookie,
)


class AuthGateWay(IAuthGateWay):


    async def create_user(self, user_create: UserCreate) -> None:
        response = await AuthService().create_user(user_create)
        check_response(response)
        return
    
    async def registration_user(self, token: Token) -> JSONResponse:
        response = await AuthService().registration_user(token)
        check_response(response)
        response_ready = converter_cookie(response)
        return response_ready
    
    async def refresh_token(self, refresh_token: str) -> Token:
        response = await AuthService().refresh_token(refresh_token)
        check_response(response)
        return Token(access_token=response.access_token)
    
    async def authenticate_user(self, user_login: UserLogin) -> JSONResponse:
        response = await AuthService().authenticate_user(user_login)
        check_response(response)
        response_ready = converter_cookie(response)
        return response_ready
    
    async def current_user(self, token: str) -> UserCurrent:
        response = await AuthService().current_user(token)
        check_response(response)
        return response