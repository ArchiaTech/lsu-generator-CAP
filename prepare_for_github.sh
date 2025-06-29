#!/bin/bash

# Couleurs pour l'affichage
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

echo -e "${PURPLE}"
echo "=========================================="
echo "🚀 PRÉPARATION POUR GITHUB"
echo "=========================================="
echo -e "${NC}"

# Fonction pour afficher les étapes
print_step() {
    echo -e "${BLUE}📋 $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

# 1. Vérification de Git
print_step "1. Vérification de Git..."

if ! command -v git &> /dev/null; then
    echo "❌ Git n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

print_success "Git est installé"

# 2. Initialisation du repository Git
print_step "2. Initialisation du repository Git..."

if [ ! -d ".git" ]; then
    git init
    print_success "Repository Git initialisé"
else
    print_success "Repository Git déjà initialisé"
fi

# 3. Vérification des fichiers sensibles
print_step "3. Vérification des fichiers sensibles..."

# Vérifier si .env existe et contient des données sensibles
if [ -f ".env" ]; then
    if grep -q "password\|secret\|key" .env; then
        print_warning "Le fichier .env contient des données sensibles"
        echo "Assurez-vous que .env est dans .gitignore"
    fi
else
    print_warning "Fichier .env manquant"
    echo "Créez-le à partir de env.example"
fi

# 4. Nettoyage des fichiers temporaires
print_step "4. Nettoyage des fichiers temporaires..."

# Supprimer les fichiers de build
rm -rf frontend/build
rm -rf frontend/dist
rm -rf backend/__pycache__
rm -rf backend/app/__pycache__
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null

print_success "Fichiers temporaires nettoyés"

# 5. Vérification de la structure
print_step "5. Vérification de la structure du projet..."

required_files=(
    "README.md"
    "LICENSE"
    "CONTRIBUTING.md"
    ".gitignore"
    "docker-compose.yml"
    "start.sh"
    "test_complet.sh"
    "env.example"
    "backend/requirements.txt"
    "frontend/package.json"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
    fi
done

if [ ${#missing_files[@]} -eq 0 ]; then
    print_success "Tous les fichiers requis sont présents"
else
    print_warning "Fichiers manquants :"
    for file in "${missing_files[@]}"; do
        echo "  - $file"
    done
fi

# 6. Test du système
print_step "6. Test du système..."

if [ -f "test_complet.sh" ]; then
    echo "Exécution des tests..."
    ./test_complet.sh > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        print_success "Tests passés"
    else
        print_warning "Certains tests ont échoué"
    fi
else
    print_warning "Script de test non trouvé"
fi

# 7. Préparation du premier commit
print_step "7. Préparation du premier commit..."

# Ajouter tous les fichiers
git add .

# Vérifier le statut
echo "Fichiers à commiter :"
git status --porcelain

# 8. Instructions pour GitHub
echo -e "${PURPLE}"
echo "=========================================="
echo "📋 INSTRUCTIONS POUR GITHUB"
echo "=========================================="
echo -e "${NC}"

echo -e "${GREEN}1. Créez un nouveau repository sur GitHub :${NC}"
echo "   - Allez sur https://github.com/new"
echo "   - Nom : lsu-system"
echo "   - Description : Système de Gestion LSU - Livret Scolaire Unique"
echo "   - Public ou Private selon votre choix"
echo "   - Ne pas initialiser avec README (déjà présent)"

echo -e "${GREEN}2. Connectez votre repository local :${NC}"
echo "   git remote add origin https://github.com/VOTRE_USERNAME/lsu-system.git"

echo -e "${GREEN}3. Faites votre premier commit :${NC}"
echo "   git commit -m \"feat: initial commit - système LSU complet\""

echo -e "${GREEN}4. Poussez vers GitHub :${NC}"
echo "   git push -u origin main"

echo -e "${GREEN}5. Configurez les secrets GitHub (optionnel) :${NC}"
echo "   - Allez dans Settings > Secrets and variables > Actions"
echo "   - Ajoutez DOCKER_USERNAME et DOCKER_PASSWORD pour CI/CD"

echo -e "${GREEN}6. Activez GitHub Pages (optionnel) :${NC}"
echo "   - Settings > Pages"
echo "   - Source : Deploy from a branch"
echo "   - Branch : main, folder : /docs"

# 9. Checklist finale
echo -e "${PURPLE}"
echo "=========================================="
echo "✅ CHECKLIST FINALE"
echo "=========================================="
echo -e "${NC}"

echo -e "${YELLOW}Avant de publier, vérifiez :${NC}"
echo "□ README.md est à jour et complet"
echo "□ .gitignore exclut les fichiers sensibles"
echo "□ env.example contient toutes les variables nécessaires"
echo "□ Les tests passent localement"
echo "□ La documentation est claire"
echo "□ Les licences sont correctes"
echo "□ Les crédits sont mentionnés"

echo -e "${PURPLE}"
echo "=========================================="
echo "🎉 PRÉPARATION TERMINÉE !"
echo "=========================================="
echo -e "${NC}"

echo -e "${GREEN}Votre projet est prêt pour GitHub !${NC}"
echo -e "${BLUE}Suivez les instructions ci-dessus pour le publier.${NC}" 