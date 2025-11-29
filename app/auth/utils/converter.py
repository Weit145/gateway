from proto import auth_pb2

from fastapi.responses import JSONResponse

from app.auth.utils.schemas import(
    CookieResponse,
    UserCreate,
    Okey,
    Token,
    CookieResponse,
    AccessToken,
    UserLogin,
    UserCurrent,
)



def convert_user_create_request(
    user: UserCreate,
    )->auth_pb2.UserCreateRequest:
    return auth_pb2.UserCreateRequest(
        login=user.login,
        username=user.username,
        email=user.email,
        password=user.password
    )

def convert_token_request(
    token: Token,
)->auth_pb2.TokenRequest:
    return auth_pb2.TokenRequest(token_pod=token.access_token)

def convert_cookie_request(
    refresh_token:str,
)->auth_pb2.CookieRequest:
    return auth_pb2.CookieRequest(refresh_token=refresh_token)

def convert_user_login_request(
    user:UserLogin,
)->auth_pb2.UserLoginRequest:
    return auth_pb2.UserLoginRequest(
            login=user.login,
            password=user.password
        )

def convert_user_current_request(
    token:str,
)->auth_pb2.UserCurrentRequest:
    return auth_pb2.UserCurrentRequest(
        access_token=token,
    )




def convert_okey_response(
    response
)->Okey:
    return Okey(
        success=response.success,
    )

def convert_cookie_response(
    response
)->CookieResponse:
    return CookieResponse(
        access_token=response.access_token,
        key=response.cookie.key,
        value=response.cookie.value,
        httponly=response.cookie.httponly,
        secure=response.cookie.secure,
        samesite=response.cookie.samesite,
        max_age=response.cookie.max_age,
    )

def convert_access_token_response(
    response
)->AccessToken:
    return AccessToken(
        access_token=response.access_token,
    )

def convert_user_current_response(
    response
)->UserCurrent:
    return UserCurrent(
        id=response.id,
        login=response.login,
        is_active=response.is_active,
        is_verified=response.is_verified,
        role=response.role,
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