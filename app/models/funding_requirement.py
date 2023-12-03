from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.schemas import FundingRequirementsInDB, FundingRequirementsSchema
from typing import List
from app.db.base_class import Base
from app.models.funding_opp_requirement import FundingOppRequirement



class FundingRequirement(Base):
   
    __tablename__ = "funding_requirements"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    title = Column(String, index=True)
    data = Column(String, index=True)

    # funidngOpportunityBackPopulator: Mapped[List["FundingOpportunity"]] = relationship(back_populates="funding_opp_requirements")   
    # funding_opp_requirements: Mapped[List["FundingOppRequirement"]] = relationship(back_populates="funidngOpportunityBackPopulator")

    funding_requirements_opp: Mapped[List["FundingOppRequirement"]] = relationship(back_populates= "fundingRequirementBackPopulator")

    def to_schema(self):
        return FundingRequirementsSchema(

        id = self.id,
        title = self.title,
        data = self.data

        )