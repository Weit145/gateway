from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    name_img: str


class ProfileOut(ProfileBase):
    username: str
    user_id: int
