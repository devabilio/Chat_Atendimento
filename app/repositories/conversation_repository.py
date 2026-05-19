from sqlalchemy.orm import Session

from app.models.conversation_model import Conversation
from app.schemas.conversation_schema import (
    ConversationCreate
)
from app.models.enums import ConversationStatus

class ConversationRepository:
    @staticmethod
    def create(
        db: Session,
        conversation: ConversationCreate
    ):
        new_conversation = Conversation(
            contact_id=conversation.contact_id
        )
        db.add(new_conversation)
        db.commit()
        db.refresh(new_conversation)
        return new_conversation
    
    @staticmethod
    def get_all(db: Session):
       return db.query(Conversation).all()
    @staticmethod
    def get_by_id(
        db: Session,
        conversation_id: int
    ):
        return db.query(Conversation).filter(
            Conversation.id == conversation_id
        ).first()
    
    @staticmethod
    def update_status(
        db: Session,
        conversation: Conversation,
        status: ConversationStatus
    ):
        conversation.status = status
        db.commit()
        db.refresh(conversation)
        return conversation