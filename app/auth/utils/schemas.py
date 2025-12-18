from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel


class UserBase(BaseModel):
    login: Annotated[str, MinLen(4), MaxLen(32)]


class Cookie(BaseModel):
    key: str
    value: str
    httponly: bool
    secure: bool
    samesite: str
    max_age: int


class UserCreate(UserBase):
    username: Annotated[str, MinLen(4), MaxLen(32)]
    email: str
    password: str


class UserLogin(UserBase):
    password: str


class Token(BaseModel):
    access_token: str


class Okey(BaseModel):
    success: bool


class CookieResponse(Cookie):
    access_token: str


class AccessToken(Token):
    pass


class UserCurrent(BaseModel):
    id: int
    login: str
    is_active: bool
    is_verified: bool
    role: str
