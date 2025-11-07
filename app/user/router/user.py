from typing import Annotated

from fastapi import APIRouter, Depends, status

router = APIRouter()

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me_user_end_point(
    current_user:str,
) -> None:
    return

@router.get("/", status_code=status.HTTP_200_OK)
async def read_me_user_end_point(
    current_user: str,
) -> None:
    return 
