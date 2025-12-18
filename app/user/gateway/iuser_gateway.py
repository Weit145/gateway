from abc import ABC, abstractmethod

from app.utils.schemas import UserCurrent
from app.user.utils.schemas import UserUpdate, OutUser


class IUserGateWay(ABC):
    @abstractmethod
    async def delete_me_user_end_point(self, current_user: UserCurrent) -> None:
        pass

    @abstractmethod
    async def read_me_user_end_point(self, current_user: UserCurrent) -> OutUser:
        pass

    @abstractmethod
    async def update_me_end_point(
        self, current_user: UserCurrent, new_user: UserUpdate
    ) -> OutUser:
        pass
