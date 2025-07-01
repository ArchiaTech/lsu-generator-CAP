#!/bin/bash

# 🚀 Script de déploiement GitHub Pages - LSU Generator CAP
set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

# Configuration
REPO_NAME="lsu-generator-CAP"
REPO_URL="https://github.com/ArchiaTech/lsu-generator-CAP.git"
GITHUB_PAGES_URL="https://archiatech.github.io/lsu-generator-CAP/"
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
    echo -e "${PURPLE}================================${NC}"
    echo -e "${PURPLE}🚀 Déploiement GitHub Pages${NC}"
    echo -e "${PURPLE}================================${NC}"
    echo -e "${BLUE}Projet:${NC} $REPO_NAME"
    echo -e "${BLUE}URL:${NC} $GITHUB_PAGES_URL"
    echo ""
}

# Vérifications
check_git() {
    if ! command -v git &> /dev/null; then
        print_error "Git non installé"
        exit 1
    fi
    print_success "Git OK"
}

init_git() {
    if [ ! -d ".git" ]; then
        print_info "Initialisation Git..."
        git init
        git remote add origin "$REPO_URL"
        print_success "Git initialisé"
    else
        print_success "Git déjà initialisé"
    fi
}

check_branch() {
    current_branch=$(git branch --show-current 2>/dev/null || echo "none")
    
    if [ "$current_branch" = "none" ]; then
        git checkout -b "$MAIN_BRANCH"
    elif [ "$current_branch" != "$MAIN_BRANCH" ]; then
        print_warning "Branche: $current_branch"
        read -p "Basculer vers $MAIN_BRANCH ? (Y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            git checkout "$MAIN_BRANCH" 2>/dev/null || git checkout -b "$MAIN_BRANCH"
        fi
    else
        print_success "Branche: $MAIN_BRANCH"
    fi
}

check_remote() {
    if ! git remote get-url origin &> /dev/null; then
        git remote add origin "$REPO_URL"
    fi
    
    remote_url=$(git remote get-url origin)
    if [[ "$remote_url" != *"$REPO_NAME"* ]]; then
        print_warning "Remote: $remote_url"
        read -p "Mettre à jour ? (Y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            git remote set-url origin "$REPO_URL"
        fi
    fi
    print_success "Remote configuré"
}

create_cname() {
    if [ ! -f "CNAME" ]; then
        echo "archiatech.github.io" > CNAME
        print_success "CNAME créé"
    fi
}

create_nojekyll() {
    if [ ! -f ".nojekyll" ]; then
        touch .nojekyll
        print_success ".nojekyll créé"
    fi
}

# Déploiement
main() {
    print_header
    
    check_git
    init_git
    check_branch
    check_remote
    
    create_cname
    create_nojekyll
    
    if git diff-index --quiet HEAD -- 2>/dev/null; then
        print_warning "Aucun changement"
        read -p "Continuer ? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 0
        fi
    fi
    
    print_info "Ajout des fichiers..."
    git add .
    git status --short
    
    commit_message="${1:-✨ Publication LSU Generator CAP}"
    print_info "Commit: $commit_message"
    git commit -m "$commit_message"
    
    print_info "Push vers GitHub..."
    git push origin "$MAIN_BRANCH"
    
    print_success "Déploiement terminé"
    print_info "URL: $GITHUB_PAGES_URL"
    print_warning "Attendez quelques minutes pour que le site soit en ligne"
}

main "$1"
