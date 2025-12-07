from abc import ABC, abstractmethod

from app.post.utils.schemas import(
    OutPost,
    CreatePost,
    UpdatePost,
)
from app.utils.schemas import UserCurrent

class IPostService(ABC):

    @abstractmethod
    def __init__(self, host: str, port: int) -> None:
        pass

    @abstractmethod
    async def create_post_end_point(self, current_user: UserCurrent, new_post: CreatePost) -> OutPost:
        pass

    @abstractmethod
    async def delete_postdb_by_id_end_point(self, current_user: UserCurrent, post_id: int) -> None:
        pass

    @abstractmethod
    async def get_posts_end_point(self, group_post_id: int) -> list[OutPost]:
        pass

    @abstractmethod
    async def get_by_id_post_end_point(self, post_id: int) -> OutPost:
        pass

    @abstractmethod
    async def get_by_username_post_end_point(self, username: str) -> list[OutPost]:
        pass

    @abstractmethod
    async def update_post_end_point(self, current_user: UserCurrent, post_id: int, updated_post: UpdatePost) -> OutPost:
        pass