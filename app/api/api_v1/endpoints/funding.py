from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from typing import Any, List, Annotated

from app import controllers, models, schemas
from app.api import deps
from app.api.api_v1.endpoints.login import test_token

router = APIRouter()

@router.post("/", response_model=schemas.FundingOpportunitySchema)
def create_funding_opportunity(
    *,

    db: Session = Depends(deps.get_db),
    fund_in: schemas.FundingOpportunityBase,
    # The following line does not applow people who are not authenticated to use a service
    # current_user: models.User = Depends(deps.get_current_active_user),

) -> Any:
    """
    Create a new funding opportunity.
    """
    # current_user = deps.get_current_user().id
    # current_user = Depends(get_current_user)
    new_funding_opportunity = controllers.funding_opportunity.create(db, obj_in=fund_in)
    return new_funding_opportunity

# Creating funding_opp on its own 
# Would need to get to get id from name 
# Only show pittch competitions from drop down after making competition 
# Have separate section for updating requirements from drop down 

@router.get("/", response_model=List[schemas.FundingOpportunitySchema])
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

@router.get("/{funding_opp_id}", response_model=List[schemas.FundingOpportunitySchema])
# def get_funding_opp_id(
#     funding_opp_id: int,
#     db: Session = Depends(deps.get_db),
# ) -> Any: 
#     """
#     Get Pitch Comps.
#     """
    # stmt = select(models.FundingOpportunity)\
    #     .where(models.FundingOpportunity.id == funding_opp_id)\
    #     .join(models.FundingOpportunity.funding_opp_requirements)
    # competitions = db.execute(stmt)
    # return competitions
def getFOs (
    funding_opp_id: int,
    db: Session = Depends(deps.get_db)
) -> List[schemas.FundingOpportunitySchema]:
    
    fos = controllers.funding_opportunity.getFOwithReqs(db, skip=0, limit=100, funding_opp_id=int(funding_opp_id))
    return fos

@router.get("/all", response_model=List[schemas.FundingOpportunitySchema])
def getAllFOwithReqs (
    db: Session = Depends(deps.get_db)
) -> Any:
    
    fos = controllers.funding_opportunity.getAllFOwithReqs(db, skip = 0, limit=100)
    return fos

@router.delete("/{fund_id}", response_model=schemas.FundingOpportunitySchema)
def delete_fund(
    fund_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    result = controllers.funding_opportunity.remove(db, id = fund_id)
    if not result:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Fund with id: {fund_id} not found"
        )
    return result



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