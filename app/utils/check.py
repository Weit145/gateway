import grpc
from typing import Any
from fastapi import HTTPException


def check_code(code:Any)->int:
    if code() == grpc.StatusCode.INVALID_ARGUMENT:
        return 400
    elif code() == grpc.StatusCode.NOT_FOUND:
        return 404
    else:
        return 500