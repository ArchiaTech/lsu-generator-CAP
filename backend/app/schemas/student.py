"""
Schémas Pydantic pour les élèves
Validation et sérialisation des données
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import date, datetime
from enum import Enum


class GenderEnum(str, Enum):
    """Enum pour le genre"""
    MALE = "M"
    FEMALE = "F"
    OTHER = "Autre"


class LevelEnum(str, Enum):
    """Enum pour les niveaux scolaires"""
    CP = "CP"
    CE1 = "CE1"
    CE2 = "CE2"
    CM1 = "CM1"
    CM2 = "CM2"


class StudentBase(BaseModel):
    """Schéma de base pour les élèves"""
    first_name: str = Field(..., min_length=1, max_length=100, description="Prénom")
    last_name: str = Field(..., min_length=1, max_length=100, description="Nom")
    birth_date: Optional[date] = Field(None, description="Date de naissance")
    gender: Optional[GenderEnum] = Field(None, description="Genre")
    level: LevelEnum = Field(..., description="Niveau scolaire")
    class_name: Optional[str] = Field(None, max_length=50, description="Classe")
    school_year: str = Field(..., regex=r"^\d{4}-\d{4}$", description="Année scolaire")
    
    # Informations de contact
    address: Optional[str] = Field(None, description="Adresse")
    phone: Optional[str] = Field(None, max_length=20, description="Téléphone")
    email: Optional[str] = Field(None, max_length=100, description="Email")
    
    # Informations familiales
    parent1_name: Optional[str] = Field(None, max_length=100, description="Nom parent 1")
    parent1_phone: Optional[str] = Field(None, max_length=20, description="Téléphone parent 1")
    parent1_email: Optional[str] = Field(None, max_length=100, description="Email parent 1")
    parent1_profession: Optional[str] = Field(None, max_length=100, description="Profession parent 1")
    
    parent2_name: Optional[str] = Field(None, max_length=100, description="Nom parent 2")
    parent2_phone: Optional[str] = Field(None, max_length=20, description="Téléphone parent 2")
    parent2_email: Optional[str] = Field(None, max_length=100, description="Email parent 2")
    parent2_profession: Optional[str] = Field(None, max_length=100, description="Profession parent 2")
    
    # Points forts et difficultés
    strengths: Optional[str] = Field(None, description="Points forts")
    difficulties: Optional[str] = Field(None, description="Difficultés")
    objectives: Optional[str] = Field(None, description="Objectifs")
    notes: Optional[str] = Field(None, description="Notes privées")


class StudentCreate(StudentBase):
    """Schéma pour la création d'un élève"""
    pass


class StudentUpdate(BaseModel):
    """Schéma pour la mise à jour d'un élève"""
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    birth_date: Optional[date] = None
    gender: Optional[GenderEnum] = None
    level: Optional[LevelEnum] = None
    class_name: Optional[str] = Field(None, max_length=50)
    school_year: Optional[str] = Field(None, regex=r"^\d{4}-\d{4}$")
    
    # Informations de contact
    address: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = Field(None, max_length=100)
    
    # Informations familiales
    parent1_name: Optional[str] = Field(None, max_length=100)
    parent1_phone: Optional[str] = Field(None, max_length=20)
    parent1_email: Optional[str] = Field(None, max_length=100)
    parent1_profession: Optional[str] = Field(None, max_length=100)
    
    parent2_name: Optional[str] = Field(None, max_length=100)
    parent2_phone: Optional[str] = Field(None, max_length=20)
    parent2_email: Optional[str] = Field(None, max_length=100)
    parent2_profession: Optional[str] = Field(None, max_length=100)
    
    # Points forts et difficultés
    strengths: Optional[str] = None
    difficulties: Optional[str] = None
    objectives: Optional[str] = None
    notes: Optional[str] = None


class StudentResponse(StudentBase):
    """Schéma de réponse pour un élève"""
    id: int
    full_name: str
    age: Optional[int] = None
    teacher_id: Optional[int] = None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class StudentListResponse(BaseModel):
    """Schéma de réponse pour la liste des élèves"""
    id: int
    first_name: str
    last_name: str
    full_name: str
    level: str
    class_name: Optional[str] = None
    school_year: str
    is_active: bool
    age: Optional[int] = None
    
    class Config:
        from_attributes = True


class StudentStats(BaseModel):
    """Statistiques d'un élève"""
    total_competences: int
    total_evaluations: int
    total_comments: int
    average_level: Optional[float] = None
    progress_rate: Optional[float] = None


class StudentSearch(BaseModel):
    """Paramètres de recherche d'élèves"""
    search: Optional[str] = None
    level: Optional[str] = None
    class_name: Optional[str] = None
    school_year: Optional[str] = None
    is_active: Optional[bool] = None
    teacher_id: Optional[int] = None 