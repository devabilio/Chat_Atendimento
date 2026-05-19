import enum

class ConversationStatus(str, enum.Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    CLOSED = "CLOSED"

class SenderType(str, enum.Enum):
    CLIENT = "CLIENT"
    AGENT = "AGENT"
    BOT = "BOT"