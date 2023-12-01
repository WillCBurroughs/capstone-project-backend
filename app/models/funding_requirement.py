from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.schemas import FundingOpportunityInDBBase

from app.db.base_class import Base

class FundingRequirement(Base):
    
    __tablename__ = "funding_requirements"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index = True)
    data = Column(String, index = True)

    # Define relationships

    def to_schema(self):
        return FundingOpportunityInDBBase(

        id = self.id,
        title = self.title,
        data = self.data

        )