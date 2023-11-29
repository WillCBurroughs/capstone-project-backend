from pydantic import BaseModel

class BusinessFundingRequirementsBase(BaseModel):
    id: int
    business_id: int
    requirement_id: int

    class Config:
        orm_mode = True

class BusinessFundingRequirementsInDB(BusinessFundingRequirementsBase):
    pass

