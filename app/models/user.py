from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.schemas import UserInDB

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    
    phone_number = Column(Integer, default=True)
    age = Column(Integer, default=True)
    is_student = Column(Boolean(), default=True)
    university_name = Column(String, index=True)

    gender = Column(String, index=True)
    is_veteran = Column(String, index=True)
    living_country = Column(String, index=True)
    living_state = Column(String, index=True)
    living_city = Column(String, index=True)

    relationship()

    def to_schema(self):
        return UserInDB(
            id=self.id,
            username=self.username,
            email=self.email,
            hashed_password=self.hashed_password,
            is_active = self.is_active,
            is_superuser = self.is_superuser,
            phone_number = self.phone_number ,
            age = self.age,
            is_student = self.is_student,
            university_name = self.university_name,
            gender = self.gender,
            is_veteran = self.is_veteran,
            living_country = self.living_country,
            living_state = self.living_state,
            living_city = self.living_city
        )