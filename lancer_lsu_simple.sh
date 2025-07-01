#!/bin/bash

# 🎓 Script de lancement LSU - Version simple et efficace
echo "🎓 Lancement Application LSU"
echo "============================"

PORT=3000
URL="http://localhost:$PORT"

print_success() {
    echo "✅ $1"
}

print_info() {
    echo "ℹ️ $1"
}

# Vérification si le serveur est déjà actif
if curl -s -f "$URL" >/dev/null 2>&1; then
    print_success "Serveur déjà actif sur $URL"
    open "$URL"
    print_success "Page chargée avec succès"
    print_success "🎉 Application LSU prête !"
    exit 0
fi

# Lancement du serveur Python
print_info "Démarrage du serveur Python..."

python3 -c "
import http.server
import socketserver
import webbrowser
import threading
import time
import os

port = $PORT
url = f'http://localhost:{port}'

def open_browser():
    time.sleep(2)
    webbrowser.open(url)
    print('✅ Navigateur ouvert automatiquement')

try:
    os.chdir('/Users/johneloi/Downloads/LSU20250628')
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(('', port), handler) as httpd:
        print(f'✅ Serveur démarré sur {url}')
        
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        print('✅ Page chargée avec succès')
        print('🎉 Application LSU prête !')
        print('📁 Pages disponibles:')
        print('   - index.html (accueil)')
        print('   - student_profile_page.html (profil élève)')
        print('   - create_student.html (création élève)')
        print('   - student_list.html (liste élèves)')
        print('   - photos_classe_pro.html (photos classe)')
        print('   - dashboard.html (tableau de bord)')
        print('🛑 Pour arrêter: Ctrl+C')
        
        httpd.serve_forever()
        
except OSError as e:
    if 'Address already in use' in str(e):
        print(f'ℹ️ Port {port} déjà utilisé')
        webbrowser.open(url)
        print('✅ Page chargée avec succès')
    else:
        print(f'❌ Erreur: {e}')
except KeyboardInterrupt:
    print('\\n🛑 Serveur arrêté')
" &

sleep 3
print_success "Application lancée avec succès"
print_info "🌐 Accès: $URL"
