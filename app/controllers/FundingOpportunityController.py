from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.BaseController import BaseController
from app.models import FundingOpportunity
from app.schemas import FundingOpportunityBase, FundingOpportunitySchema, FundingOpportunityInDBBase


class FundingOpportunityController(BaseController[FundingOpportunity, FundingOpportunityInDBBase, FundingOpportunityBase]):
    
    def create(self, db: Session, obj_in: FundingOpportunityBase) -> FundingOpportunityInDBBase:
        db_obj = FundingOpportunity(
            fund_name=obj_in.fund_name,
            fund_contact_email=obj_in.fund_contact_email,
            fund_type=obj_in.fund_type,
            fund_amount=obj_in.fund_amount,
            equity_taken=obj_in.equity_taken,
            amount_equity_taken=obj_in.amount_equity_taken,
            fund_host_id=obj_in.fund_host_id
        )
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

funding_opportunity = FundingOpportunityController(FundingOpportunity)