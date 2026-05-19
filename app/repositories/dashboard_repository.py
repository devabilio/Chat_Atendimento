from sqlalchemy.orm import Session
from app.models.contact_model import Contact
from app.models.conversation_model import Conversation
from app.models.message_model import Message
from app.models.enums import ConversationStatus

class DashboardRepository:
    @staticmethod
    def get_metrics(db: Session):
        total_contacts = int(
            db.query(Contact).count()
        )
        total_conversations = int(
            db.query(Conversation).count()
        )
        open_conversations = int(
            db.query(Conversation).filter(
                Conversation.status == ConversationStatus.OPEN
            ).count()
        )
        closed_conversations = int(
            db.query(Conversation).filter(
                Conversation.status == ConversationStatus.CLOSED
            ).count()
        )
        total_messages = int(
            db.query(Message).count()
        )
        return {
            "total_contacts": total_contacts,
            "total_conversations": total_conversations,
            "open_conversations": open_conversations,
            "closed_conversations": closed_conversations,
            "total_messages": total_messages
        }