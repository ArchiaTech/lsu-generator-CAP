#!/bin/bash

# 🎓 Script de lancement LSU
echo "🎓 Lancement Application LSU..."

# Vérification Docker
if ! docker info &> /dev/null; then
    echo "❌ Docker non démarré"
    exit 1
fi

# Démarrage des services
echo "🚀 Démarrage des services..."
./start.sh

# Attente et vérification
echo "⏳ Vérification des ports..."
sleep 10

# Vérification port 3000
for i in {1..15}; do
    if curl -s -f http://localhost:3000 >/dev/null 2>&1; then
        echo "✅ Frontend accessible"
        break
    fi
    echo "⏳ Tentative $i/15..."
    sleep 2
    if [ $i -eq 15 ]; then
        echo "❌ Frontend non accessible"
        exit 1
    fi
done

# Ouverture navigateur
echo "🌐 Ouverture du navigateur..."
open http://localhost:3000

echo "✅ Page chargée avec succès"
echo "🎉 Application LSU prête !"
