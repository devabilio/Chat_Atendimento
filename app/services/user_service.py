from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from app.repositories.user_repository import (
    UserRepository
)
from app.auth.security import (
    hash_password,
    verify_password
)
from app.auth.jwt_handler import (
    create_access_token
)

class UserService:
    @staticmethod
    def create_user(
        db: Session,
        user_data: UserCreate
    ):
        existing_user = (
            UserRepository.get_user_by_username(
                db,
                user_data.username
            )
        )
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )
        hashed_password = hash_password(
            user_data.password
        )
        user = User(
            username=user_data.username,
            password=hashed_password
        )
        return UserRepository.create_user(
            db,
            user
        )

    @staticmethod
    def login(
        db: Session,
        username: str,
        password: str
    ):
        user = UserRepository.get_user_by_username(
            db,
            username
        )
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )
        password_valid = verify_password(
            password,
            user.password
        )
        if not password_valid:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )
        token = create_access_token({
            "sub": user.username
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }