from typing import Any, List, Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, Form, status
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import controllers, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from datetime import timedelta
from app.core import security


router = APIRouter()

@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = controllers.user.get_multi(db, skip=skip, limit=limit)
    return users

@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    email: EmailStr = Body(None),
    username: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if email is not None:
        user_in.email = email
    if username is not None:
        user_in.username = email
    user = controllers.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    new_user = controllers.user.get_by_email(db, email=user_in.email)
    if new_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    new_user = controllers.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(
            email_to=user_in.email, username=user_in.email, password=user_in.password
        )
    return new_user


@router.get("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    email: EmailStr = Body(None),
    username: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new user.
    """
    new_user = controllers.user.get_by_email(db, email=current_user.email)
    if new_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    new_user = controllers.user.create(db, obj_in=current_user)
    if settings.EMAILS_ENABLED and current_user.email:
        send_new_account_email(
            email_to=current_user.email, username=current_user.email, password=current_user.password
        )
    return new_user
    
    

@router.get("/user-id", response_model=int)
def get_user_id(current_user: models.User = Depends(deps.get_current_user)) -> int:
    """
    Get user ID for the currently logged-in user.
    """
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    print("This is correct")
    return current_user.id


@router.get("/{user_id}/is_veteran", response_model=bool)
def is_veteran(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> bool:
    """
    Get the is_veteran status of a specific user by id.
    """
    user = controllers.user.get(db, id=user_id)
    if user == current_user or controllers.user.is_superuser(current_user):
        return user.is_veteran
    raise HTTPException(
        status_code=400, detail="The user doesn't have enough privileges"
    )

@router.get("/{user_id}/is_student", response_model=bool)
def is_student(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> bool:
    """
    Get the is_veteran status of a specific user by id.
    """
    user = controllers.user.get(db, id=user_id)
    if user == current_user or controllers.user.is_superuser(current_user):
        return user.is_student
    raise HTTPException(
        status_code=400, detail="The user doesn't have enough privileges"
    )

# How to get university 
@router.get("/{user_id}/get_university", response_model=schemas.User)
def get_university(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> bool:
    """
    Get the is_veteran status of a specific user by id.
    """
    user = controllers.user.get(db, id=user_id)
    
    return user.university_name


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    userame: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    new_user = controllers.user.get_by_email(db, email=email)
    if new_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, username=username)
    new_user = controllers.user.create(db, obj_in=user_in)
    return new_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = controllers.user.get(db, id=user_id)

    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
) -> Any:
    """
    Update a user.
    """
    user = controllers.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = controllers.user.update(db, db_obj=user, obj_in=user_in)
    return user

@router.put("column/{user_id}", response_model=schemas.User)
def update_user_attr(
    user_id: int,
    column_name: str,  
    column_value: Any,  
    db: Session = Depends(deps.get_db),
) -> Any:
    existing_user_id = controllers.user.get(db, id=user_id)
    if existing_user_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Food Log with id {user_id} not found",
        )

    
    setattr(existing_user_id, column_name, column_value)

    db.commit()
    db.refresh(existing_user_id)

    return existing_user_id



@router.post("/register")
def register_user(*, db: Session = Depends(deps.get_db), 
    username: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[str, Form()]
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    new_user = controllers.user.get_by_email(db, email=email)
    if new_user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, username=username)
    new_user = controllers.user.create(db, obj_in=user_in)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    # check if token exists
    existing_token: Token = controllers.token.get_token_by_user_id(db, obj_in=new_user.id)

    if existing_token:
        if existing_token.expires < datetime.datetime.utcnow():
            token = controllers.token.refresh(db, obj_in=existing_token)

    if not existing_token: 
        access_token: str = security.create_access_token(new_user.id, expires_delta=access_token_expires)
        token = controllers.token.create(db, obj_in=access_token)

    return {
        "access_token": token.access_token,
        "token_type": "bearer"
    }