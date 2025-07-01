#!/usr/bin/env python3
"""
🎓 Script de lancement LSU - Version Python
"""

import subprocess
import time
import requests
import webbrowser
import sys

class LSULauncher:
    def __init__(self):
        self.frontend_url = "http://localhost:3000"
        self.backend_url = "http://localhost:8000"
        
    def print_success(self, message):
        print(f"✅ {message}")
        
    def print_error(self, message):
        print(f"❌ {message}")
        
    def print_info(self, message):
        print(f"ℹ️ {message}")
        
    def check_docker(self):
        try:
            result = subprocess.run(['docker', 'info'], 
                                  capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except:
            return False
            
    def start_services(self):
        self.print_info("Démarrage des services...")
        try:
            subprocess.run(['./start.sh'], check=True, timeout=300)
            self.print_success("Services démarrés")
            return True
        except:
            self.print_error("Erreur lors du démarrage")
            return False
            
    def check_port(self, port, service_name):
        self.print_info(f"Vérification du port {port} ({service_name})...")
        
        for i in range(15):
            try:
                response = requests.get(f"http://localhost:{port}", timeout=5)
                if response.status_code == 200:
                    self.print_success(f"{service_name} accessible")
                    return True
            except:
                pass
                
            if i < 14:
                self.print_info(f"Tentative {i+1}/15...")
                time.sleep(2)
                
        self.print_error(f"{service_name} non accessible")
        return False
        
    def open_browser(self):
        self.print_info("Ouverture du navigateur...")
        try:
            webbrowser.open(self.frontend_url)
            self.print_success("Navigateur ouvert")
            return True
        except:
            self.print_info(f"Ouvrez manuellement: {self.frontend_url}")
            return False
            
    def launch(self):
        print("🎓 Lancement Application LSU")
        print("=" * 30)
        
        if not self.check_docker():
            self.print_error("Docker non disponible")
            return False
            
        if not self.start_services():
            return False
            
        time.sleep(10)
        
        if not self.check_port(8000, "Backend"):
            return False
            
        if not self.check_port(3000, "Frontend"):
            return False
            
        self.open_browser()
        
        self.print_success("Page chargée avec succès")
        print("🎉 Application LSU prête !")
        return True

if __name__ == "__main__":
    launcher = LSULauncher()
    success = launcher.launch()
    sys.exit(0 if success else 1)
