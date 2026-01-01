import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from fastapi import APIRouter

from app.core.redis.repositories.redis_repositories import RedisRepository

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


api_router = APIRouter(prefix="/api")

api_router.include_router(user_router, prefix="/user", tags=["User"])
api_router.include_router(post_router, prefix="/post", tags=["Post"])
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])

app.include_router(api_router)



if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)
