from pydantic import BaseModel
from typing import Optional
from datetime import date

class BusinessBase(BaseModel):
    id: int
    owner_id: int
    revenue: Optional[float]
    country_operation: Optional[str]
    state_operation: Optional[str]
    city_operation: Optional[str]
    for_profit: Optional[bool]
    business_sector: Optional[str]
    type_of_business: Optional[str]
    business_stage: Optional[str]
    business_age: Optional[date]

    class Config:
        orm_mode = True

class BusinessInDB(BusinessBase):
    pass