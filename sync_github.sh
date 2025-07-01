#!/bin/bash

# 🚀 Script de synchronisation GitHub - Projet LSU
set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Variables
REPO_NAME="gestion-lsu"
MAIN_BRANCH="main"

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️ $1${NC}"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}🚀 Synchronisation GitHub LSU${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Vérifications
check_git() {
    if ! command -v git &> /dev/null; then
        print_error "Git non installé"
        exit 1
    fi
    
    if [ ! -d ".git" ]; then
        print_error "Pas un dépôt Git"
        exit 1
    fi
    
    print_success "Git OK"
}

check_branch() {
    current_branch=$(git branch --show-current)
    
    if [ "$current_branch" != "$MAIN_BRANCH" ]; then
        print_warning "Branche actuelle: $current_branch (attendu: $MAIN_BRANCH)"
        read -p "Continuer ? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 0
        fi
    else
        print_success "Branche: $MAIN_BRANCH"
    fi
}

check_changes() {
    if git diff-index --quiet HEAD --; then
        print_warning "Aucun changement"
        read -p "Pousser quand même ? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 0
        fi
    else
        print_success "Changements détectés"
    fi
}

# Synchronisation
main() {
    print_header
    
    check_git
    check_branch
    check_changes
    
    # Ajout des fichiers
    print_info "Ajout des fichiers..."
    git add .
    git status --short
    
    # Commit
    commit_message="${1:-🚀 Mise à jour du générateur LSU}"
    print_info "Commit: $commit_message"
    git commit -m "$commit_message"
    
    # Push
    print_info "Poussée vers GitHub..."
    git pull origin "$MAIN_BRANCH" --rebase
    git push origin "$MAIN_BRANCH"
    
    print_success "Synchronisation terminée"
    echo -e "${GREEN}URL:${NC} https://github.com/ELOIJOHN/$REPO_NAME"
}

main "$1"
