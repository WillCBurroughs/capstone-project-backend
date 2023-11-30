from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str = None

class UserInDBBase(UserBase):
    id: int

class User(UserInDBBase):
    phone_number: str
    age: int
    is_student: bool
    university_name: str
    gender: str
    is_veteran: bool
    living_country: str
    living_state: str
    living_city: str

    class Config:
        from_attributes = True