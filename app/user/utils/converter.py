from proto import user_pb2

from app.user.utils.schemas import(
    UserUpdate,
    OutUser,
)
from app.utils.schemas import(
    UserCurrent,
)

def converter_user_delete_request(
    current_user: UserCurrent,
)->user_pb2.UserDeleteRequest:
    return user_pb2.UserDeleteRequest(
        id=current_user.id,
    )

def converter_user_get_request(
    current_user: UserCurrent,
)->user_pb2.UserGetRequest:
    return user_pb2.UserGetRequest(
        id=current_user.id,
    )

def converter_user_update_request(
    current_user: UserCurrent,
    new_user: UserUpdate,
)->user_pb2.UserUpdateRequest:
    return user_pb2.UserUpdateRequest(
        id=current_user.id,
        username=new_user.username,
    )

def converter_OutUser(
    response,
)->OutUser:
    return OutUser(
        username=response.username,
    )