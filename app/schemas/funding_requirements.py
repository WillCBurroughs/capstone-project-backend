from pydantic import BaseModel
from typing import Optional

class FundingRequirementsBase(BaseModel):
     title: str
     data: str

     class Config:
         orm_mode = True

class FundingRequirementsInDB(FundingRequirementsBase):
    id: int

class UpdateFundingRequirements(FundingRequirementsBase):
    title: Optional[str]
    data: Optional[str]

class FundingRequirementsSchema(FundingRequirementsInDB):
    class Config: 
        from_attributes = True

        allow_population_by_field_name = True

