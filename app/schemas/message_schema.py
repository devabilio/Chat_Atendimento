from pydantic import BaseModel
from app.models.enums import SenderType
from datetime import datetime

class MessageCreate(BaseModel):
    conversation_id: int
    content: str
    sender_type: SenderType

class MessageResponse(BaseModel):
    id: int
    content: str
    sender_type: SenderType
    created_at: datetime
    class Config:
        from_attributes = True