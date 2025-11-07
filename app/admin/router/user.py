from typing import Annotated

from fastapi import APIRouter, Depends, Path, status

router = APIRouter(prefix="/user")


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_users_end_point(
) -> None:
    return

@router.delete("/nocomfirm/",status_code = status.HTTP_204_NO_CONTENT)
async def dellete_all_no_comfirm_users_end_point(
)->None:
    return

@router.get("/{user_id}/", status_code=status.HTTP_200_OK)
async def get_user_by_id_end_point(
    user_id: Annotated[int, Path(ge=1)],
) -> None:
    return

