from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.BaseController import BaseController
from app.models import FundingOpportunity as FundingOpportunityModel
from app.schemas import UpdateFundingOpportunity, FundingOpportunitySchema, FundingOpportunityInDBBase


class FundingOpportunityController(BaseController[FundingOpportunitySchema, FundingOpportunityInDBBase, UpdateFundingOpportunity]):
    
    def create(self, db: Session, obj_in: FundingOpportunitySchema) -> FundingOpportunitySchema:
        db_obj = FundingOpportunitySchema(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: FundingOpportunitySchema, obj_in: Union[FundingOpportunitySchema, Dict[str, Any]]
    ) -> FundingOpportunitySchema:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


funding_opportunity = FundingOpportunityController(FundingOpportunitySchema)



