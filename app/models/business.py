from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas import BusinessInDB
from models import Business, Requirement

from app.db.base_class import Base

class Business(Base):
    
    __tablename__ = "business"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('business.id'))
    requirement_id = Column(Integer, ForeignKey('requirement.id'))

    # Define relationships
    business = relationship("Business")
    requirement = relationship("Requirement")

    relationship()

    def to_schema(self):
        return BusinessInDB(

            id = self.id,
            business_id = self.business_id,
            requirement_id = self.requirement_id

        )