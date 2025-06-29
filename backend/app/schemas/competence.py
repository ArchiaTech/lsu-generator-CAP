"""
Schémas Pydantic pour les compétences
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CompetenceBase(BaseModel):
    """Schéma de base pour les compétences"""
    nom: str
    description: Optional[str] = None
    domaine: str
    niveau: str


class CompetenceCreate(CompetenceBase):
    """Schéma pour créer une compétence"""
    pass


class CompetenceResponse(CompetenceBase):
    """Schéma pour la réponse d'une compétence"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 