"""
Endpoints pour la gestion des élèves
"""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_students(db: AsyncSession = Depends(get_db)):
    """Récupérer tous les élèves"""
    # TODO: Implémenter la logique
    return []


@router.post("/")
async def create_student(db: AsyncSession = Depends(get_db)):
    """Créer un nouvel élève"""
    # TODO: Implémenter la logique
    return {"message": "Élève créé"}


@router.get("/{student_id}")
async def get_student(student_id: int, db: AsyncSession = Depends(get_db)):
    """Récupérer un élève par son ID"""
    # TODO: Implémenter la logique
    return {"id": student_id, "message": "Élève trouvé"} 