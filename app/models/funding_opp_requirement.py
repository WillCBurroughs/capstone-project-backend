from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.funding_opportunity import FundingOpportunity
from app.models.funding_requirement import FundingRequirement
from app.schemas.funding_opp_requirements import FundingOpportunityRequirementSchema
from typing import List

from app.db.base_class import Base

class FundingOppRequirement(Base):

    __tablename__ = "funding_opp_requirements"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement= True)
    fund_id: Mapped[int] = Column(Integer, ForeignKey('funding_opportunity.id'))
    requirement_id: Mapped[int] = Column(Integer, ForeignKey('funding_requirements.id'))

    # Used to define data to be parsed for testing if qualified 
    data: Mapped[str] = Column(String, index=True)

    opportunity = relationship("FundingOpportunity", back_populates="requirements")
    requirement = relationship("FundingRequirement", back_populates="opportunities")
    #fundingRequirementBackPopulator: Mapped[List["FundingRequirement"]] = relationship(back_populates="funding_requirements_opp")
    
    def to_schema(self):
            return FundingOpportunityRequirementSchema(

                id = self.id,
                fund_id = self.fund_id,
                requirement_id = self.requirement_id,
                data = self.data

    )