"""
Configuration de l'application LSU
Gestion des variables d'environnement avec Pydantic Settings
"""

from pydantic_settings import BaseSettings
from typing import List, Optional
import os


class Settings(BaseSettings):
    """Configuration de l'application"""
    
    # Informations de base
    APP_NAME: str = "Système de Gestion LSU"
    VERSION: str = "1.0.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # Base de données
    DATABASE_URL: str = "postgresql://lsu_user:lsu_password@localhost:5432/lsu_db"
    POSTGRES_DB: str = "lsu_db"
    POSTGRES_USER: str = "lsu_user"
    POSTGRES_PASSWORD: str = "lsu_password"
    
    # Sécurité
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS et hôtes autorisés
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8080"
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # IA (optionnel)
    OPENAI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    AI_MODEL: str = "gpt-4"
    AI_MAX_TOKENS: int = 1000
    AI_TEMPERATURE: float = 0.7
    
    # Email (optionnel)
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: int = 587
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAIL_FROM: str = "noreply@lsu-system.com"
    
    # Redis (optionnel)
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = 0
    
    # Logs
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/lsu-system.log"
    
    # Backup
    BACKUP_ENABLED: bool = True
    BACKUP_RETENTION_DAYS: int = 30
    BACKUP_PATH: str = "./backups"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Instance globale des paramètres
settings = Settings() 