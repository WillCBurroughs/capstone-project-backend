from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
#from app.models.funding_opportunity import FundingOpportunity
from app.schemas import User
from typing import List

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean(), default=True)
    
    phone_number: Mapped[str] = mapped_column(String, default="270-427-6325")
    age: Mapped[int] = mapped_column(Integer, default= 20)
    is_student: Mapped[bool] = mapped_column(Boolean(), default=True)
    university_name: Mapped[str] = mapped_column(String, index=True, default="")

    gender: Mapped[str] = mapped_column(String, index= True, default="")
    is_veteran: Mapped[str] = mapped_column(String, index=True, default="is_veteran")
    living_country: Mapped[str] = mapped_column(String, index=True, default="")
    living_state: Mapped[str] = mapped_column(String, index=True, default="")
    living_city: Mapped[str] = mapped_column(String, index=True, default="")

    opportunities = relationship("FundingOpportunity", back_populates="host")

    def to_schema(self):
        return User(
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
            living_country = self.living_country,
            living_state = self.living_state,
            living_city = self.living_city,
            is_veteran = self.is_veteran
        )