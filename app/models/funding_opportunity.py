from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.schemas import funding_opportunityInDB
from models import Business, Requirement

from app.db.base_class import Base

class Funding_Opportunity(Base):
    
    __tablename__ = "funding_opportunity"
    
    id = Column(Integer, primary_key=True, index=True)
    fund_name = Column(String, index = True)
    fund_host_id = Column(String, ForeignKey('user.id'))
    
    fund_contact_email = Column(String, index = True)
    fund_type = Column(String, index = True)
    fund_amount = Column(float, index = True)

    equity_taken = Column(Boolean(), index = True)
    amount_equity_taken = Column(float, index = True)

    # Define relationships


    def to_schema(self):
        return funding_opportunityInDB(

        id = self.id,
        fund_name = self.fund_name,
        fund_host_id = self.fund_host_id,
        
        fund_contact_email = self.fund_contact_email,
        fund_type = self.fund_type,
        fund_amount = self.fund_amount,
        
        equity_taken = self.equity_taken,
        amount_equity_taken = self.amount_equity_taken

        )