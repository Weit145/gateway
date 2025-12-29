from typing import Annotated

from fastapi import APIRouter, status, Depends, Path

from app.utils.user_current import get_admin_user
from app.utils.schemas import UserCurrent

from app.admin.gateway.admin_gateway import AdminGateWay

router = APIRouter(prefix="/user")


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_end_point(
    current_admin: Annotated[UserCurrent, Depends(get_admin_user)],
    user_id: Annotated[int, Path(title="The ID of the user to delete")],
) -> None:
    return await AdminGateWay().delete_user_end_point(current_admin,user_id)


@router.put("/{user_id}/", status_code=status.HTTP_200_OK)
async def ban_user_end_point(
    current_admin: Annotated[UserCurrent, Depends(get_admin_user)],
    user_id: Annotated[int, Path(title="The ID of the user to ban")],
) -> None:
    return await AdminGateWay().ban_user_end_point(current_admin,user_id)
