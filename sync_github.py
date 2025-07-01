#!/usr/bin/env python3
"""
🚀 Script de synchronisation GitHub - Projet LSU
Synchronise automatiquement le projet avec GitHub
"""

import subprocess
import sys
import os
from pathlib import Path

class GitHubSync:
    def __init__(self):
        self.repo_name = "gestion-lsu"
        self.main_branch = "main"
        self.remote_url = "git@github.com:ELOIJOHN/gestion-lsu.git"
        
    def print_success(self, message):
        print(f"✅ {message}")
        
    def print_warning(self, message):
        print(f"⚠️ {message}")
        
    def print_error(self, message):
        print(f"❌ {message}")
        
    def print_info(self, message):
        print(f"ℹ️ {message}")
        
    def run_command(self, command, check=True):
        """Exécute une commande Git"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=check)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            if check:
                self.print_error(f"Erreur: {e.stderr}")
                return None
            return e.stdout.strip()
            
    def check_git(self):
        """Vérifie que Git est disponible"""
        if not self.run_command("git --version", check=False):
            self.print_error("Git non installé")
            return False
            
        if not Path(".git").exists():
            self.print_error("Pas un dépôt Git")
            return False
            
        self.print_success("Git OK")
        return True
        
    def check_branch(self):
        """Vérifie la branche actuelle"""
        current_branch = self.run_command("git branch --show-current")
        
        if current_branch != self.main_branch:
            self.print_warning(f"Branche actuelle: {current_branch} (attendu: {self.main_branch})")
            response = input("Continuer ? (y/N): ").lower()
            if response != 'y':
                return False
        else:
            self.print_success(f"Branche: {self.main_branch}")
            
        return True
        
    def check_remote(self):
        """Vérifie la configuration du remote"""
        remote_url = self.run_command("git remote get-url origin", check=False)
        
        if not remote_url:
            self.print_info("Configuration du remote...")
            self.run_command(f"git remote add origin {self.remote_url}")
            self.print_success("Remote configuré")
        elif self.repo_name not in remote_url:
            self.print_warning(f"Remote URL: {remote_url}")
            response = input("Continuer ? (y/N): ").lower()
            if response != 'y':
                return False
                
        return True
        
    def check_changes(self):
        """Vérifie s'il y a des changements"""
        if self.run_command("git diff-index --quiet HEAD --", check=False) == "":
            self.print_warning("Aucun changement détecté")
            response = input("Pousser quand même ? (y/N): ").lower()
            if response != 'y':
                return False
        else:
            self.print_success("Changements détectés")
            
        return True
        
    def add_files(self):
        """Ajoute tous les fichiers"""
        self.print_info("Ajout des fichiers...")
        self.run_command("git add .")
        
        # Affichage du statut
        status = self.run_command("git status --short")
        if status:
            self.print_info("Fichiers modifiés:")
            print(status)
            
        self.print_success("Fichiers ajoutés")
        
    def make_commit(self, message=None):
        """Crée un commit"""
        if not message:
            message = "🚀 Mise à jour du générateur LSU"
            
        self.print_info(f"Commit: {message}")
        self.run_command(f'git commit -m "{message}"')
        self.print_success("Commit créé")
        
    def push_changes(self):
        """Pousse les changements"""
        self.print_info("Récupération des dernières modifications...")
        self.run_command(f"git pull origin {self.main_branch} --rebase")
        
        self.print_info("Poussée vers GitHub...")
        self.run_command(f"git push origin {self.main_branch}")
        
        self.print_success("Changements poussés")
        
    def sync(self, commit_message=None):
        """Synchronisation principale"""
        print("🚀 Synchronisation GitHub LSU")
        print("=" * 30)
        
        # Vérifications
        if not self.check_git():
            return False
            
        if not self.check_branch():
            return False
            
        if not self.check_remote():
            return False
            
        if not self.check_changes():
            return False
            
        # Synchronisation
        self.add_files()
        self.make_commit(commit_message)
        self.push_changes()
        
        # Informations finales
        print("\n🎉 Synchronisation terminée")
        print(f"URL: https://github.com/ELOIJOHN/{self.repo_name}")
        
        return True

def main():
    syncer = GitHubSync()
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ["help", "-h", "--help"]:
            print("Usage: python sync_github.py [message_commit]")
            print("Exemples:")
            print("  python sync_github.py")
            print('  python sync_github.py "🚀 Mise à jour du générateur LSU"')
            return
            
        commit_message = sys.argv[1]
    else:
        commit_message = None
        
    success = syncer.sync(commit_message)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 