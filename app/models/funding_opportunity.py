from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
#from app.models.funding_opp_requirement import FundingOppRequirement
from app.schemas import FundingOpportunitySchema
from typing import List
from app.db.base_class import Base
from app.schemas.user import User
# from app.models.funding_opp_requirement import FundingOppRequirement

class FundingOpportunity(Base):
   
    __tablename__ = "funding_opportunity"
    # id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    fund_name: Mapped[str] = mapped_column(String, index=True)
    fund_host_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    fund_contact_email : Mapped[str] = mapped_column(String, index=True)
    fund_type: Mapped[str] = mapped_column(String, index=True)
    fund_amount: Mapped[float] = mapped_column(Float, index=True)
    equity_taken: Mapped[bool] = mapped_column(Boolean(), index=True)
    amount_equity_taken: Mapped[float] = mapped_column(Float, index=True)

    requirements = relationship("FundingOppRequirement", back_populates="opportunity")

    host = relationship("User", back_populates="opportunities")

    def to_schema(self):
        return FundingOpportunitySchema(

        id = self.id,
        fund_name = self.fund_name,
        fund_host_id = self.fund_host_id,
        
        fund_contact_email = self.fund_contact_email,
        fund_type = self.fund_type,
        fund_amount = self.fund_amount,
        
        equity_taken = self.equity_taken,
        amount_equity_taken = self.amount_equity_taken

        )