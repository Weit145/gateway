from abc import ABC, abstractmethod

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

class IAuthService(ABC):
    
    @abstractmethod
    def __init__(self, host: str, port: int)->None:
        pass

    @abstractmethod
    async def create_user(self, user_create:UserCreate)->Okey:
        pass

    @abstractmethod
    async def registration_user(self, token:Token)->CookieResponse:
        pass

    @abstractmethod
    async def refresh_token(self, refresh_token:str)->AccessToken:
        pass

    @abstractmethod
    async def authenticate_user(self,user_login:UserLogin)->CookieResponse:
        pass

    @abstractmethod
    async def current_user(self,token:str)->UserCurrent:
        pass