"""
Routeur principal de l'API v1
Regroupement de toutes les routes de l'application
"""

from fastapi import APIRouter

from app.api.v1.endpoints import students, competences, comments, evaluations, users, ai

# Création du routeur principal
api_router = APIRouter()

# Inclusion des routeurs spécifiques
api_router.include_router(
    students.router,
    prefix="/students",
    tags=["Élèves"]
)

api_router.include_router(
    competences.router,
    prefix="/competences",
    tags=["Compétences"]
)

api_router.include_router(
    comments.router,
    prefix="/comments",
    tags=["Commentaires"]
)

api_router.include_router(
    evaluations.router,
    prefix="/evaluations",
    tags=["Évaluations"]
)

api_router.include_router(
    users.router,
    prefix="/users",
    tags=["Utilisateurs"]
)

api_router.include_router(
    ai.router,
    prefix="/ai",
    tags=["Intelligence Artificielle"]
) 