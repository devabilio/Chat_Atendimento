from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Enum
)
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.models.enums import ConversationStatus

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(
        Integer,
        ForeignKey("contacts.id"),
        nullable=False
    )
    status = Column(
        Enum(ConversationStatus),
        default=ConversationStatus.OPEN
    )
    contact = relationship(
    "Contact",
    back_populates="conversations"
    )
    messages = relationship(
    "Message",
    back_populates="conversation"
    )