from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Enum,
    Text,
    DateTime
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.models.enums import SenderType

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id"),
        nullable=False
    )
    content = Column(
        Text,
        nullable=False
    )
    sender_type = Column(
        Enum(SenderType),
        nullable=False
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    conversation = relationship(
    "Conversation",
    back_populates="messages"
    )
