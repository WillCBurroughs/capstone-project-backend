from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import Any, List, Annotated

from app import controllers, models, schemas
from app.api import deps
from app.api.api_v1.endpoints.login import test_token

router = APIRouter()

@router.post("/", response_model=schemas.FundingOpportunityRequirementSchema)
def create_funding_opportunity(
    *,

    db: Session = Depends(deps.get_db),
    fund_in: schemas.FundingOppRequirementsBase,

    # The following line does not applow people who are not authenticated to use a service
    # current_user: models.User = Depends(deps.get_current_active_user),

) -> Any:
    """
    Create a new funding opportunity.
    """
    # current_user = deps.get_current_user().id
    # current_user = Depends(get_current_user)
    new_funding_opportunity_requirement = controllers.funding_opportunity_Requirement.create(db, obj_in=fund_in)
    return new_funding_opportunity_requirement

@router.get("/", response_model=List[schemas.FundingOpportunityRequirementSchema])
def read_funding_requirement_opportunities(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> List[schemas.FundingOpportunityRequirementSchema]:
    """
    Get All opportunity requirements
    """
    funding_opportunity_requirement_list = controllers.funding_opportunity_Requirement.get_multi(db, skip=skip, limit=limit)
    return funding_opportunity_requirement_list

# @router.get("/", response_model=List[schemas.FundingOpportunitySchema])
# def read_competitions(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
# ) -> Any: 
#     """
#     Get Pitch Comps.
#     """
#     competitions = controllers.funding_opportunity.get_multi(db, skip=skip, limit=limit)
#     return competitions