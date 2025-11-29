from typing import Annotated

from fastapi import APIRouter, Depends, status, Path

from app.utils.user_current import get_current_user
from app.utils.schemas import UserCurrent

from app.user.utils.schemas import UserUpdate, OutUser
from app.user.gateway.user_gateway import UserGateWay
router = APIRouter()

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me_user_end_point(
    current_user:Annotated[UserCurrent, Depends(get_current_user)],
) -> None:
    await UserGateWay().delete_me_user_end_point(current_user)

@router.get("/", status_code=status.HTTP_200_OK)
async def read_me_user_end_point(
    current_user:Annotated[UserCurrent, Depends(get_current_user)],
) -> OutUser:
    return await UserGateWay().read_me_user_end_point(current_user)


@router.put("/", status_code=status.HTTP_200_OK)
async def update_me_end_point(
    current_user:Annotated[UserCurrent, Depends(get_current_user)],
    new_user: UserUpdate,
) -> OutUser:
    return await UserGateWay().update_me_end_point(current_user, new_user)

# @router.put("/reset/", status_code=status.HTTP_200_OK)
# async def reset_me_end_point(
#     profile: str,
# ) -> None:
#     return
