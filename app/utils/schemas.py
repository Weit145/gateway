from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr


class UserCurrent(BaseModel):
    id:int
    login:str
    is_active:bool
    is_verified:bool
    role:str
