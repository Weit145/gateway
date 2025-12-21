from abc import ABC, abstractmethod

from app.post.utils.schemas import OutPost, CreatePost, UpdatePost
from app.utils.schemas import UserCurrent


class IPostGateWay(ABC):
    @abstractmethod
    async def create_post_end_point(
        self, current_user: UserCurrent, new_post: CreatePost
    ) -> OutPost:
        pass

    @abstractmethod
    async def delete_postdb_by_id_end_point(
        self, current_user: UserCurrent, post_id: int
    ) -> None:
        pass

    @abstractmethod
    async def get_posts_end_point(self, limit: int, last_id: int) -> list[OutPost]:
        pass

    @abstractmethod
    async def get_by_id_post_end_point(self, post_id: int) -> OutPost:
        pass

    @abstractmethod
    async def get_by_user_id_post_end_point(
        self, username: str, id: int
    ) -> list[OutPost]:
        pass

    @abstractmethod
    async def update_post_end_point(
        self, current_user: UserCurrent, post_id: int, updated_post: UpdatePost
    ) -> OutPost:
        pass
