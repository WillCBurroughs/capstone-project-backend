from pydantic import BaseModel

class UserRoleBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

class UserRoleInDB(UserRoleBase):
    pass