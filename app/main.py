from fastapi import FastAPI

from app.config.database import (
    Base,
    engine
)

from app.routes.contact_route import (
    router as contact_router
)

from app.routes.conversation_route import (
    router as conversation_router
)

from app.routes.message_route import (
    router as message_router
)

from app.routes.dashboard_route import (
    router as dashboard_router
)

from app.routes.user_route import (
    router as user_router
)

app = FastAPI()

app.include_router(contact_router)
app.include_router(conversation_router)
app.include_router(message_router)
app.include_router(dashboard_router)
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "message": "API running"
    }