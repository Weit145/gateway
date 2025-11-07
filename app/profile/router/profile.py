from typing import Annotated

from fastapi import APIRouter, Depends, status


router = APIRouter()

@router.put("/", status_code=status.HTTP_200_OK)
async def update_profile_end_point(
    new_profile: str,
    profile: str,
) -> None:
    return 

@router.put("/reset/", status_code=status.HTTP_200_OK)
async def reset_me_end_point(
    profile: str,
) -> None:
    return


@router.get("/", status_code=status.HTTP_200_OK)
async def read_me_profile_end_point(
    profile: str,
) -> None:
    return
