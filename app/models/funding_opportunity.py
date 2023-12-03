from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.schemas import FundingOpportunityBase
from typing import List
from app.db.base_class import Base
from app.models.funding_opp_requirement import FundingOppRequirement

class FundingOpportunity(Base):
   
    __tablename__ = "funding_opportunity"
    
    id = Column(Integer, primary_key=True, index=True)
    fund_name = Column(String, index=True)
    fund_host_id = Column(Integer, ForeignKey('users.id'))
    fund_contact_email = Column(String, index=True)
    fund_type = Column(String, index=True)
    fund_amount = Column(Float, index=True)
    equity_taken = Column(Boolean(), index=True)
    amount_equity_taken = Column(Float, index=True)

    funding_opp_requirements: Mapped[List["FundingOppRequirement"]] = relationship(back_populates="funidngOpportunityBackPopulator")
    

    def to_schema(self):
        return FundingOpportunityBase(

        id = self.id,
        fund_name = self.fund_name,
        fund_host_id = self.fund_host_id,
        
        fund_contact_email = self.fund_contact_email,
        fund_type = self.fund_type,
        fund_amount = self.fund_amount,
        
        equity_taken = self.equity_taken,
        amount_equity_taken = self.amount_equity_taken

        )