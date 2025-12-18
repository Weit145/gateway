from pydantic import BaseModel


class UserCurrent(BaseModel):
    id: int
    login: str
    is_active: bool
    is_verified: bool
    role: str
