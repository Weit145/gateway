import grpc
from proto import post_pb2_grpc
from app.utils.schemas import UserCurrent

from app.post.grpc.ipost_service import IPostService
from app.post.utils.schemas import (
    OutPost,
    CreatePost,
    UpdatePost,
)

from app.post.utils.converter import (
    converter_user_create_request,
    converter_user_delete_request,
    converter_user_get_posts_request,
    converter_user_get_by_id_request,
    converter_user_get_by_auth_request,
    converter_user_update_request,
    converter_OutPost,
    converter_list_OutPost,
)


class PostService(IPostService):
    def __init__(self, host: str = "post-service", port: int = 50054) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = post_pb2_grpc.PostStub(self.channel)

    async def create_post_end_point(
        self, current_user: UserCurrent, new_post: CreatePost
    ) -> OutPost:
        request = converter_user_create_request(current_user, new_post)
        response = await self.stub.CreatePost(request)
        return converter_OutPost(response)

    async def delete_postdb_by_id_end_point(
        self, current_user: UserCurrent, post_id: int
    ) -> None:
        request = converter_user_delete_request(current_user, post_id)
        await self.stub.DeletePost(request)

    async def get_posts_end_point(self, limit: int, last_id: int) -> list[OutPost]:
        request = converter_user_get_posts_request(limit, last_id)
        response = await self.stub.GetGroupPost(request)
        return converter_list_OutPost(response)

    async def get_by_id_post_end_point(self, post_id: int) -> OutPost:
        request = converter_user_get_by_id_request(post_id)
        response = await self.stub.GetByIdPost(request)
        return converter_OutPost(response)

    async def get_by_username_post_end_point(self, username: str, id) -> list[OutPost]:
        request = converter_user_get_by_auth_request(username, id)
        response = await self.stub.GetByIdUserPost(request)
        return converter_list_OutPost(response)

    async def update_post_end_point(
        self, current_user: UserCurrent, post_id: int, updated_post: UpdatePost
    ) -> OutPost:
        request = converter_user_update_request(current_user, post_id, updated_post)
        response = await self.stub.PutPost(request)
        return converter_OutPost(response)
