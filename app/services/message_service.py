from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.enums import (
    ConversationStatus
)
from app.repositories.conversation_repository import (
    ConversationRepository
)
from app.repositories.message_repository import (
    MessageRepository
)
from app.schemas.message_schema import (
    MessageCreate
)

class MessageService:
    @staticmethod
    def create_message(
        db: Session,
        message: MessageCreate
    ):
        conversation = ConversationRepository.get_by_id(
            db,
            message.conversation_id
        )
        if not conversation:
            raise HTTPException(
                status_code=404,
                detail="Conversa não encontrada"
            )
        if conversation.status == ConversationStatus.CLOSED:
            raise HTTPException(
                status_code=400,
                detail="Conversa encerrada"
            )

        return MessageRepository.create(
            db,
            message
        )
    
    @staticmethod
    def get_messages(
        db: Session,
        conversation_id: int
    ):
        conversation = ConversationRepository.get_by_id(
            db,
            conversation_id
        )
        if not conversation:
            raise HTTPException(
                status_code=404,
                detail="Conversa não encontrada"
            )
        return MessageRepository.get_by_conversation(
            db,
            conversation_id
        )