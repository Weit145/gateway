from typing import Annotated

from fastapi import APIRouter, Depends, status, Path, Query

from app.utils.user_current import get_current_user
from app.utils.schemas import UserCurrent

from app.post.gateway.post_gateway import PostGateWay
from app.post.utils.schemas import CreatePost, OutPost, UpdatePost

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def create_post_end_point(
    current_user: Annotated[UserCurrent, Depends(get_current_user)],
    post: CreatePost,
) -> OutPost:
    return await PostGateWay().create_post_end_point(current_user, post)


@router.delete("/{post_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_postdb_by_id_end_point(
    current_user: Annotated[UserCurrent, Depends(get_current_user)],
    post_id: Annotated[int, Path(title="The ID of the post to delete")],
) -> None:
    return await PostGateWay().delete_postdb_by_id_end_point(current_user, post_id)


@router.get("/user/", status_code=status.HTTP_200_OK)
async def get_by_username_post_end_point(
    current_user: Annotated[UserCurrent, Depends(get_current_user)],
    username: str = Query(..., title="Username"),
) -> list[OutPost]:
    return await PostGateWay().get_by_username_post_end_point(username, current_user.id)


@router.get("/group/", status_code=status.HTTP_200_OK)
async def get_posts_end_point(
    limit: int = Query(5),
    last_id: int = Query(0),
) -> list[OutPost]:
    return await PostGateWay().get_posts_end_point(limit, last_id)


@router.get("/one/{post_id}/", status_code=status.HTTP_200_OK)
async def get_by_id_post_end_point(
    post_id: int = Path(title="The ID of the post to get"),
) -> OutPost:
    return await PostGateWay().get_by_id_post_end_point(post_id)


@router.put("/{post_id}/", status_code=status.HTTP_200_OK)
async def update_post_end_point(
    current_user: Annotated[UserCurrent, Depends(get_current_user)],
    post_id: Annotated[int, Path(title="The ID of the post to update")],
    new_post: UpdatePost,
) -> OutPost:
    return await PostGateWay().update_post_end_point(current_user, post_id, new_post)
