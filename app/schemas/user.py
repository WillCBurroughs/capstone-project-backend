from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None
    phone_number: Optional[str] = None
    age: Optional[int] = None
    is_student: Optional[bool] = False
    university_name: Optional[str] = None
    gender: Optional[str] = None
    is_veteran: Optional[str] = "is_veteran"
    living_country: Optional[bool] = False
    living_state: Optional[str] = None
    living_city: Optional[str] = None

class UserInDBBase(UserBase):
    id: int

class User(UserInDBBase):
    phone_number: str
    age: int
    is_student: bool
    university_name: str
    gender: str
    is_veteran: str
    living_country: str
    living_state: str
    living_city: str

    class Config:
        from_attributes = True