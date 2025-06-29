"""
Endpoints pour la gestion des commentaires
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_comments(db: AsyncSession = Depends(get_db)):
    """Récupérer tous les commentaires"""
    # TODO: Implémenter la logique
    return []


@router.post("/")
async def create_comment(db: AsyncSession = Depends(get_db)):
    """Créer un nouveau commentaire"""
    # TODO: Implémenter la logique
    return {"message": "Commentaire créé"} 