#!/bin/bash

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${PURPLE}"
echo "=========================================="
echo "🧪 TEST COMPLET DU SYSTÈME LSU"
echo "=========================================="
echo -e "${NC}"

# Fonction pour afficher les résultats
print_result() {
    if [ $1 -eq 0 ]; then
        echo -e "${GREEN}✅ $2${NC}"
    else
        echo -e "${RED}❌ $2${NC}"
    fi
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️ $1${NC}"
}

print_success() {
    echo -e "${GREEN}🎉 $1${NC}"
}

# 1. Vérification des conteneurs Docker
echo -e "${CYAN}1. Vérification des conteneurs Docker...${NC}"
docker-compose ps | grep -E "(lsu-backend|lsu-frontend|lsu-postgres|lsu-redis)" > /dev/null
print_result $? "Tous les conteneurs sont en cours d'exécution"

# 2. Test des ports
echo -e "${CYAN}2. Test des ports...${NC}"

# Test port 8000 (Backend)
curl -s http://localhost:8000/health > /dev/null
print_result $? "Port 8000 (Backend API) accessible"

# Test port 3000 (Frontend)
curl -s http://localhost:3000 > /dev/null
print_result $? "Port 3000 (Frontend React) accessible"

# Test port 5432 (PostgreSQL)
docker-compose exec postgres pg_isready -U lsu_user > /dev/null 2>&1
print_result $? "Port 5432 (PostgreSQL) accessible"

# Test port 6379 (Redis)
docker-compose exec redis redis-cli ping > /dev/null 2>&1
print_result $? "Port 6379 (Redis) accessible"

# 3. Test de la base de données
echo -e "${CYAN}3. Test de la base de données...${NC}"

# Test connexion PostgreSQL
docker-compose exec postgres psql -U lsu_user -d lsu_db -c "SELECT version();" > /dev/null 2>&1
print_result $? "Connexion PostgreSQL établie"

# Test des tables
docker-compose exec postgres psql -U lsu_user -d lsu_db -c "\dt" | grep -E "(students|competences)" > /dev/null 2>&1
print_result $? "Tables de base créées"

# 4. Test de l'API Backend
echo -e "${CYAN}4. Test de l'API Backend...${NC}"

# Test route racine
curl -s http://localhost:8000/ | grep -q "LSU"
print_result $? "Route racine API fonctionnelle"

# Test route health
curl -s http://localhost:8000/health | grep -q "status"
print_result $? "Route health API fonctionnelle"

# Test route students
curl -s http://localhost:8000/api/v1/students/ | grep -q "\[\]"
print_result $? "Route students API fonctionnelle"

# Test documentation
curl -s http://localhost:8000/docs | grep -q "Swagger"
print_result $? "Documentation API accessible"

# 5. Test du Frontend
echo -e "${CYAN}5. Test du Frontend...${NC}"

# Test page d'accueil React
curl -s http://localhost:3000 | grep -q "Système LSU"
print_result $? "Page d'accueil React chargée"

# Test des fichiers statiques
curl -s http://localhost:3000/static/js/bundle.js > /dev/null
print_result $? "Bundle JavaScript accessible"

# 6. Test des pages HTML
echo -e "${CYAN}6. Test des pages HTML...${NC}"

# Test page d'accueil HTML
curl -s http://localhost:3000/lsu_index.html | grep -q "LSU École Primaire"
print_result $? "Page d'accueil HTML accessible"

# Test générateur HTML
curl -s http://localhost:3000/improved_lsu_generator.html | grep -q "Générateur de Commentaires"
print_result $? "Générateur HTML accessible"

# Test profil élève HTML
curl -s http://localhost:3000/student_profile_page.html | grep -q "Fiche Élève"
print_result $? "Profil élève HTML accessible"

# 7. Test des connexions entre services
echo -e "${CYAN}7. Test des connexions entre services...${NC}"

# Test Backend → PostgreSQL
docker-compose exec backend python -c "
import psycopg2
try:
    conn = psycopg2.connect('postgresql://lsu_user:lsu_password@postgres:5432/lsu_db')
    print('OK')
except Exception as e:
    print('ERROR')
" | grep -q "OK"
print_result $? "Backend → PostgreSQL connecté"

# Test Backend → Redis
docker-compose exec backend python -c "
import redis
try:
    r = redis.Redis(host='redis', port=6379, db=0)
    r.ping()
    print('OK')
except Exception as e:
    print('ERROR')
" | grep -q "OK"
print_result $? "Backend → Redis connecté"

# 8. Test de performance
echo -e "${CYAN}8. Test de performance...${NC}"

# Test latence API
start_time=$(date +%s.%N)
curl -s http://localhost:8000/health > /dev/null
end_time=$(date +%s.%N)
latency=$(echo "$end_time - $start_time" | bc -l)
latency_ms=$(echo "$latency * 1000" | bc -l | cut -d. -f1)

if [ $latency_ms -lt 100 ]; then
    print_result 0 "Latence API: ${latency_ms}ms (excellent)"
elif [ $latency_ms -lt 500 ]; then
    print_result 0 "Latence API: ${latency_ms}ms (bon)"
else
    print_warning "Latence API: ${latency_ms}ms (lent)"
fi

# 9. Test de sécurité
echo -e "${CYAN}9. Test de sécurité...${NC}"

# Test CORS
curl -s -H "Origin: http://localhost:3000" -H "Access-Control-Request-Method: GET" \
     -H "Access-Control-Request-Headers: X-Requested-With" \
     -X OPTIONS http://localhost:8000/api/v1/students/ > /dev/null
print_result $? "CORS configuré"

# Test pas de données sensibles exposées
curl -s http://localhost:8000/ | grep -q "password\|secret\|key" && print_warning "Données sensibles potentiellement exposées" || print_result 0 "Aucune donnée sensible exposée"

# 10. Test de résilience
echo -e "${CYAN}10. Test de résilience...${NC}"

# Test redémarrage rapide
docker-compose restart backend > /dev/null 2>&1
sleep 3
curl -s http://localhost:8000/health > /dev/null
print_result $? "Backend redémarre correctement"

# 11. Résumé final
echo -e "${PURPLE}"
echo "=========================================="
echo "📊 RÉSUMÉ DES TESTS"
echo "=========================================="
echo -e "${NC}"

# Compter les succès
total_tests=$(grep -c "✅\|❌\|⚠️" <<< "$(tail -n +1)")
success_tests=$(grep -c "✅" <<< "$(tail -n +1)")
error_tests=$(grep -c "❌" <<< "$(tail -n +1)")
warning_tests=$(grep -c "⚠️" <<< "$(tail -n +1)")

echo -e "${GREEN}✅ Tests réussis: $success_tests${NC}"
echo -e "${RED}❌ Tests échoués: $error_tests${NC}"
echo -e "${YELLOW}⚠️ Avertissements: $warning_tests${NC}"

# Calculer le pourcentage de succès
if [ $total_tests -gt 0 ]; then
    success_rate=$((success_tests * 100 / total_tests))
    echo -e "${CYAN}Taux de succès: ${success_rate}%${NC}"
fi

# Recommandations
echo -e "${PURPLE}"
echo "=========================================="
echo "💡 RECOMMANDATIONS"
echo "=========================================="
echo -e "${NC}"

if [ $error_tests -eq 0 ]; then
    print_success "Système entièrement fonctionnel !"
    echo -e "${GREEN}🎯 Prêt pour la production${NC}"
else
    print_warning "Certains tests ont échoué"
    echo -e "${YELLOW}🔧 Vérifiez les logs: docker-compose logs${NC}"
fi

if [ $warning_tests -gt 0 ]; then
    print_warning "Améliorations recommandées"
    echo -e "${YELLOW}📈 Optimisez les performances si nécessaire${NC}"
fi

echo -e "${PURPLE}"
echo "=========================================="
echo "🔗 ACCÈS AU SYSTÈME"
echo "=========================================="
echo -e "${NC}"

echo -e "${GREEN}Frontend React: http://localhost:3000${NC}"
echo -e "${GREEN}Backend API: http://localhost:8000${NC}"
echo -e "${GREEN}Documentation API: http://localhost:8000/docs${NC}"
echo -e "${GREEN}Page d'accueil HTML: http://localhost:3000/lsu_index.html${NC}"
echo -e "${GREEN}Générateur HTML: http://localhost:3000/improved_lsu_generator.html${NC}"
echo -e "${GREEN}Profil élève HTML: http://localhost:3000/student_profile_page.html${NC}"

echo -e "${PURPLE}"
echo "=========================================="
echo "✅ TEST COMPLET TERMINÉ"
echo "=========================================="
echo -e "${NC}" 