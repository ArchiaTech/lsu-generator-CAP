# 🔗 Guide des Connexions - Système LSU

## Vue d'ensemble des connexions

Le système LSU utilise une architecture microservices avec les connexions suivantes :

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Base de       │
│   React         │◄──►│   FastAPI       │◄──►│   données       │
│   :3000         │    │   :8000         │    │   PostgreSQL    │
└─────────────────┘    └─────────────────┘    │   :5432         │
                                              └─────────────────┘
        │                                              │
        │                                              │
        ▼                                              ▼
┌─────────────────┐                        ┌─────────────────┐
│   Nginx         │                        │   Redis         │
│   Reverse Proxy │                        │   Cache         │
│   :80           │                        │   :6379         │
└─────────────────┘                        └─────────────────┘
```

## 🔧 Configuration des connexions

### 1. Frontend → Backend

**Configuration dans le frontend :**
```javascript
// frontend/src/config/api.js
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const apiConfig = {
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
};
```

**Variable d'environnement :**
```env
# frontend/.env
REACT_APP_API_URL=http://localhost:8000
```

**Exemple d'utilisation :**
```javascript
// Appel API depuis le frontend
const response = await fetch(`${API_BASE_URL}/api/v1/students`, {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
});
```

### 2. Backend → Base de données

**Configuration dans le backend :**
```python
# backend/app/core/database.py
DATABASE_URL = "postgresql://lsu_user:lsu_password@postgres:5432/lsu_db"

# Conversion pour async
async_database_url = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

engine = create_async_engine(
    async_database_url,
    echo=settings.DEBUG,
    pool_pre_ping=True,
    pool_recycle=300,
)
```

**Variable d'environnement :**
```env
# backend/.env
DATABASE_URL=postgresql://lsu_user:lsu_password@postgres:5432/lsu_db
```

### 3. Nginx → Frontend + Backend

**Configuration Nginx :**
```nginx
# docker/nginx/nginx.conf
upstream backend {
    server backend:8000;
}

upstream frontend {
    server frontend:3000;
}

server {
    listen 80;
    
    # API routes
    location /api/ {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Frontend routes
    location / {
        proxy_pass http://frontend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 🧪 Test des connexions

### Test manuel

#### 1. Test de la base de données
```bash
# Connexion directe à PostgreSQL
docker-compose exec postgres psql -U lsu_user -d lsu_db

# Test de requête
SELECT COUNT(*) FROM students;
```

#### 2. Test du backend API
```bash
# Test de santé
curl http://localhost:8000/health

# Test de la route racine
curl http://localhost:8000/

# Test de la documentation
curl http://localhost:8000/docs

# Test de l'API (authentification requise)
curl http://localhost:8000/api/v1/students
```

#### 3. Test du frontend
```bash
# Test de la page d'accueil
curl http://localhost:3000

# Test avec navigateur
open http://localhost:3000
```

#### 4. Test de Redis
```bash
# Connexion à Redis
docker-compose exec redis redis-cli

# Test de ping
PING
```

#### 5. Test de Nginx
```bash
# Test du proxy
curl http://localhost:80/api/

# Test du frontend via proxy
curl http://localhost:80/
```

### Test automatique

Utilisez le script de test :
```bash
# Test complet
./test_connections.sh

# Test spécifique
./test_connections.sh backend
./test_connections.sh frontend
./test_connections.sh postgres
```

## 🔍 Diagnostic des problèmes

### 1. Problème de connexion Frontend → Backend

**Symptômes :**
- Erreur CORS dans la console
- Erreur 404 sur les appels API
- Frontend ne charge pas les données

**Solutions :**
```bash
# Vérifier que le backend est démarré
docker-compose ps backend

# Vérifier les logs du backend
docker-compose logs backend

# Tester l'API directement
curl http://localhost:8000/health

# Vérifier la configuration CORS
# backend/app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 2. Problème de connexion Backend → Base de données

**Symptômes :**
- Erreur 500 sur les routes API
- Messages d'erreur de connexion DB
- Timeout sur les requêtes

**Solutions :**
```bash
# Vérifier que PostgreSQL est démarré
docker-compose ps postgres

# Vérifier les logs PostgreSQL
docker-compose logs postgres

# Tester la connexion DB
docker-compose exec postgres pg_isready -U lsu_user -d lsu_db

# Vérifier les variables d'environnement
docker-compose exec backend env | grep DATABASE
```

### 3. Problème de ports

**Symptômes :**
- Impossible d'accéder aux services
- Erreur "Connection refused"
- Ports déjà utilisés

**Solutions :**
```bash
# Vérifier les ports utilisés
lsof -i :3000
lsof -i :8000
lsof -i :5432

# Arrêter les services qui utilisent les ports
sudo lsof -ti:3000 | xargs kill -9

# Redémarrer les conteneurs
docker-compose restart
```

## 📊 Monitoring des connexions

### 1. Logs en temps réel
```bash
# Tous les services
docker-compose logs -f

# Service spécifique
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f postgres
```

### 2. Statut des conteneurs
```bash
# Statut général
docker-compose ps

# Informations détaillées
docker-compose ps -a
```

### 3. Utilisation des ressources
```bash
# Statistiques des conteneurs
docker stats

# Utilisation du disque
docker system df
```

## 🔒 Sécurité des connexions

### 1. Authentification JWT
```python
# backend/app/core/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token invalide")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide")
    
    return username
```

### 2. CORS Configuration
```python
# backend/app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### 3. Rate Limiting
```nginx
# docker/nginx/nginx.conf
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;

location /api/ {
    limit_req zone=api burst=20 nodelay;
    proxy_pass http://backend;
}
```

## 🚀 Optimisation des connexions

### 1. Pool de connexions
```python
# backend/app/core/database.py
engine = create_async_engine(
    async_database_url,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True,
    pool_recycle=300,
)
```

### 2. Cache Redis
```python
# backend/app/core/cache.py
import redis.asyncio as redis

redis_client = redis.from_url(settings.REDIS_URL)

async def get_cached_data(key: str):
    return await redis_client.get(key)

async def set_cached_data(key: str, value: str, expire: int = 3600):
    await redis_client.setex(key, expire, value)
```

### 3. Compression Gzip
```nginx
# docker/nginx/nginx.conf
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript;
```

## 📝 Checklist de vérification

### Avant le démarrage
- [ ] Docker et Docker Compose installés
- [ ] Ports 3000, 8000, 5432 disponibles
- [ ] Fichier .env configuré
- [ ] Variables d'environnement définies

### Après le démarrage
- [ ] PostgreSQL accessible sur localhost:5432
- [ ] Backend API accessible sur localhost:8000
- [ ] Frontend accessible sur localhost:3000
- [ ] Documentation API accessible sur localhost:8000/docs
- [ ] Redis accessible sur localhost:6379 (optionnel)
- [ ] Nginx accessible sur localhost:80 (optionnel)

### Tests de fonctionnalité
- [ ] Création d'un élève via API
- [ ] Affichage des élèves dans le frontend
- [ ] Génération de commentaire IA
- [ ] Sauvegarde en base de données
- [ ] Authentification utilisateur

## 🆘 Support et dépannage

### Commandes utiles
```bash
# Redémarrer tous les services
docker-compose restart

# Reconstruire les images
docker-compose build --no-cache

# Nettoyer complètement
docker-compose down -v
docker system prune -f

# Voir les logs d'erreur
docker-compose logs --tail=100 backend

# Accéder au shell d'un conteneur
docker-compose exec backend bash
docker-compose exec postgres psql -U lsu_user -d lsu_db
```

### Ressources de diagnostic
- **Logs** : `docker-compose logs -f`
- **Statut** : `docker-compose ps`
- **Ressources** : `docker stats`
- **Tests** : `./test_connections.sh`
- **Documentation** : http://localhost:8000/docs 