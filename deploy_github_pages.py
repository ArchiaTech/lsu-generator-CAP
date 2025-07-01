#!/usr/bin/env python3
"""
🚀 Script de déploiement GitHub Pages - LSU Generator CAP
Déploie automatiquement le projet sur GitHub Pages
"""

import subprocess
import sys
import os
import time
import requests
from pathlib import Path

class GitHubPagesDeployer:
    def __init__(self):
        self.repo_name = "lsu-generator-CAP"
        self.repo_url = "https://github.com/ArchiaTech/lsu-generator-CAP.git"
        self.github_pages_url = "https://archiatech.github.io/lsu-generator-CAP/"
        self.main_branch = "main"
        
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
        self.print_success("Git OK")
        return True
        
    def init_git(self):
        """Initialise Git si nécessaire"""
        if not Path(".git").exists():
            self.print_info("Initialisation Git...")
            self.run_command("git init")
            self.run_command(f"git remote add origin {self.repo_url}")
            self.print_success("Git initialisé")
        else:
            self.print_success("Git déjà initialisé")
            
    def check_branch(self):
        """Vérifie et configure la branche"""
        current_branch = self.run_command("git branch --show-current", check=False)
        
        if not current_branch:
            self.run_command(f"git checkout -b {self.main_branch}")
            self.print_success(f"Branche créée: {self.main_branch}")
        elif current_branch != self.main_branch:
            self.print_warning(f"Branche actuelle: {current_branch}")
            response = input(f"Basculer vers {self.main_branch} ? (Y/n): ").lower()
            if response != 'n':
                self.run_command(f"git checkout {self.main_branch}")
        else:
            self.print_success(f"Branche: {self.main_branch}")
            
    def check_remote(self):
        """Vérifie la configuration du remote"""
        remote_url = self.run_command("git remote get-url origin", check=False)
        
        if not remote_url:
            self.run_command(f"git remote add origin {self.repo_url}")
        elif self.repo_name not in remote_url:
            self.print_warning(f"Remote: {remote_url}")
            response = input("Mettre à jour ? (Y/n): ").lower()
            if response != 'n':
                self.run_command(f"git remote set-url origin {self.repo_url}")
                
        self.print_success("Remote configuré")
        
    def create_cname(self):
        """Crée le fichier CNAME"""
        if not Path("CNAME").exists():
            with open("CNAME", "w") as f:
                f.write("archiatech.github.io")
            self.print_success("CNAME créé")
            
    def create_nojekyll(self):
        """Crée le fichier .nojekyll"""
        if not Path(".nojekyll").exists():
            Path(".nojekyll").touch()
            self.print_success(".nojekyll créé")
            
    def add_files(self):
        """Ajoute tous les fichiers"""
        self.print_info("Ajout des fichiers...")
        self.run_command("git add .")
        
        status = self.run_command("git status --short")
        if status:
            self.print_info("Fichiers modifiés:")
            print(status)
            
    def make_commit(self, message=None):
        """Crée un commit"""
        if not message:
            message = "✨ Publication LSU Generator CAP"
            
        self.print_info(f"Commit: {message}")
        self.run_command(f'git commit -m "{message}"')
        self.print_success("Commit créé")
        
    def push_changes(self):
        """Pousse les changements"""
        self.print_info("Push vers GitHub...")
        self.run_command(f"git push origin {self.main_branch}")
        self.print_success("Push terminé")
        
    def check_site_online(self):
        """Vérifie si le site est en ligne"""
        self.print_info("Vérification du site...")
        
        for attempt in range(1, 11):
            try:
                response = requests.get(self.github_pages_url, timeout=10)
                if response.status_code == 200:
                    self.print_success("Site en ligne !")
                    return True
            except:
                pass
                
            self.print_warning(f"Tentative {attempt}/10")
            time.sleep(30)
            
        self.print_warning("Site pas encore en ligne")
        return False
        
    def deploy(self, commit_message=None):
        """Déploiement principal"""
        print("🚀 Déploiement GitHub Pages")
        print("=" * 30)
        print(f"Projet: {self.repo_name}")
        print(f"URL: {self.github_pages_url}")
        print()
        
        # Vérifications et configuration
        if not self.check_git():
            return False
            
        self.init_git()
        self.check_branch()
        self.check_remote()
        
        # Préparation
        self.create_cname()
        self.create_nojekyll()
        
        # Vérification des changements
        if self.run_command("git diff-index --quiet HEAD --", check=False) == "":
            self.print_warning("Aucun changement")
            response = input("Continuer ? (y/N): ").lower()
            if response != 'y':
                return False
                
        # Déploiement
        self.add_files()
        self.make_commit(commit_message)
        self.push_changes()
        
        # Vérification
        self.check_site_online()
        
        # Informations finales
        print("\n🎉 Déploiement terminé")
        print(f"URL: {self.github_pages_url}")
        print("Attendez quelques minutes pour que le site soit en ligne")
        
        return True

def main():
    deployer = GitHubPagesDeployer()
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ["help", "-h", "--help"]:
            print("Usage: python deploy_github_pages.py [message_commit]")
            print("Exemples:")
            print("  python deploy_github_pages.py")
            print('  python deploy_github_pages.py "✨ Publication LSU Generator CAP"')
            return
            
        commit_message = sys.argv[1]
    else:
        commit_message = None
        
    success = deployer.deploy(commit_message)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 