from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.contact_repository import ContactRepository
from app.schemas.contact_schema import ContactCreate
from app.schemas.contact_schema import (
    ContactCreate,
    ContactUpdate
)

class ContactService:
    @staticmethod
    def create_contact(db: Session, contact: ContactCreate):

        return ContactRepository.create(db, contact)
    
    @staticmethod
    def get_contacts(db: Session):

        return ContactRepository.get_all(db)
    
    @staticmethod
    def get_contact_by_id(
        db: Session,
        contact_id: int
    ):
        contact = ContactRepository.get_by_id(
            db,
            contact_id
        )
        if not contact:
            raise HTTPException(
                status_code=404,
                detail="Contato não encontrado"
            )
        return contact
    
    @staticmethod
    def delete_contact(
        db: Session,
        contact_id: int
    ):
        contact =  ContactRepository.get_by_id(
            db,
            contact_id
        )
        if not contact:
            raise HTTPException(
                status_code=404,
                detail="Contato não encontrado"
            )
        ContactRepository.delete(
            db,
            contact
        )
        return {
            "mensagem": "Contato deletado com sucesso"
        }
    @staticmethod
    def update_contact(
        db: Session,
        contact_id: int,
        contact_data: ContactUpdate
    ):
        contact = ContactRepository.get_by_id(
            db,
            contact_id
        )
        if not contact:
            raise HTTPException(
                status_code=404,
                detail="Contato não encontrado"
            )
        return ContactRepository.update(
            db,
            contact,
            contact_data
        )