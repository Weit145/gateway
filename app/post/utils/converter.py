from proto import post_pb2
from app.utils.schemas import (
    UserCurrent,
)

from app.post.utils.schemas import (
    OutPost,
    CreatePost,
    UpdatePost,
)


def converter_user_create_request(
    current_user: UserCurrent,
    new_post: CreatePost,
) -> post_pb2.PostCreateRequest:
    return post_pb2.PostCreateRequest(
        auth_id=current_user.id,
        title=new_post.title,
        body=new_post.body,
    )


def converter_user_delete_request(
    current_user: UserCurrent,
    post_id: int,
) -> post_pb2.PostDeleteRequest:
    return post_pb2.PostDeleteRequest(
        auth_id=current_user.id,
        post_id=post_id,
    )


def converter_user_get_posts_request(
    limit: int,
    last_id: int,
) -> post_pb2.PostGetGroupRequest:
    return post_pb2.PostGetGroupRequest(
        limit=limit,
        last_id=last_id,
    )


def converter_user_get_by_id_request(
    post_id: int,
) -> post_pb2.PostGetByIdRequest:
    return post_pb2.PostGetByIdRequest(
        post_id=post_id,
    )


def converter_user_get_by_auth_request(
    username: str,
    id: int,
) -> post_pb2.PostGetByIdUserRequest:
    return post_pb2.PostGetByIdUserRequest(
        username=username,
        auth_id=id,
    )


def converter_user_update_request(
    current_user: UserCurrent,
    post_id: int,
    updated_post: UpdatePost,
) -> post_pb2.PostPutRequest:
    return post_pb2.PostPutRequest(
        auth_id=current_user.id,
        post_id=post_id,
        title=updated_post.title,
        body=updated_post.body,
    )


def converter_OutPost(
    response,
) -> OutPost:
    return OutPost(
        id=response.post_id,
        username=response.username,
        title=response.title,
        body=response.body,
    )


def converter_list_OutPost(
    responses,
) -> list[OutPost]:
    return [converter_OutPost(post) for post in responses.posts]
