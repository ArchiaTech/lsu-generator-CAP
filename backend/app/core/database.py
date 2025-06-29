"""
Configuration de la base de données
SQLAlchemy avec support PostgreSQL asynchrone
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import structlog

from app.core.config import settings

logger = structlog.get_logger()

# Conversion de l'URL PostgreSQL pour async
async_database_url = settings.DATABASE_URL.replace(
    "postgresql://", "postgresql+asyncpg://"
)

# Création du moteur asynchrone
engine = create_async_engine(
    async_database_url,
    echo=settings.DEBUG,
    poolclass=NullPool if settings.DEBUG else None,
    pool_pre_ping=True,
    pool_recycle=300,
)

# Session factory asynchrone
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base pour les modèles
Base = declarative_base()


async def get_db() -> AsyncSession:
    """Dependency pour obtenir une session de base de données"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Erreur de session DB: {e}")
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    """Initialisation de la base de données"""
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Base de données initialisée avec succès")
    except Exception as e:
        logger.error(f"❌ Erreur d'initialisation de la base de données: {e}")
        raise


async def close_db():
    """Fermeture de la connexion à la base de données"""
    try:
        await engine.dispose()
        logger.info("✅ Connexion à la base de données fermée")
    except Exception as e:
        logger.error(f"❌ Erreur de fermeture de la base de données: {e}") 