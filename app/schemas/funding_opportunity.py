from pydantic import BaseModel
from typing import Optional

class FundingOpportunityBase(BaseModel):
    fund_name: str
    fund_contact_email: str
    fund_type: int
    fund_amount: Optional[float]
    equity_taken: Optional[bool]
    amount_equity_taken: Optional[float]

class FundingOpportunityInDBBase(FundingOpportunityBase):
    id: int
    fund_host_id: int

class UpdateFundingOpportunity(FundingOpportunityBase):
    fund_name: Optional[str]
    fund_contact_email: Optional[str]
    fund_type: Optional[int]
    fund_amount: Optional[float]
    equity_taken: Optional[bool]
    amount_equity_taken: Optional[float]

class FundingOpportunitySchema(FundingOpportunityInDBBase):

    class Config:
        from_attributes = True

        allow_population_by_field_name = True