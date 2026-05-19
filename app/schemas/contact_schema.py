from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    nome: str
    telefone: int
    email: EmailStr

class ContactUpdate(BaseModel):
    nome: str
    telefone: int
    email: EmailStr