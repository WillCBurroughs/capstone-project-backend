from pydantic import BaseModel
from typing import Optional

class FundingRequirementsBase(BaseModel):
     title: str
     data: str

     class Config:
         populate_by_name = True

class FundingRequirementsInDB(FundingRequirementsBase):
    id: int

class UpdateFundingRequirements(FundingRequirementsBase):
    title: Optional[str]
    data: Optional[str]

class FundingRequirementsSchema(FundingRequirementsInDB):
    class Config: 
        from_attributes = True

        populate_by_name = True

