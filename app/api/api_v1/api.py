from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, utils, funding, requirement, funding_opp_requirement

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(funding.router, prefix="/funding", tags=["funding"])
api_router.include_router(requirement.router, prefix="/requirement", tags = ["requirement"])
api_router.include_router(funding_opp_requirement.router, prefix = "/funding-opp-req", tags = ["funding-opp-req"])
