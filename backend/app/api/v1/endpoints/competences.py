"""
Endpoints pour la gestion des compétences
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.models.competence import Competence
from app.schemas.competence import CompetenceCreate, CompetenceResponse

router = APIRouter()

@router.get("/", response_model=List[CompetenceResponse])
async def get_competences(db: AsyncSession = Depends(get_db)):
    """Récupérer toutes les compétences"""
    # TODO: Implémenter la logique
    return []

@router.post("/", response_model=CompetenceResponse)
async def create_competence(
    competence: CompetenceCreate,
    db: AsyncSession = Depends(get_db)
):
    """Créer une nouvelle compétence"""
    # TODO: Implémenter la logique
    return competence 