import grpc
from proto import auth_pb2, auth_pb2_grpc

from app.auth.grpc.iauth_service import IAuthService
from app.auth.utils.schemas import (
    UserCreate,
    Okey,
    Token,
    CookieResponse,
    AccessToken,
    UserLogin,
    UserBase,
    UserCurrent,
)
from app.auth.utils.converter import (
    convert_user_create_request,
    convert_okey_response,
    convert_token_request,
    convert_cookie_response,
    convert_cookie_request,
    convert_access_token_response,
    convert_user_login_request,
    convert_user_current_request,
    convert_user_current_response,
)


class AuthService(IAuthService):

    def __init__(self, host: str = "auth-service", port: int = 50051) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = auth_pb2_grpc.AuthStub(self.channel)

    async def create_user(self, user_create: UserCreate) -> Okey:
        request = convert_user_create_request(user_create)
        response = await self.stub.CreateUser(request)
        return convert_okey_response(response)

    async def registration_user(self, token: Token) -> CookieResponse:
        request = convert_token_request(token)
        response = await self.stub.RegistrationUser(request)
        return convert_cookie_response(response)

    async def refresh_token(self, refresh_token: str) -> AccessToken:
        request = convert_cookie_request(refresh_token)
        response = await self.stub.RefreshToken(request)
        return convert_access_token_response(response)

    async def authenticate_user(self, user_login: UserLogin) -> CookieResponse:
        request = convert_user_login_request(user_login)
        response = await self.stub.Authenticate(request)
        return convert_cookie_response(response)

    async def current_user(self, user: UserBase) -> UserCurrent:
        request = convert_user_current_request(user.username)
        response = await self.stub.CurrentUser(request)
        return convert_user_current_response(response)
    