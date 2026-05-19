from sqlalchemy.orm import Session
from app.models.message_model import Message
from app.schemas.message_schema import (
    MessageCreate
)

class MessageRepository:

    @staticmethod
    def create(
        db: Session,
        message: MessageCreate
    ):
        new_message = Message(
            conversation_id=message.conversation_id,
            content=message.content,
            sender_type=message.sender_type
        )

        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message
    
    @staticmethod
    def get_by_conversation(
        db: Session,
        conversation_id: int
    ):
        return db.query(Message).filter(
            Message.conversation_id == conversation_id
        ).order_by(
            Message.created_at.asc()
        ).all()