from abc import ABC, abstractmethod

from app.user.utils.schemas import (
    OutUser,
    UserUpdate,
)
from app.utils.schemas import UserCurrent

class IUserService(ABC):

    @abstractmethod
    def __init__(self, host: str, port: int) -> None:
        pass

    @abstractmethod
    async def delete_me_user_end_point(self, current_user: UserCurrent) -> None:
        pass

    @abstractmethod
    async def read_me_user_end_point(self, current_user: UserCurrent) -> OutUser:
        pass
        
    @abstractmethod
    async def update_me_end_point(self, current_user: UserCurrent, new_user: UserUpdate) -> OutUser:
        pass