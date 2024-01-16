from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.BaseController import BaseController
from app.models import FundingOppRequirement
from app.schemas import FundingOppRequirementsBase, FundingOpportunityRequirementSchema, FundingOppRequirementInDBBase 


class FundingOpportunityRequirementController(BaseController[FundingOppRequirement, FundingOppRequirementInDBBase, FundingOppRequirementsBase]):
    
    def create(self, db: Session, obj_in: FundingOppRequirementsBase) -> FundingOppRequirementInDBBase:
        db_obj = FundingOppRequirement(
            fund_id=obj_in.fund_id,
            requirement_id =obj_in.requirement_id,
            data =obj_in.data,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: FundingOpportunityRequirementSchema, obj_in: Union[FundingOpportunityRequirementSchema, Dict[str, Any]]
    ) -> FundingOpportunityRequirementSchema:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

funding_opportunity_Requirement = FundingOpportunityRequirementController(FundingOppRequirement)



# id = Column(Integer, primary_key=True, index=True, autoincrement= True)
# fund_id = Column(Integer, ForeignKey('funding_opportunity.id'))
# requirement_id = Column(Integer, ForeignKey('funding_requirements.id'))

# # Used to define data to be parsed for testing if qualified 
# data = Column(String, index=True)