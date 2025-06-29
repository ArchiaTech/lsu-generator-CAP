#!/bin/bash

# Variables
DATE=$(date +"%Y%m%d-%H%M")
BACKUP_DIR="backup/$DATE"
DEV_DIR="dev"
MAIN_DIR="main"

# Créer le dossier de sauvegarde
mkdir -p "$BACKUP_DIR"

# Sauvegarder l'état actuel de main/
cp -r $MAIN_DIR/* "$BACKUP_DIR/"

# Copier les fichiers de dev/ vers main/
rm -rf $MAIN_DIR/*
cp -r $DEV_DIR/* $MAIN_DIR/

# Git commit et push
cd $MAIN_DIR
git add .
git commit -m "🔄 Déploiement depuis dev le $DATE"
git push origin main
