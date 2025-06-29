"""
Endpoints pour la gestion des utilisateurs
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_users(db: AsyncSession = Depends(get_db)):
    """Récupérer tous les utilisateurs"""
    # TODO: Implémenter la logique
    return []


@router.post("/")
async def create_user(db: AsyncSession = Depends(get_db)):
    """Créer un nouvel utilisateur"""
    # TODO: Implémenter la logique
    return {"message": "Utilisateur créé"} 