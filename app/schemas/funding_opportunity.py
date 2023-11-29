# from pydantic import BaseModel
# from typing import Optional

# class FundingOpportunityBase(BaseModel):
#     id: int
#     fund_name: str
#     fund_host_id: str
#     fund_contact_email: str
#     fund_type: str
#     fund_amount: Optional[float]
#     equity_taken: Optional[bool]
#     amount_equity_taken: Optional[float]

#     class Config:
#         orm_mode = True

# class FundingOpportunityInDB(FundingOpportunityBase):
#     pass