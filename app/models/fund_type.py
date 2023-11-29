from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Business, Requirement

from app.schemas import Fund_TypeInDB
from app.db.base_class import Base

class Fund_Type(Base):
    
    __tablename__ = "fund_type"
    
    id = Column(Integer, ForeignKey(""))

    owner_id = Column(Integer, ForeignKey('business.id'))


    # Define relationships
    business = relationship("Business")
    requirement = relationship("Requirement")

    relationship()

    def to_schema(self):
        return Fund_TypeInDB(

            id = self.id,
            business_id = self.business_id,
            requirement_id = self.requirement_id

        )