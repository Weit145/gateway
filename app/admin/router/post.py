from typing import Annotated

from fastapi import APIRouter, status, Depends, Path

from app.utils.user_current import get_admin_user
from app.utils.schemas import UserCurrent

from app.admin.gateway.admin_gateway import AdminGateWay

router = APIRouter(prefix="/post")


@router.delete("/{post_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post_end_point(
    current_admin: Annotated[UserCurrent, Depends(get_admin_user)],
    post_id: Annotated[int, Path(title="The ID of the post to delete")],
) -> None:
    return await AdminGateWay().delete_post_end_point(current_admin,post_id)
