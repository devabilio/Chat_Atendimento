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
    user: UserLogin,
    db: Session = Depends(get_db)
):
    token = UserService.login(
        db,
        user.username,
        user.password
    )
    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return token