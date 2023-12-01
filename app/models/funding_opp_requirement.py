from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

from app.db.base_class import Base

class FundingOppRequirement(Base):
    
    __tablename__ = "funding_opp_requirements"
    
    id = Column(Integer, primary_key=True, index=True)
    fund_id = Column(Integer, ForeignKey('funding_opportunity.id'))
    requirement_id = Column(Integer, ForeignKey('funding_requirements.id'))
    
    # Used to define data to be parsed for testing if qualified 
    data = Column(String, index=True)
    
    # funidngOpportunityBackPopulator: Mapped[List["FundingOpportunity"]] = relationship(back_populates="funding_opp_requirements")
    # fundingRequirementBackPopulator: Mapped[List["FundingRequirement"]] = relationship(back_populates= "funding_opp_requirements")
    
    funding_opportunity = relationship("FundingOpportunity", back_populates="funding_opp_requirements")
    funding_requirement = relationship("FundingRequirement", back_populates="funding_opp_requirements")