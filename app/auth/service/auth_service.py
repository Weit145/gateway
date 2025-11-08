import grpc
from proto import auth_pb2, auth_pb2_grpc

from app.auth.service.iauth_service import IAuthService

from app.auth.utils.schemas import(
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

    def __init__(self, host: str = "localhost", port: int = 50051) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = auth_pb2_grpc.AuthStub(self.channel)

    async def create_user(self, user_create: UserCreate) -> Okey:
        request = auth_pb2.UserCreateRequest(
            username = user_create.username,
            email = user_create.email,
            password = user_create.password
            )
        response = await self.stub.CreateUser(request)
        return Okey(success = response.success, status_code=response.status_code,error = response.error)
    
    async def registration_user(self, token: Token) -> CookieResponse:
        request = auth_pb2.TokenRequest(
            token_pod=token.access_token
        )
        response = await self.stub.RegistrationUser(request)
        cookie_pb = response.cookie  # auth_pb2.Cookie
        okey_pb = response.response
        return CookieResponse(
            access_token=response.access_token,
            key=cookie_pb.key,
            value=cookie_pb.value,
            httponly=cookie_pb.httponly,
            secure=cookie_pb.secure,
            samesite=cookie_pb.samesite,
            max_age=cookie_pb.max_age,
            success=okey_pb.success,
            status_code=okey_pb.status_code,
            error=okey_pb.error
        )

    
    async def refresh_token(self, refresh_token: str) -> AccessToken:
        request = auth_pb2.CookieRequest(
            refresh_token = refresh_token,
        )

        response = await self.stub.RefreshToken(request)
        okey_pb = response.response
        return AccessToken(
            access_token = response.access_token,
            success = okey_pb.success,
            status_code = okey_pb.status_code,
            error = okey_pb.error
        )
    
    async def authenticate_user(self, user_login: UserLogin) -> CookieResponse:
        request = auth_pb2.UserLoginRequest(
            username = user_login.username,
            password = user_login.password,
        )
        response = await self.stub.Authenticate(request)
        cookie_pb = response.cookie  # auth_pb2.Cookie
        okey_pb = response.response
        return CookieResponse(
            access_token=response.access_token,
            key=cookie_pb.key,
            value=cookie_pb.value,
            httponly=cookie_pb.httponly,
            secure=cookie_pb.secure,
            samesite=cookie_pb.samesite,
            max_age=cookie_pb.max_age,
            success=okey_pb.success,
            status_code=okey_pb.status_code,
            error=okey_pb.error
        )
    
    async def current_user(self, user: UserBase) -> UserCurrent:
        request = auth_pb2.UserCurrentRequest(
            username = user.username,
        )
        response = await self.stub.CurrentUser(request)
        okey_pb = response.response
        return UserCurrent(
            id = response.id,
            username = response.username,
            is_active = response.is_active,
            is_verified = response.is_verified,
            role = response.role,
            success=okey_pb.success,
            status_code = okey_pb.status_code,
            error=okey_pb.error
        )
