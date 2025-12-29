import grpc 
from fastapi import HTTPException
from app.admin.gateway.iadmin_gateway import IAdminGateWay
from app.admin.grpc.admin_service import AdminService
from app.utils.schemas import UserCurrent
from app.utils.check import (
    check_code,
)

class AdminGateWay(IAdminGateWay):
    async def delete_user_end_point(self, current_admin: UserCurrent, user_id: int) -> None:
        try:
            response = await AdminService().delete_user_end_point(current_admin,user_id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response
    
    async def ban_user_end_point(self, current_admin: UserCurrent, user_id: int) -> None:
        try:
            response = await AdminService().ban_user_end_point(current_admin,user_id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response
    
    async def delete_post_end_point(self, current_admin: UserCurrent, post_id: int) -> None:
        try:
            response = await AdminService().delete_post_end_point(current_admin,post_id)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), detail=e.details())
        return response