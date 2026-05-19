from sqlalchemy import Column, Integer, String
from app.config.database import Base
from sqlalchemy.orm import relationship
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    conversations = relationship(
    "Conversation",
    back_populates="contact"
    )