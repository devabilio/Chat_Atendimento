from pydantic import BaseModel
from app.models.enums import ConversationStatus

class ConversationCreate(BaseModel):
    contact_id: int

class ConversationResponse(BaseModel):
    id: int
    contact_id: int
    status: ConversationStatus
    class Config:
        from_attributes = True

class ConversationStatusUpdate(BaseModel):
    status: ConversationStatus