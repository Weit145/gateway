from proto import user_pb2
from app.utils.schemas import(
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
)->user_pb2.PostCreateRequest:
    return user_pb2.PostCreateRequest(
        author_id=current_user.id,
        title=new_post.title,
        content=new_post.body,
    )

def converter_user_delete_request(
    current_user: UserCurrent,
    post_id: int,
)->user_pb2.PostDeleteRequest:
    return user_pb2.PostDeleteRequest(
        auth_id=current_user.id,
        post_id=post_id,
    )

def converter_user_get_posts_request(
    group_post_id: int,
)->user_pb2.PostGetGroupRequest:
    return user_pb2.PostGetGroupRequest(
        group_id=group_post_id,
    )

def converter_user_get_by_id_request(
    post_id: int,
)->user_pb2.PostGetByIdRequest:
    return user_pb2.PostGetByIdRequest(
        post_id=post_id,
    )

def converter_user_get_by_auth_request(
    username: str,
)->user_pb2.PostGetByUsernameRequest:
    return user_pb2.PostGetByUsernameRequest(
        username=username,
    )

def converter_user_update_request(
    current_user: UserCurrent,
    post_id: int,
    updated_post: UpdatePost,
)->user_pb2.PostPutRequest:
    return user_pb2.PostPutRequest(
        auth_id=current_user.id,
        post_id=post_id,
        title=updated_post.title,
        content=updated_post.body,
    )








def converter_OutPost(
    response,
)->OutPost:
    return OutPost(
        id=response.post_id,
        username=response.username,
        title=response.title,
        body=response.body,
    )

def converter_list_OutPost(
    responses,
)->list[OutPost]:
    return [converter_OutPost(response) for response in responses]