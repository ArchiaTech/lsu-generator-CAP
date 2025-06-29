"""
Modèle Competence - Évaluation des compétences LSU
"""

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from typing import Optional

from app.core.database import Base


class CompetenceLevel(enum.Enum):
    """Niveaux de compétence LSU"""
    INSUFFISANT = "insuffisant"
    FRAGILE = "fragile"
    SATISFAISANT = "satisfaisant"
    EXCELLENT = "excellent"


class CompetenceDomain(enum.Enum):
    """Domaines de compétences"""
    FRANCAIS_LECTURE = "francais_lecture"
    FRANCAIS_ECRITURE = "francais_ecriture"
    FRANCAIS_ORAL = "francais_oral"
    MATHS_CALCUL = "maths_calcul"
    MATHS_GEOMETRIE = "maths_geometrie"
    MATHS_RESOLUTION = "maths_resolution"
    SCIENCES = "sciences"
    HISTOIRE_GEO = "histoire_geo"
    ARTS = "arts"
    EPS = "eps"
    LANGUE_VIVANTE = "langue_vivante"
    COMPETENCES_SOCIALES = "competences_sociales"


class Competence(Base):
    """Modèle pour les compétences des élèves"""
    
    __tablename__ = "competences"
    
    # Identifiant principal
    id = Column(Integer, primary_key=True, index=True)
    
    # Relations
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False, index=True)
    
    # Informations de la compétence
    domain = Column(Enum(CompetenceDomain), nullable=False, index=True)
    subdomain = Column(String(100), nullable=True)  # Sous-domaine spécifique
    
    # Évaluation
    level = Column(Enum(CompetenceLevel), nullable=False, index=True)
    score = Column(Integer, nullable=True)  # Score numérique (1-4)
    
    # Commentaires
    comment = Column(Text, nullable=True)  # Commentaire détaillé
    strengths = Column(Text, nullable=True)  # Points forts observés
    difficulties = Column(Text, nullable=True)  # Difficultés identifiées
    
    # Contexte d'évaluation
    evaluation_date = Column(DateTime(timezone=True), nullable=False, index=True)
    period = Column(String(50), nullable=False, index=True)  # 1er trimestre, 2ème trimestre, etc.
    evaluator_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Métadonnées
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    student = relationship("Student", back_populates="competences")
    evaluator = relationship("User")
    
    def __repr__(self):
        return f"<Competence(id={self.id}, student_id={self.student_id}, domain='{self.domain}', level='{self.level}')>"
    
    @property
    def level_color(self) -> str:
        """Couleur associée au niveau"""
        colors = {
            CompetenceLevel.INSUFFISANT: "#f44336",  # Rouge
            CompetenceLevel.FRAGILE: "#ff9800",      # Orange
            CompetenceLevel.SATISFAISANT: "#4CAF50", # Vert
            CompetenceLevel.EXCELLENT: "#2196F3"     # Bleu
        }
        return colors.get(self.level, "#999999")
    
    @property
    def level_text(self) -> str:
        """Texte du niveau en français"""
        texts = {
            CompetenceLevel.INSUFFISANT: "Maîtrise insuffisante",
            CompetenceLevel.FRAGILE: "Maîtrise fragile",
            CompetenceLevel.SATISFAISANT: "Maîtrise satisfaisante",
            CompetenceLevel.EXCELLENT: "Très bonne maîtrise"
        }
        return texts.get(self.level, "Non évalué")
    
    def to_dict(self) -> dict:
        """Conversion en dictionnaire"""
        return {
            "id": self.id,
            "student_id": self.student_id,
            "domain": self.domain.value,
            "subdomain": self.subdomain,
            "level": self.level.value,
            "level_text": self.level_text,
            "level_color": self.level_color,
            "score": self.score,
            "comment": self.comment,
            "strengths": self.strengths,
            "difficulties": self.difficulties,
            "evaluation_date": self.evaluation_date.isoformat() if self.evaluation_date else None,
            "period": self.period,
            "evaluator_id": self.evaluator_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        } 