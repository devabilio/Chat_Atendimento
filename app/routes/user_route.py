from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
    UserResponse
)
from app.services.user_service import (
    UserService
)
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_user(
        db,
        user
    )

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return UserService.login(
        db,
        form_data.username,
        form_data.password
    )