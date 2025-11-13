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


class AuthService(IAuthService):

    def __init__(self, host: str = "auth-service", port: int = 50051) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = auth_pb2_grpc.AuthStub(self.channel)

    async def create_user(self, user_create: UserCreate) -> Okey:
        request = auth_pb2.UserCreateRequest(
            username=user_create.username,
            email=user_create.email,
            password=user_create.password
        )
        response = await self.stub.CreateUser(request)
        return Okey(
            success=response.success,
            status_code=response.status_code,
            error=response.error
        )

    async def registration_user(self, token: Token) -> CookieResponse:
        request = auth_pb2.TokenRequest(token_pod=token.access_token)
        response = await self.stub.RegistrationUser(request)
        return CookieResponse(
            access_token=response.access_token,
            key=response.cookie.key,
            value=response.cookie.value,
            httponly=response.cookie.httponly,
            secure=response.cookie.secure,
            samesite=response.cookie.samesite,
            max_age=response.cookie.max_age,
            success=response.response.success,
            status_code=response.response.status_code,
            error=response.response.error
        )

    async def refresh_token(self, refresh_token: str) -> AccessToken:
        request = auth_pb2.CookieRequest(refresh_token=refresh_token)
        response = await self.stub.RefreshToken(request)
        return AccessToken(
            access_token=response.access_token,
            success=response.response.success,
            status_code=response.response.status_code,
            error=response.response.error
        )

    async def authenticate_user(self, user_login: UserLogin) -> CookieResponse:
        request = auth_pb2.UserLoginRequest(
            username=user_login.username,
            password=user_login.password
        )
        response = await self.stub.Authenticate(request)
        return CookieResponse(
            access_token=response.access_token,
            key=response.cookie.key,
            value=response.cookie.value,
            httponly=response.cookie.httponly,
            secure=response.cookie.secure,
            samesite=response.cookie.samesite,
            max_age=response.cookie.max_age,
            success=response.response.success,
            status_code=response.response.status_code,
            error=response.response.error
        )

    async def current_user(self, user: UserBase) -> UserCurrent:
        request = auth_pb2.UserCurrentRequest(username=user.username)
        response = await self.stub.CurrentUser(request)
        return UserCurrent(
            id=response.id,
            username=response.username,
            is_active=response.is_active,
            is_verified=response.is_verified,
            role=response.role,
            success=response.response.success,
            status_code=response.response.status_code,
            error=response.response.error
        )
    
#     import grpc
# from proto import auth_pb2, auth_pb2_grpc

# async def serve():
#     server = grpc.aio.server()
#     auth_pb2_grpc.add_AuthServicer_to_server(AuthService(), server)
#     server.add_insecure_port('[::]:50051')
#     print("gRPC сервер запущен на порту 50051...")
#     await server.start()
#     await server.wait_for_termination()