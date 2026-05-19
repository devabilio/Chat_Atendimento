from sqlalchemy.orm import Session

from app.models.contact_model import Contact
from app.schemas.contact_schema import ContactCreate

class ContactRepository:

    @staticmethod
    def create(db: Session, contact: ContactCreate):
        new_contact = Contact(
            nome=contact.nome,
            telefone=contact.telefone,
            email=contact.email
        )
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)
        return new_contact

    @staticmethod
    def get_all(db: Session):

        return db.query(Contact).all()
    
    @staticmethod
    def get_by_id(db: Session, contact_id: int):

        return db.query(Contact).filter(
            Contact.id == contact_id
        ).first()

    @staticmethod
    def delete(
        db: Session,
        contact: Contact
    ):
        db.delete(contact)
        db.commit()

    @staticmethod
    def update(
        db: Session,
        contact: Contact,
        contact_data
    ):
        contact.nome = contact_data.nome
        contact.telefone = contact_data.telefone
        contact.email = contact_data.email

        db.commit()
        db.refresh(contact)

        return contact
