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
    # current_user: models.User = Depends(deps.get_current_active_user),
    current_user = test_token()

) -> Any:
    """
    Create a new funding opportunity.
    """
    # current_user = deps.get_current_user().id
    # current_user = Depends(get_current_user)

    current_user = test_token()
    fund_data = fund_in.dict()
    fund_data["fund_host_id"] = current_user


    new_funding_opportunity = controllers.funding_opportunity.create(db, fund_data)
    return new_funding_opportunity