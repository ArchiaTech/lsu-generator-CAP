#!/bin/bash

echo "🎓 Lancement rapide LSU..."

# Vérification si les services sont déjà actifs
if curl -s -f http://localhost:3000 >/dev/null 2>&1; then
    echo "✅ Services déjà actifs"
    open http://localhost:3000
    echo "✅ Page chargée avec succès"
    exit 0
fi

# Vérification Docker
if ! docker info &> /dev/null; then
    echo "❌ Docker non démarré"
    exit 1
fi

# Vérification des conteneurs existants
if docker-compose ps | grep -q "Up"; then
    echo "🚀 Redémarrage des services..."
    docker-compose restart
else
    echo "🚀 Démarrage des services..."
    ./start.sh
fi

# Attente et vérification
echo "⏳ Vérification..."
sleep 15

# Vérification finale
if curl -s -f http://localhost:3000 >/dev/null 2>&1; then
    echo "✅ Frontend accessible"
    open http://localhost:3000
    echo "✅ Page chargée avec succès"
    echo "🎉 Application LSU prête !"
else
    echo "❌ Frontend non accessible"
    exit 1
fi
