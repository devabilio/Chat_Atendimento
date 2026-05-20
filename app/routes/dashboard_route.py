from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.repositories.dashboard_repository import (
    DashboardRepository
)
from app.auth.dependencies import (
    get_current_user
)
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/metrics")
def get_metrics(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    data = DashboardRepository.get_metrics(db)

    return {
        "total_contacts": data["total_contacts"],
        "total_conversations": data["total_conversations"],
        "open_conversations": data["open_conversations"],
        "closed_conversations": data["closed_conversations"],
        "total_messages": data["total_messages"]
    }