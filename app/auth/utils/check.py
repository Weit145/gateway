from typing import Any
from fastapi import HTTPException


def check_response(response:Any)->None:
    if not response.success:
        raise HTTPException(status_code=response.status_code, 
                            detail=response.error)