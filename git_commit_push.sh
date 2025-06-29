#!/bin/bash

# Script de commit et push automatique pour le projet LSU
# Auteur: Assistant IA
# Date: 2025-01-29

echo "🎓 Script de Commit et Push - Projet LSU"
echo "========================================"

# Vérifie que tu es bien dans un dépôt git
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo "⛔️ Ce dossier n'est pas un dépôt Git."
  echo "💡 Pour initialiser un dépôt Git : git init"
  exit 1
fi

# Vérifie la branche active
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [[ "$current_branch" != "main" ]]; then
  echo "⚠️ Tu n'es pas sur la branche 'main' (actuellement : $current_branch)"
  echo "💡 Pour changer de branche : git checkout main"
  exit 1
fi

echo "✅ Branche active : $current_branch"

# Vérifie s'il y a des modifications
if git diff-index --quiet HEAD --; then
  echo "ℹ️ Aucune modification détectée."
  echo "💡 Aucun commit nécessaire."
  exit 0
fi

echo "📋 Modifications détectées :"
git status --short

# Demande un message de commit
echo ""
read -p "📝 Entrez un message de commit : " commit_msg

# Vérifie que le message n'est pas vide
if [[ -z "$commit_msg" ]]; then
  echo "❌ Le message de commit ne peut pas être vide."
  exit 1
fi

# Ajoute tous les fichiers
echo "📁 Ajout des fichiers..."
git add .
echo "✅ Fichiers ajoutés."

# Crée le commit
echo "💾 Création du commit..."
if git commit -m "$commit_msg"; then
  echo "✅ Commit effectué avec le message : $commit_msg"
else
  echo "❌ Échec du commit."
  exit 1
fi

# Vérifie s'il y a un remote configuré
if ! git remote get-url origin > /dev/null 2>&1; then
  echo "⚠️ Aucun remote 'origin' configuré."
  echo "💡 Pour configurer un remote : git remote add origin <URL>"
  exit 1
fi

# Affiche l'URL du remote
remote_url=$(git remote get-url origin)
echo "🌐 Remote configuré : $remote_url"

# Pousse vers GitHub
echo "🚀 Push vers GitHub..."
if git push origin main; then
  echo "✅ Modifications poussées avec succès vers GitHub."
  echo ""
  echo "🎉 Opération terminée avec succès !"
  echo "📊 Résumé :"
  echo "   - Branche : $current_branch"
  echo "   - Commit : $commit_msg"
  echo "   - Remote : $remote_url"
else
  echo "❌ Échec du push."
  echo "💡 Vérifie :"
  echo "   - Tes identifiants GitHub"
  echo "   - Les conflits potentiels"
  echo "   - La connexion internet"
  echo "   - Les permissions sur le repository"
  exit 1
fi 