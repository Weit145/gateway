from typing import Annotated

from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK    )
async def create_post_end_point(
    post: str,
    current_user: str,
) -> None:
    return 


@router.delete("/{post_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_postdb_by_id_end_point(
    current_user: str,
    post_db: str,
) -> None:
    return


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_posts_end_point(
) -> None:
    return


@router.get("/{post_id}/", status_code=status.HTTP_200_OK)
async def get_by_id_post_end_point(
    post_db: str,
) -> None:
    return


@router.put("/{post_id}/", status_code=status.HTTP_200_OK)
async def update_post_end_point(
    post: str,
    post_to_redact: str,
) -> None:
    return 
