import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

    #poetry run python -m grpc_tools.protoc     -I proto     --python_out=proto     --grpc_python_out=proto     proto/auth.proto 

    # docker compose exec auth-service /bin/sh
    # # внутри контейнера
    # alembic upgrade head

    # docker exec -it kafka bash
    # kafka-console-consumer --bootstrap-server localhost:9092 --topic registration
