from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.conversation_schema import (
    ConversationCreate
)
from app.services.conversation_service import (
    ConversationService
)
from app.schemas.conversation_schema import (
    ConversationCreate,
    ConversationResponse
)
from app.schemas.conversation_schema import (
    ConversationCreate,
    ConversationResponse,
    ConversationStatusUpdate
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"]
)


@router.post("/")
def create_conversation(
    conversation: ConversationCreate,
    db: Session = Depends(get_db)
):
    return ConversationService.create_conversation(
        db,
        conversation
    )

@router.get(
    "/",
    response_model=list[ConversationResponse]
)
def get_conversations(
    db: Session = Depends(get_db)
):
    return ConversationService.get_conversations(db)

@router.patch("/{conversation_id}/status")
def update_conversation_status(
    conversation_id: int,
    status_data: ConversationStatusUpdate,
    db: Session = Depends(get_db)
):
    return ConversationService.update_status(
        db,
        conversation_id,
        status_data
    )