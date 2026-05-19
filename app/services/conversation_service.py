from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.contact_repository import (
    ContactRepository
)
from app.repositories.conversation_repository import (
    ConversationRepository
)
from app.schemas.conversation_schema import (
    ConversationCreate
)
from app.models.enums import ConversationStatus

class ConversationService:
    @staticmethod
    def create_conversation(
        db: Session,
        conversation: ConversationCreate
    ):
        contact = ContactRepository.get_by_id(
            db,
            conversation.contact_id
        )
        if not contact:
            raise HTTPException(
                status_code=404,
                detail="Contato não encontrado"
            )
        return ConversationRepository.create(
            db,
            conversation
        )
    @staticmethod
    def get_conversations(db: Session):

        return ConversationRepository.get_all(db)
    
    @staticmethod
    def update_status(
        db: Session,
        conversation_id: int,
        status_data
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
        return ConversationRepository.update_status(
            db,
            conversation,
            status_data.status
        )