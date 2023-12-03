from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.controllers.BaseController import BaseController
from app.models import FundingRequirement
from app.schemas import FundingRequirementsBase, FundingRequirementsSchema, FundingRequirementsInDB


class FundingRequirementController(BaseController[FundingRequirement, FundingRequirementsInDB, FundingRequirementsBase]):
    
    def create(self, db: Session, obj_in: FundingRequirementsBase) -> FundingRequirementsInDB:
        db_obj = FundingRequirement(
            title=obj_in.title,
            data=obj_in.data,
            fund_type=obj_in.fund_type
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: FundingRequirementsSchema, obj_in: Union[FundingRequirementsSchema, Dict[str, Any]]
    ) -> FundingRequirementsSchema:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

funding_requirement = FundingRequirementController(FundingRequirement)