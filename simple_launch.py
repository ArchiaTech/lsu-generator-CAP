#!/usr/bin/env python3
"""
🎓 Lancement simple LSU - Serveur HTTP local
Lance un serveur Python pour les fichiers HTML statiques
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os
from pathlib import Path

class LSULauncher:
    def __init__(self, port=3000):
        self.port = port
        self.url = f"http://localhost:{port}"
        
    def print_success(self, message):
        print(f"✅ {message}")
        
    def print_info(self, message):
        print(f"ℹ️ {message}")
        
    def start_server(self):
        """Démarre le serveur HTTP"""
        self.print_info(f"Démarrage du serveur sur le port {self.port}...")
        
        # Changement vers le répertoire du projet
        os.chdir(Path(__file__).parent)
        
        # Configuration du serveur
        handler = http.server.SimpleHTTPRequestHandler
        
        try:
            with socketserver.TCPServer(("", self.port), handler) as httpd:
                self.print_success(f"Serveur démarré sur {self.url}")
                
                # Ouverture du navigateur dans un thread séparé
                def open_browser():
                    time.sleep(1)  # Attendre que le serveur soit prêt
                    webbrowser.open(self.url)
                    self.print_success("Navigateur ouvert")
                    self.print_success("Page chargée avec succès")
                    print("🎉 Application LSU prête !")
                    print(f"📁 Fichiers disponibles:")
                    print(f"   - index.html (page d'accueil)")
                    print(f"   - student_profile_page.html (profil élève)")
                    print(f"   - create_student.html (création élève)")
                    print(f"   - student_list.html (liste des élèves)")
                    print(f"   - photos_classe_pro.html (photos de classe)")
                    print(f"   - dashboard.html (tableau de bord)")
                    print(f"\n🌐 Accès: {self.url}")
                    print("🛑 Pour arrêter: Ctrl+C")
                
                browser_thread = threading.Thread(target=open_browser)
                browser_thread.daemon = True
                browser_thread.start()
                
                # Démarrage du serveur
                httpd.serve_forever()
                
        except OSError as e:
            if "Address already in use" in str(e):
                self.print_info(f"Le port {self.port} est déjà utilisé")
                webbrowser.open(self.url)
                self.print_success("Page chargée avec succès")
            else:
                print(f"❌ Erreur: {e}")
        except KeyboardInterrupt:
            print("\n🛑 Serveur arrêté")

if __name__ == "__main__":
    print("🎓 Lancement simple LSU")
    print("=" * 30)
    
    launcher = LSULauncher()
    launcher.start_server() 