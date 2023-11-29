from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.schemas import Business_Funding_RequirementsInDB
from models import Business, Requirement

from app.db.base_class import Base

class Business_Funding_Requirements(Base):
    
    __tablename__ = "business_funding_requirements"
    
    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id'))
    requirement_id = Column(Integer, ForeignKey('requirement.id'))

    # Define relationships
    business = relationship("Business")
    requirement = relationship("Requirement")

    relationship()

    def to_schema(self):
        return Business_Funding_RequirementsInDB(

            id = self.id,
            business_id = self.business_id,
            requirement_id = self.requirement_id

        )