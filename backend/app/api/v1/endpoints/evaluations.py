"""
Endpoints pour la gestion des évaluations
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_evaluations(db: AsyncSession = Depends(get_db)):
    """Récupérer toutes les évaluations"""
    # TODO: Implémenter la logique
    return []


@router.post("/")
async def create_evaluation(db: AsyncSession = Depends(get_db)):
    """Créer une nouvelle évaluation"""
    # TODO: Implémenter la logique
    return {"message": "Évaluation créée"} 