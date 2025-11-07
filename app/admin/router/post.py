from typing import Annotated

from fastapi import APIRouter, Depends, status, Request

router = APIRouter(prefix="/post")

@router.delete("/all/", status_code=status.HTTP_204_NO_CONTENT)
async def dellete_all_posts_end_point(
    request: Request,
) -> None:
    return
