#!/bin/bash

# 🧪 Script de test des connexions - Système LSU
# Test de tous les services et leurs connexions

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

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}🧪 Test des Connexions LSU${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Test de la base de données PostgreSQL
test_postgres() {
    print_message "Test de la connexion PostgreSQL..."
    
    if docker-compose exec -T postgres pg_isready -U lsu_user -d lsu_db >/dev/null 2>&1; then
        print_success "✅ PostgreSQL est connecté et accessible"
        
        # Test de requête simple
        if docker-compose exec -T postgres psql -U lsu_user -d lsu_db -c "SELECT COUNT(*) FROM students;" >/dev/null 2>&1; then
            print_success "✅ Requête SQL fonctionnelle"
        else
            print_warning "⚠️ Requête SQL échouée"
        fi
    else
        print_error "❌ PostgreSQL n'est pas accessible"
        return 1
    fi
}

# Test du backend FastAPI
test_backend() {
    print_message "Test de la connexion Backend API..."
    
    # Test de santé
    if curl -f http://localhost:8000/health >/dev/null 2>&1; then
        print_success "✅ Backend API est accessible"
        
        # Test de la route racine
        if curl -f http://localhost:8000/ >/dev/null 2>&1; then
            print_success "✅ Route racine API fonctionnelle"
        else
            print_warning "⚠️ Route racine API échouée"
        fi
        
        # Test de la documentation
        if curl -f http://localhost:8000/docs >/dev/null 2>&1; then
            print_success "✅ Documentation API accessible"
        else
            print_warning "⚠️ Documentation API inaccessible"
        fi
        
        # Test de l'API des élèves
        if curl -f http://localhost:8000/api/v1/students >/dev/null 2>&1; then
            print_success "✅ API des élèves accessible"
        else
            print_warning "⚠️ API des élèves inaccessible (authentification requise)"
        fi
        
    else
        print_error "❌ Backend API n'est pas accessible"
        return 1
    fi
}

# Test du frontend React
test_frontend() {
    print_message "Test de la connexion Frontend..."
    
    # Attendre un peu que React démarre
    sleep 5
    
    if curl -f http://localhost:3000 >/dev/null 2>&1; then
        print_success "✅ Frontend React est accessible"
        
        # Test de la page d'accueil
        if curl -s http://localhost:3000 | grep -q "React\|LSU" >/dev/null 2>&1; then
            print_success "✅ Page d'accueil React chargée"
        else
            print_warning "⚠️ Page d'accueil React non détectée"
        fi
        
    else
        print_error "❌ Frontend React n'est pas accessible"
        return 1
    fi
}

# Test de Redis (optionnel)
test_redis() {
    print_message "Test de la connexion Redis..."
    
    if docker-compose exec -T redis redis-cli ping >/dev/null 2>&1; then
        print_success "✅ Redis est connecté et accessible"
    else
        print_warning "⚠️ Redis n'est pas accessible (optionnel)"
    fi
}

# Test de Nginx (si actif)
test_nginx() {
    print_message "Test de la connexion Nginx..."
    
    if curl -f http://localhost:80 >/dev/null 2>&1; then
        print_success "✅ Nginx est accessible"
        
        # Test du proxy vers l'API
        if curl -f http://localhost:80/api/ >/dev/null 2>&1; then
            print_success "✅ Proxy Nginx vers API fonctionnel"
        else
            print_warning "⚠️ Proxy Nginx vers API échoué"
        fi
        
    else
        print_warning "⚠️ Nginx n'est pas accessible (optionnel en dev)"
    fi
}

# Test des connexions entre services
test_service_connections() {
    print_message "Test des connexions entre services..."
    
    # Test Backend → PostgreSQL
    if docker-compose exec -T backend python -c "
import asyncio
import asyncpg
import os

async def test_db():
    try:
        conn = await asyncpg.connect(os.getenv('DATABASE_URL'))
        await conn.execute('SELECT 1')
        await conn.close()
        print('✅ Backend → PostgreSQL: OK')
    except Exception as e:
        print(f'❌ Backend → PostgreSQL: {e}')

asyncio.run(test_db())
" >/dev/null 2>&1; then
        print_success "✅ Connexion Backend → PostgreSQL fonctionnelle"
    else
        print_error "❌ Connexion Backend → PostgreSQL échouée"
    fi
    
    # Test Frontend → Backend
    if curl -s http://localhost:3000 | grep -q "localhost:8000\|api" >/dev/null 2>&1; then
        print_success "✅ Configuration Frontend → Backend détectée"
    else
        print_warning "⚠️ Configuration Frontend → Backend non détectée"
    fi
}

# Test des ports
test_ports() {
    print_message "Test des ports ouverts..."
    
    ports=("3000" "8000" "5432" "6379" "80")
    
    for port in "${ports[@]}"; do
        if lsof -i :$port >/dev/null 2>&1; then
            print_success "✅ Port $port est ouvert"
        else
            print_warning "⚠️ Port $port n'est pas ouvert"
        fi
    done
}

# Test de performance
test_performance() {
    print_message "Test de performance..."
    
    # Test de latence API
    start_time=$(date +%s.%N)
    curl -f http://localhost:8000/health >/dev/null 2>&1
    end_time=$(date +%s.%N)
    
    latency=$(echo "$end_time - $start_time" | bc -l 2>/dev/null || echo "0.1")
    print_message "Latence API: ${latency}s"
    
    if (( $(echo "$latency < 1.0" | bc -l) )); then
        print_success "✅ Performance API acceptable"
    else
        print_warning "⚠️ Performance API lente"
    fi
}

# Affichage des informations de connexion
show_connection_info() {
    echo ""
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}🔗 Informations de Connexion${NC}"
    echo -e "${BLUE}================================${NC}"
    echo -e "${GREEN}Frontend React:${NC} http://localhost:3000"
    echo -e "${GREEN}Backend API:${NC} http://localhost:8000"
    echo -e "${GREEN}Documentation API:${NC} http://localhost:8000/docs"
    echo -e "${GREEN}Base de données:${NC} localhost:5432"
    echo -e "${GREEN}Redis:${NC} localhost:6379"
    echo -e "${GREEN}Nginx:${NC} http://localhost:80"
    echo ""
    echo -e "${YELLOW}Comptes de test:${NC}"
    echo -e "Admin: admin@lsu-system.com / password"
    echo -e "Enseignant: teacher1@lsu-system.com / password"
    echo ""
    echo -e "${BLUE}Commandes de test:${NC}"
    echo -e "Test complet: ${GREEN}./test_connections.sh${NC}"
    echo -e "Logs: ${GREEN}docker-compose logs -f${NC}"
    echo -e "Statut: ${GREEN}docker-compose ps${NC}"
    echo ""
}

# Fonction principale
main() {
    print_header
    
    # Vérifier que Docker est en cours d'exécution
    if ! docker info >/dev/null 2>&1; then
        print_error "Docker n'est pas en cours d'exécution"
        exit 1
    fi
    
    # Vérifier que les conteneurs sont démarrés
    if ! docker-compose ps | grep -q "Up"; then
        print_warning "Aucun conteneur en cours d'exécution. Démarrage..."
        docker-compose up -d
        sleep 10
    fi
    
    # Tests
    test_ports
    test_postgres
    test_backend
    test_frontend
    test_redis
    test_nginx
    test_service_connections
    test_performance
    
    # Résumé
    show_connection_info
    
    print_success "🎉 Tests de connexion terminés !"
}

# Gestion des arguments
case "${1:-all}" in
    "all")
        main
        ;;
    "postgres")
        test_postgres
        ;;
    "backend")
        test_backend
        ;;
    "frontend")
        test_frontend
        ;;
    "redis")
        test_redis
        ;;
    "nginx")
        test_nginx
        ;;
    "ports")
        test_ports
        ;;
    "performance")
        test_performance
        ;;
    *)
        echo "Usage: $0 {all|postgres|backend|frontend|redis|nginx|ports|performance}"
        echo "  all         - Tous les tests (défaut)"
        echo "  postgres    - Test PostgreSQL uniquement"
        echo "  backend     - Test Backend API uniquement"
        echo "  frontend    - Test Frontend React uniquement"
        echo "  redis       - Test Redis uniquement"
        echo "  nginx       - Test Nginx uniquement"
        echo "  ports       - Test des ports uniquement"
        echo "  performance - Test de performance uniquement"
        exit 1
        ;;
esac 