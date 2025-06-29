"""
🎓 Système de Gestion LSU - API Backend
Application FastAPI pour la gestion d'élèves et génération de commentaires LSU
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import structlog
import os
from typing import List

from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.api import api_router
from app.core.logging import setup_logging

# Configuration du logging
setup_logging()
logger = structlog.get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestion du cycle de vie de l'application"""
    # Startup
    logger.info("🚀 Démarrage de l'application LSU")
    
    # Création des tables si elles n'existent pas
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Base de données initialisée")
    except Exception as e:
        logger.error(f"❌ Erreur d'initialisation de la base de données: {e}")
    
    yield
    
    # Shutdown
    logger.info("🛑 Arrêt de l'application LSU")

# Création de l'application FastAPI
app = FastAPI(
    title="🎓 Système de Gestion LSU",
    description="API pour la gestion d'élèves et génération de commentaires LSU",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration des hôtes de confiance (production)
if settings.ENVIRONMENT == "production":
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )

# Inclusion des routes API
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    """Route racine de l'API"""
    return {
        "message": "🎓 Système de Gestion LSU - API Backend",
        "version": "1.0.0",
        "status": "online",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    """Vérification de l'état de santé de l'API"""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "database": "connected" if engine else "disconnected"
    }

@app.get("/api")
async def api_info():
    """Informations sur l'API"""
    return {
        "name": "LSU Management System API",
        "version": "1.0.0",
        "description": "API pour la gestion d'élèves et génération de commentaires LSU",
        "endpoints": {
            "students": "/api/v1/students",
            "competences": "/api/v1/competences",
            "comments": "/api/v1/comments",
            "evaluations": "/api/v1/evaluations",
            "users": "/api/v1/users",
            "ai": "/api/v1/ai"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info"
    ) 