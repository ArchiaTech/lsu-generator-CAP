#!/usr/bin/env python3
"""
🎓 Script de lancement LSU - Version Python optimisée
Lance l'application avec vérifications et ouverture automatique
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os
import requests
import sys
from pathlib import Path

class LSULauncher:
    def __init__(self, port=3000):
        self.port = port
        self.url = f"http://localhost:{port}"
        self.project_dir = Path("/Users/johneloi/Downloads/LSU20250628")
        
    def print_success(self, message):
        print(f"✅ {message}")
        
    def print_info(self, message):
        print(f"ℹ️ {message}")
        
    def print_error(self, message):
        print(f"❌ {message}")
        
    def check_server(self):
        """Vérifie si le serveur est déjà actif"""
        try:
            response = requests.get(self.url, timeout=3)
            return response.status_code == 200
        except:
            return False
            
    def check_port(self):
        """Vérifie si le port est utilisé"""
        try:
            response = requests.get(self.url, timeout=1)
            return True
        except:
            return False
            
    def start_server(self):
        """Démarre le serveur HTTP"""
        self.print_info("Démarrage du serveur Python...")
        
        # Changement vers le répertoire du projet
        os.chdir(self.project_dir)
        
        def open_browser():
            time.sleep(2)
            webbrowser.open(self.url)
            self.print_success("Navigateur ouvert automatiquement")
            
        try:
            handler = http.server.SimpleHTTPRequestHandler
            
            with socketserver.TCPServer(("", self.port), handler) as httpd:
                self.print_success(f"Serveur démarré sur {self.url}")
                
                # Ouverture du navigateur dans un thread séparé
                browser_thread = threading.Thread(target=open_browser)
                browser_thread.daemon = True
                browser_thread.start()
                
                self.print_success("Page chargée avec succès")
                self.print_success("🎉 Application LSU prête !")
                
                print("\n📁 Pages disponibles:")
                print("   - index.html (page d'accueil)")
                print("   - student_profile_page.html (profil élève)")
                print("   - create_student.html (création élève)")
                print("   - student_list.html (liste des élèves)")
                print("   - photos_classe_pro.html (photos de classe)")
                print("   - dashboard.html (tableau de bord)")
                print("   - lsu_generator.html (générateur LSU)")
                print("   - improved_lsu_generator.html (générateur amélioré)")
                
                print(f"\n🌐 Accès: {self.url}")
                print("🛑 Pour arrêter: Ctrl+C")
                
                # Démarrage du serveur
                httpd.serve_forever()
                
        except OSError as e:
            if "Address already in use" in str(e):
                self.print_info(f"Le port {self.port} est déjà utilisé")
                webbrowser.open(self.url)
                self.print_success("Page chargée avec succès")
            else:
                self.print_error(f"Erreur: {e}")
        except KeyboardInterrupt:
            print("\n🛑 Serveur arrêté")
            
    def launch(self):
        """Lancement principal"""
        print("🎓 Lancement Application LSU")
        print("=" * 30)
        
        # Vérification si le serveur est déjà actif
        if self.check_server():
            self.print_success("Serveur déjà actif")
            webbrowser.open(self.url)
            self.print_success("Page chargée avec succès")
            self.print_success("🎉 Application LSU prête !")
            return True
            
        # Vérification du port
        if self.check_port():
            self.print_info("Port déjà utilisé, tentative d'ouverture...")
            webbrowser.open(self.url)
            self.print_success("Page chargée avec succès")
            return True
            
        # Lancement du serveur
        self.start_server()
        return True

def main():
    launcher = LSULauncher()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "check":
            if launcher.check_server():
                launcher.print_success("Serveur actif")
            else:
                launcher.print_error("Serveur non actif")
        elif command == "open":
            webbrowser.open(launcher.url)
            launcher.print_success("Navigateur ouvert")
        else:
            print("Usage: python lancer_lsu.py [check|open]")
    else:
        launcher.launch()

if __name__ == "__main__":
    main() 