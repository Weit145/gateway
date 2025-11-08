from fastapi.responses import JSONResponse
from app.auth.utils.schemas import(
    CookieResponse,

)

def converter_cookie(response:CookieResponse)->JSONResponse:
    result = JSONResponse(content={"access_token": response.access_token})
    result.set_cookie(
        key=response.key,
        value=response.value,
        httponly=response.httponly,
        secure=response.secure,
        samesite=response.samesite,
        max_age=response.max_age,
    )
    return result