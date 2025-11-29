from abc import ABC, abstractmethod
from fastapi.responses import JSONResponse

from app.auth.utils.schemas import(
    UserCreate,
    Token,
    UserLogin,
    UserBase,
    UserCurrent,
)

class IAuthGateWay(ABC):

    @abstractmethod
    async def create_user(self, user_create:UserCreate)->None:
        pass

    @abstractmethod
    async def registration_user(self, token:Token)->JSONResponse:
        pass

    @abstractmethod
    async def refresh_token(self, refresh_token:str)->Token:
        pass

    @abstractmethod
    async def authenticate_user(self, user_login:UserLogin)->JSONResponse:
        pass

    @abstractmethod
    async def current_user(self,token:str)->UserCurrent:
        pass