import grpc
from proto import user_pb2, user_pb2_grpc
from app.utils.schemas import UserCurrent

from app.user.grpc.iuser_service import IUserService
from app.user.utils.schemas import (
    OutUser,
    UserUpdate,
)
from app.user.utils.converter import(
    converter_user_delete_request,
    converter_user_get_request,
    converter_user_update_request,
    converter_OutUser,
)

class UserService(IUserService):

    def __init__(self, host: str = "user-service", port: int = 50053) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = user_pb2_grpc.UserStub(self.channel)

    async def delete_me_user_end_point(self, current_user: UserCurrent) -> None:
        request = converter_user_delete_request(current_user)
        await self.stub.DeleteUser(request)

    async def read_me_user_end_point(self, current_user: UserCurrent) -> OutUser:
        request = converter_user_get_request(current_user)
        response = await self.stub.GetUser(request)
        return converter_OutUser(response)

    async def update_me_end_point(self, current_user: UserCurrent, new_user: UserUpdate) -> OutUser:
        request = converter_user_update_request(current_user, new_user)
        response = await self.stub.UserUpdate(request)
        return converter_OutUser(response)