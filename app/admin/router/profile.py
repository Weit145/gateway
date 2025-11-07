from typing import Annotated

from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/profile")

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_all_profiles_end_point(
) -> None:
    return


@router.put("/", status_code=status.HTTP_205_RESET_CONTENT)
async def reset_all_profiles_end_point(
) -> None:
    return