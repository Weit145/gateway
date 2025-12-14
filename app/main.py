import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.redis.redis import RedisRepository

from app.user import router as user_router
from app.post import router as post_router
from app.auth import router as auth_router
from app.admin import router as admin_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    allowed = await RedisRepository().rate_limit(request)
    if not allowed:
        return JSONResponse(status_code=429, content={"detail": "Too many requests"})
    return await call_next(request)


app.include_router(user_router,prefix="/user", tags=["User"])
app.include_router(post_router,prefix="/post", tags=["Post"])
app.include_router(auth_router,prefix="/auth", tags=["Auth"])
app.include_router(admin_router,prefix="/admin", tags=["Admin"])



if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)

    # poetry run python app/main.py
    # docker compose up --build
    # git submodule add https://github.com/Weit145/proto-repo proto
    # git submodule update --init --recursive --remote

    #poetry run python -m grpc_tools.protoc     -I proto     --python_out=proto     --grpc_python_out=proto     proto/auth/auth.proto 
    # poetry run python -m grpc_tools.protoc     -I proto     --python_out=proto     --grpc_python_out=proto     proto/user/user.proto 
    # docker compose exec auth-service /bin/sh
    # # внутри контейнера
    # alembic upgrade head

    # docker exec -it kafka bash
    # kafka-console-consumer --bootstrap-server localhost:9092 --topic registration
