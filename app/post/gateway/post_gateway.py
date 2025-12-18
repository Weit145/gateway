import grpc
from fastapi import HTTPException
from app.post.gateway.ipost_gateway import IPostGateWay
from app.post.grpc.post_service import PostService
from app.utils.schemas import UserCurrent
from app.post.utils.schemas import (
    OutPost,
    CreatePost,
    UpdatePost,
)
from app.utils.check import (
    check_code,
)


class PostGateWay(IPostGateWay):
    async def create_post_end_point(
        self, current_user: UserCurrent, new_post: CreatePost
    ) -> OutPost:
        try:
            response = await PostService().create_post_end_point(current_user, new_post)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response

    async def delete_postdb_by_id_end_point(
        self, current_user: UserCurrent, post_id: int
    ) -> None:
        try:
            await PostService().delete_postdb_by_id_end_point(current_user, post_id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())

    async def get_posts_end_point(self, limit: int, last_id: int) -> list[OutPost]:
        try:
            response = await PostService().get_posts_end_point(limit, last_id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response

    async def get_by_id_post_end_point(self, post_id: int) -> OutPost:
        try:
            response = await PostService().get_by_id_post_end_point(post_id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response

    async def get_by_username_post_end_point(
        self, username: str, id: int
    ) -> list[OutPost]:
        try:
            response = await PostService().get_by_username_post_end_point(username, id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response

    async def update_post_end_point(
        self, current_user: UserCurrent, post_id: int, updated_post: UpdatePost
    ) -> OutPost:
        try:
            response = await PostService().update_post_end_point(
                current_user, post_id, updated_post
            )
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response
