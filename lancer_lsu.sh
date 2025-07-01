#!/bin/bash

# 🎓 Script de lancement LSU - Version simple et rapide
# Auteur: Assistant IA
# Usage: ./lancer_lsu.sh

echo "🎓 Lancement Application LSU"
echo "============================"

# Vérification si le port 3000 est déjà utilisé
if curl -s -f http://localhost:3000 >/dev/null 2>&1; then
    echo "✅ Application déjà en cours"
    open http://localhost:3000
    echo "✅ Page chargée avec succès"
    echo "🎉 Application LSU prête !"
    exit 0
fi

# Vérification de Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 non installé"
    exit 1
fi

echo "🚀 Démarrage du serveur local..."

# Lancement du serveur Python en arrière-plan
python3 -c "
import http.server
import socketserver
import webbrowser
import threading
import time
import os

port = 3000
url = f'http://localhost:{port}'

def open_browser():
    time.sleep(2)
    webbrowser.open(url)
    print('✅ Navigateur ouvert automatiquement')

try:
    os.chdir('/Users/johneloi/Downloads/LSU20250628')
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(('', port), handler) as httpd:
        print('✅ Serveur démarré sur http://localhost:3000')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        print('✅ Page chargée avec succès')
        print('🎉 Application LSU prête !')
        print('📁 Fichiers disponibles:')
        print('   - index.html (page d\'accueil)')
        print('   - student_profile_page.html (profil élève)')
        print('   - create_student.html (création élève)')
        print('   - student_list.html (liste des élèves)')
        print('   - photos_classe_pro.html (photos de classe)')
        print('   - dashboard.html (tableau de bord)')
        print('🛑 Pour arrêter: Ctrl+C')
        
        httpd.serve_forever()
        
except OSError as e:
    if 'Address already in use' in str(e):
        print('ℹ️ Port 3000 déjà utilisé')
        webbrowser.open(url)
        print('✅ Page chargée avec succès')
    else:
        print(f'❌ Erreur: {e}')
except KeyboardInterrupt:
    print('\\n🛑 Serveur arrêté')
" &

# Attendre un peu pour que le serveur démarre
sleep 3

# Vérification finale
if curl -s -f http://localhost:3000 >/dev/null 2>&1; then
    echo "✅ Application lancée avec succès"
    echo "🌐 Accès: http://localhost:3000"
else
    echo "❌ Erreur lors du lancement"
    exit 1
fi 