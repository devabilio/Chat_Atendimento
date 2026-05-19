from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/metrics")
def get_metrics(
    db: Session = Depends(get_db)
):
    data = DashboardService.get_metrics(db)

    return {
        "total_contacts": data["total_contacts"],
        "total_conversations": data["total_conversations"],
        "open_conversations": data["open_conversations"],
        "closed_conversations": data["closed_conversations"],
        "total_messages": data["total_messages"]
    }