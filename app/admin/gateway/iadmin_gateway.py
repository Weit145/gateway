from abc import ABC, abstractmethod

from app.utils.schemas import UserCurrent

class IAdminGateWay(ABC):
    @abstractmethod
    async def delete_user_end_point(
        self,  current_admin: UserCurrent,  user_id: int
    )->None:
        pass

    @abstractmethod
    async def ban_user_end_point(
        self, current_admin: UserCurrent,  user_id: int
    )->None:
        pass

    @abstractmethod
    async def delete_post_end_point(
        self, current_admin: UserCurrent,  post_id: int
    )->None:
        pass