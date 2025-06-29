"""
Modèle Student - Gestion des élèves
"""

from sqlalchemy import Column, Integer, String, Date, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import Optional

from app.core.database import Base


class Student(Base):
    """Modèle pour les élèves"""
    
    __tablename__ = "students"
    
    # Identifiant principal
    id = Column(Integer, primary_key=True, index=True)
    
    # Informations personnelles
    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    birth_date = Column(Date, nullable=True)
    gender = Column(String(10), nullable=True)  # M, F, Autre
    
    # Informations scolaires
    level = Column(String(20), nullable=False, index=True)  # CP, CE1, CE2, CM1, CM2
    class_name = Column(String(50), nullable=True)  # CM1-A, CE2-B, etc.
    school_year = Column(String(9), nullable=False)  # 2024-2025
    teacher_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Informations de contact
    address = Column(Text, nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    
    # Informations familiales
    parent1_name = Column(String(100), nullable=True)
    parent1_phone = Column(String(20), nullable=True)
    parent1_email = Column(String(100), nullable=True)
    parent1_profession = Column(String(100), nullable=True)
    
    parent2_name = Column(String(100), nullable=True)
    parent2_phone = Column(String(20), nullable=True)
    parent2_email = Column(String(100), nullable=True)
    parent2_profession = Column(String(100), nullable=True)
    
    # Points forts et difficultés
    strengths = Column(Text, nullable=True)  # JSON ou texte libre
    difficulties = Column(Text, nullable=True)  # JSON ou texte libre
    objectives = Column(Text, nullable=True)  # Objectifs du trimestre
    
    # Statut
    is_active = Column(Boolean, default=True, index=True)
    notes = Column(Text, nullable=True)  # Notes privées de l'enseignant
    
    # Métadonnées
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    teacher = relationship("User", back_populates="students")
    competences = relationship("Competence", back_populates="student")
    evaluations = relationship("Evaluation", back_populates="student")
    comments = relationship("Comment", back_populates="student")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}', level='{self.level}')>"
    
    @property
    def full_name(self) -> str:
        """Nom complet de l'élève"""
        return f"{self.first_name} {self.last_name}"
    
    @property
    def age(self) -> Optional[int]:
        """Âge de l'élève"""
        if self.birth_date:
            today = datetime.now().date()
            return today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
            )
        return None
    
    def to_dict(self) -> dict:
        """Conversion en dictionnaire"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "birth_date": self.birth_date.isoformat() if self.birth_date else None,
            "age": self.age,
            "gender": self.gender,
            "level": self.level,
            "class_name": self.class_name,
            "school_year": self.school_year,
            "teacher_id": self.teacher_id,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "parent1_name": self.parent1_name,
            "parent1_phone": self.parent1_phone,
            "parent1_email": self.parent1_email,
            "parent1_profession": self.parent1_profession,
            "parent2_name": self.parent2_name,
            "parent2_phone": self.parent2_phone,
            "parent2_email": self.parent2_email,
            "parent2_profession": self.parent2_profession,
            "strengths": self.strengths,
            "difficulties": self.difficulties,
            "objectives": self.objectives,
            "is_active": self.is_active,
            "notes": self.notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        } 