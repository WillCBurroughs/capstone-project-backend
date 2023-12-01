from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import Any, List, Annotated

from app import controllers, models, schemas
from app.api import deps
from app.api.api_v1.endpoints.login import test_token



router = APIRouter()

@router.post("/", response_model=schemas.FundingOpportunityBase)
def create_funding_opportunity(
    *,

    db: Session = Depends(deps.get_db),
    fund_in: schemas.FundingOpportunityBase,
    current_user: models.User = Depends(deps.get_current_active_user),

) -> Any:
    """
    Create a new funding opportunity.
    """
    # current_user = deps.get_current_user().id
    # current_user = Depends(get_current_user)
    new_funding_opportunity = controllers.funding_opportunity.create(db, obj_in=fund_in)
    return new_funding_opportunity

@router.get("/", response_model=List[schemas.FundingOpportunityBase])
def read_competitions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any: 
    """
    Get Pitch Comps.
    """
    competitions = controllers.funding_opportunity.get_multi(db, skip=skip, limit=limit)
    return competitions


# @router.get("/", response_model=List[schemas.User])
# def read_users(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: models.User = Depends(deps.get_current_active_superuser),
# ) -> Any:
#     """
#     Retrieve users.
#     """
#     users = controllers.user.get_multi(db, skip=skip, limit=limit)
#     return users