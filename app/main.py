from fastapi import FastAPI

from app.config.database import Base, engine
from app.models.contact_model import Contact
from app.routes.contact_route import router as contact_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contact_router)

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}
