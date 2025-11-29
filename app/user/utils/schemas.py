from typing import Annotated

from annotated_types import MaxLen, MinLen
from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: Annotated[str, MinLen(6), MaxLen(32)]


class UserUpdate(UserBase):
    pass

class OutUser(UserBase):
    pass


