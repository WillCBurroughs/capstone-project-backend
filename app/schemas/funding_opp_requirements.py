from pydantic import BaseModel
from typing import Optional

class FundingOppRequirementsBase(BaseModel):
    fund_id: int
    requirement_id: int

    # Used to define data to be parsed for testing if qualified 
    data: str

class FundingOppRequirementInDBBase(FundingOppRequirementsBase):
    id: int

class UpdateFundingOpportunity(FundingOppRequirementsBase):
    data: Optional[str]

class FundingOpportunityRequirementSchema(FundingOppRequirementInDBBase):
    class config:

        from_attributes = True
        allow_population_by_field_name = True


# from pydantic import BaseModel
# from typing import Optional

# from pydantic import BaseModel
# from typing import Optional

# class FundingOpportunityBase(BaseModel):
#     fund_name: str
#     fund_contact_email: str
#     fund_type: int
#     fund_amount: Optional[float]
#     equity_taken: Optional[bool]
#     amount_equity_taken: Optional[float]
#     fund_host_id: int

# class FundingOpportunityInDBBase(FundingOpportunityBase):
#     id: int

# class UpdateFundingOpportunity(FundingOpportunityBase):
#     fund_name: Optional[str]
#     fund_contact_email: Optional[str]
#     fund_type: Optional[int]
#     fund_amount: Optional[float]
#     equity_taken: Optional[bool]
#     amount_equity_taken: Optional[float]

# class FundingOpportunitySchema(FundingOpportunityInDBBase):

#     class Config:
#         from_attributes = True

#         allow_population_by_field_name = True