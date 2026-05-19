from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.message_schema import (
    MessageCreate
)
from app.services.message_service import (
    MessageService
)
from app.schemas.message_schema import (
    MessageCreate,
    MessageResponse
)

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)

@router.post("/")
def create_message(
    message: MessageCreate,
    db: Session = Depends(get_db)
):
    return MessageService.create_message(
        db,
        message
    )

@router.get(
    "/{conversation_id}",
    response_model=list[MessageResponse]
)
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db)
):
    return MessageService.get_messages(
        db,
        conversation_id
    )