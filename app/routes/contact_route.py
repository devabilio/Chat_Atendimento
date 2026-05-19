from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.contact_schema import (
    ContactCreate,
    ContactUpdate
)

from app.config.database import get_db
from app.schemas.contact_schema import ContactCreate
from app.services.contact_service import ContactService

router = APIRouter(
    prefix="/contacts",
    tags=["Contacts"]
)

@router.post("/")
def create_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db)
):
    return ContactService.create_contact(db, contact)

@router.get("/")
def get_contacts(
    db:Session = Depends(get_db)
):
    
    return ContactService.get_contacts(db)

@router.get("/{contact_id}")
def get_contact_by_id(
    contact_id: int,
    db: Session = Depends(get_db)
):
    
    return ContactService.get_contact_by_id(
        db,
        contact_id
    )

@router.delete("/{contact_id}")
def delete_contact(
    contact_id: int,
    db: Session = Depends(get_db)
):
    return ContactService.delete_contact(
        db,
        contact_id
    )

@router.put("/{contact_id}")
def update_contact(
    contact_id: int,
    contact: ContactUpdate,
    db: Session = Depends(get_db)
):
    return ContactService.update_contact(
        db,
        contact_id,
        contact
    )