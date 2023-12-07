from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session, joinedload

from app.controllers.BaseController import BaseController
from app.models import FundingOpportunity, FundingOppRequirement, FundingRequirement, User
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

    def getFOwithReqs(
        self, db: Session, *, skip: int = 0, limit: int = 100, funding_opp_id: int
    ) -> Any:
        
        results = db.query(FundingOpportunity)\
            .join(FundingOppRequirement, FundingOppRequirement.fund_id == FundingOpportunity.id)\
            .where(FundingOpportunity.id == funding_opp_id).all()
        # funding_opps = {}
        # for result in results:
  
        #     funding_opp_requirements = (
        #         db.query(FundingOppRequirement)
        #         .where(FundingOppRequirement.fund_id == result.id)
        #         .all()
        #     )
        #     funding_host = (
        #         db.query(User)
        #         .where(User.id == result.fund_host_id)
        #         .all()
        #     )
        #     fo = {
        #         "funding_host":funding_host,
        #         "funding_requirements":funding_opp_requirements,
        #         "funding_opp":result
        #     }

        #     funding_opps[result.id] = fo

        # fos = list(funding_opps.values())
        # print(fos)
        return results

funding_opportunity = FundingOpportunityController(FundingOpportunity)