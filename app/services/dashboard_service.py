from sqlalchemy.orm import Session
from app.repositories.dashboard_repository import (
    DashboardRepository
)

class DashboardService:
    @staticmethod
    def get_metrics(db: Session):
        return DashboardRepository.get_metrics(db)