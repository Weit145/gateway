from proto import auth_pb2

from fastapi.responses import JSONResponse

from app.auth.utils.schemas import(
    UserCurrent as auth_UserCurrent
)
from app.utils.schemas import(
    UserCurrent
)

def converter_UserCurrent(
    response: auth_UserCurrent,
)->UserCurrent:
    return UserCurrent(
        id=response.id,
        login=response.login,
        is_active=response.is_active,
        is_verified=response.is_verified,
        role=response.role,
    )