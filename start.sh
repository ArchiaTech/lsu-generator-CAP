#!/bin/bash

# 🎓 Script de démarrage du Système de Gestion LSU
# Démarrage rapide avec Docker Compose

set -e

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Fonction pour afficher les messages
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}🎓 Système de Gestion LSU${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Vérification de Docker
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker n'est pas installé. Veuillez l'installer d'abord."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose n'est pas installé. Veuillez l'installer d'abord."
        exit 1
    fi
    
    print_message "Docker et Docker Compose sont installés"
}

# Vérification des fichiers de configuration
check_config() {
    if [ ! -f "docker-compose.yml" ]; then
        print_error "Fichier docker-compose.yml manquant"
        exit 1
    fi
    
    if [ ! -f "env.example" ]; then
        print_error "Fichier env.example manquant"
        exit 1
    fi
    
    # Création du fichier .env s'il n'existe pas
    if [ ! -f ".env" ]; then
        print_warning "Fichier .env manquant, création depuis env.example"
        cp env.example .env
        print_message "Fichier .env créé. Veuillez le configurer selon vos besoins."
    fi
    
    print_message "Configuration vérifiée"
}

# Nettoyage des conteneurs existants
cleanup() {
    print_message "Nettoyage des conteneurs existants..."
    docker-compose down --remove-orphans 2>/dev/null || true
    print_message "Nettoyage terminé"
}

# Démarrage des services
start_services() {
    print_message "Démarrage des services..."
    
    # Build des images
    print_message "Construction des images Docker..."
    docker-compose build --no-cache
    
    # Démarrage des services
    print_message "Démarrage des conteneurs..."
    docker-compose up -d
    
    print_message "Services démarrés avec succès"
}

# Vérification de l'état des services
check_services() {
    print_message "Vérification de l'état des services..."
    
    # Attendre que les services soient prêts
    sleep 10
    
    # Vérifier PostgreSQL
    if docker-compose exec -T postgres pg_isready -U lsu_user -d lsu_db >/dev/null 2>&1; then
        print_message "✅ PostgreSQL est prêt"
    else
        print_warning "⚠️ PostgreSQL n'est pas encore prêt"
    fi
    
    # Vérifier le backend
    if curl -f http://localhost:8000/health >/dev/null 2>&1; then
        print_message "✅ Backend API est prêt"
    else
        print_warning "⚠️ Backend API n'est pas encore prêt"
    fi
    
    # Vérifier le frontend
    if curl -f http://localhost:3000 >/dev/null 2>&1; then
        print_message "✅ Frontend est prêt"
    else
        print_warning "⚠️ Frontend n'est pas encore prêt"
    fi
}

# Affichage des informations d'accès
show_access_info() {
    echo ""
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}🌐 Accès à l'application${NC}"
    echo -e "${BLUE}================================${NC}"
    echo -e "${GREEN}Frontend:${NC} http://localhost:3000"
    echo -e "${GREEN}Backend API:${NC} http://localhost:8000"
    echo -e "${GREEN}Documentation API:${NC} http://localhost:8000/docs"
    echo -e "${GREEN}Base de données:${NC} localhost:5432"
    echo ""
    echo -e "${YELLOW}Comptes de test:${NC}"
    echo -e "Admin: admin@lsu-system.com / password"
    echo -e "Enseignant: teacher1@lsu-system.com / password"
    echo ""
    echo -e "${BLUE}Commandes utiles:${NC}"
    echo -e "Voir les logs: ${GREEN}docker-compose logs -f${NC}"
    echo -e "Arrêter: ${GREEN}docker-compose down${NC}"
    echo -e "Redémarrer: ${GREEN}docker-compose restart${NC}"
    echo ""
}

# Fonction principale
main() {
    print_header
    
    # Vérifications préalables
    check_docker
    check_config
    
    # Nettoyage
    cleanup
    
    # Démarrage
    start_services
    
    # Vérification
    check_services
    
    # Informations d'accès
    show_access_info
    
    print_message "🎉 Système LSU démarré avec succès !"
}

# Gestion des arguments
case "${1:-start}" in
    "start")
        main
        ;;
    "stop")
        print_message "Arrêt des services..."
        docker-compose down
        print_message "Services arrêtés"
        ;;
    "restart")
        print_message "Redémarrage des services..."
        docker-compose restart
        print_message "Services redémarrés"
        ;;
    "logs")
        docker-compose logs -f
        ;;
    "clean")
        print_message "Nettoyage complet..."
        docker-compose down -v --remove-orphans
        docker system prune -f
        print_message "Nettoyage terminé"
        ;;
    "build")
        print_message "Construction des images..."
        docker-compose build --no-cache
        print_message "Construction terminée"
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|logs|clean|build}"
        echo "  start   - Démarrer tous les services (défaut)"
        echo "  stop    - Arrêter tous les services"
        echo "  restart - Redémarrer tous les services"
        echo "  logs    - Afficher les logs en temps réel"
        echo "  clean   - Nettoyer complètement (supprime les volumes)"
        echo "  build   - Reconstruire les images Docker"
        exit 1
        ;;
esac 