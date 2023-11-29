from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.schemas import BusinessInDB
from models import Business, Requirement

from app.db.base_class import Base

class Business(Base):
    
    __tablename__ = "business"
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    revenue = Column(float, index = True)
    country_operation = Column(String, index = True)
    state_operation = Column(String, index = True)
    city_operation = Column(String, index = True)
    for_profit = Column(Boolean(), index = True)
    business_sector = Column(String, index = True)
    type_of_business = Column(String, index = True)
    business_stage = Column(String, index = True)
    business_age = Column(Date, index = True)

    # Define relationships
    owner = relationship("Owner", back_populates="businesses")
    business_funding_requirements = relationship("Business_Funding_Requirements", back_populates="business")

    relationship()

    def to_schema(self):
        return BusinessInDB(

            id = self.id,
            owner_id = self.owner_id,
            revenue = self.revenue,
            country_operation = self.country_operation,
            state_operation = self.state_operation,
            city_operation = self.city_operation,
            for_profit = self.for_profit,
            business_sector = self.business_sector,
            type_of_business = self.type_of_business, 
            business_stage = self.business_stage,
            business_age = self.business_age

        )