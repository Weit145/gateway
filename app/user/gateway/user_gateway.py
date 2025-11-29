import grpc 
from fastapi import HTTPException
from app.user.gateway.iuser_gateway import IUserGateWay
from app.user.grpc.user_service import UserService
from app.utils.schemas import UserCurrent
from app.user.utils.schemas import (
    UserUpdate, 
    OutUser,
)
from app.utils.check import(
    check_code,
)


class UserGateWay(IUserGateWay):

    async def delete_me_user_end_point(self, current_user: UserCurrent) -> None:
        try:
            response = await UserService().delete_me_user_end_point(current_user)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        
    async def read_me_user_end_point(self, current_user: UserCurrent) -> OutUser:
        try:
            response = await UserService().read_me_user_end_point(current_user)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        return response
    
    async def update_me_end_point(self, current_user: UserCurrent, new_user: UserUpdate) -> OutUser:
        try:
            response = await UserService().update_me_end_point(current_user, new_user)
        except grpc.RpcError as e:
            raise HTTPException(status_code=check_code(e.code), 
                            detail=e.details())
        return response