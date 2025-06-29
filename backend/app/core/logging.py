"""
Configuration du système de logging
Structlog pour un logging structuré et performant
"""

import structlog
import logging
import sys
from typing import Any, Dict
from app.core.config import settings


def setup_logging():
    """Configuration du système de logging"""
    
    # Configuration de base
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.LOG_LEVEL.upper())
    )
    
    # Configuration Structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_logger(name: str = None) -> structlog.BoundLogger:
    """Obtenir un logger configuré"""
    return structlog.get_logger(name)


def log_request(request_data: Dict[str, Any], logger: structlog.BoundLogger = None):
    """Logger une requête HTTP"""
    if logger is None:
        logger = get_logger("http")
    
    logger.info(
        "Requête HTTP",
        method=request_data.get("method"),
        url=request_data.get("url"),
        client_ip=request_data.get("client_ip"),
        user_agent=request_data.get("user_agent")
    )


def log_error(error: Exception, context: Dict[str, Any] = None, logger: structlog.BoundLogger = None):
    """Logger une erreur avec contexte"""
    if logger is None:
        logger = get_logger("error")
    
    error_data = {
        "error_type": type(error).__name__,
        "error_message": str(error),
        "context": context or {}
    }
    
    logger.error("Erreur application", **error_data) 