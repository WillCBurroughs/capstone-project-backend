from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship, Mapped
from app.schemas import UserInDBBase
from typing import List

from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[String] = Column(String, index=True)
    email: Mapped[String] = Column(String, unique=True, index=True, nullable=False)
    hashed_password: Mapped[String] = Column(String, nullable=False)
    is_active: Mapped[Boolean] = Column(Boolean(), default=True)
    is_superuser: Mapped[Boolean] = Column(Boolean(), default=False)
    
    phone_number: Mapped[String] = Column(String, default="270-427-6325")
    age: Mapped[Integer] = Column(Integer, default= 20)
    is_student: Mapped[Boolean] = Column(Boolean(), default=True)
    university_name: Mapped[String] = Column(String, index=True)

    gender: Mapped[String] = Column(String, index= True)
    is_veteran: Mapped[Boolean] = Column(Boolean, index=True)
    living_country: Mapped[String] = Column(String, index=True)
    living_state: Mapped[String] = Column(String, index=True)
    living_city: Mapped[String] = Column(String, index=True)

    # funding_opportunities: relationship(Mapped[List["FundingOpportunity"]], foreign_keys="funding_opportunity.fund_host_id", back_populates="host")

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