import grpc
from proto import admin_pb2_grpc
from app.utils.schemas import UserCurrent

from app.admin.grpc.iadmin_service import IAdminService

from app.admin.utils.converter import(
    convert_delete_post,
    convert_delete_user,
    convert_ban_user,
)

class AdminService(IAdminService):
    def __init__(self, host: str = "admin-service", port: int = 50056) -> None:
        self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        self.stub = admin_pb2_grpc.AdminStub(self.channel)

    async def delete_user_end_point(self, current_admin: UserCurrent, user_id: int) -> None:
        request = convert_delete_user(id = user_id)
        await self.stub.DeleteUser(request)

    async def ban_user_end_point(self, current_admin: UserCurrent, user_id: int) -> None:
        request = convert_ban_user(id = user_id)
        await self.stub.BanUser(request)

    async def delete_post_end_point(self, current_admin: UserCurrent, post_id: int) -> None:
        request = convert_delete_post(id = post_id)
        await self.stub.DeletePost(request)