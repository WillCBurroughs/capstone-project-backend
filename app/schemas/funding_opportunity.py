from pydantic import BaseModel
from typing import Optional, List
from app.schemas.funding_opp_requirements import FundingOpportunityRequirementSchema

from app.schemas.user import User
# from app.models import User

class FundingOpportunityBase(BaseModel):
    fund_name: str
    fund_contact_email: str
    fund_type: int
    fund_amount: Optional[float]
    equity_taken: Optional[bool]
    amount_equity_taken: Optional[float]
    fund_host_id: int

class FundingOpportunityInDBBase(FundingOpportunityBase):
    id: int

class UpdateFundingOpportunity(FundingOpportunityBase):
    fund_name: Optional[str]
    fund_contact_email: Optional[str]
    fund_type: Optional[int]
    fund_amount: Optional[float]
    equity_taken: Optional[bool]
    amount_equity_taken: Optional[float]

class FundingOpportunitySchema(FundingOpportunityInDBBase):

    host: User

    requirements: List["FundingOpportunityRequirementSchema"]

    class Config:
        from_attributes = True

        populate_by_name = True