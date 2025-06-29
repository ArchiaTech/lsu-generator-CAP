# 🎓 Système de Gestion LSU - Livret Scolaire Unique

Un système complet de gestion pédagogique pour l'école primaire, comprenant un générateur de commentaires intelligent, une gestion des profils élèves et une interface moderne.

## 🚀 Fonctionnalités

### ✨ Générateur de Commentaires
- **IA intégrée** pour générer des commentaires personnalisés
- **Templates adaptés** par niveau scolaire (CP à CM2)
- **Personnalisation** selon les points forts et difficultés
- **Export PDF** et sauvegarde automatique

### 👤 Gestion des Élèves
- **Profils complets** avec informations personnelles
- **Suivi des compétences** par domaine
- **Historique des évaluations** avec graphiques
- **Gestion des contacts** familiaux

### 🎯 Interface Moderne
- **Design responsive** (mobile, tablette, desktop)
- **Navigation intuitive** entre les pages
- **Thème cohérent** avec l'identité visuelle LSU
- **Accessibilité** optimisée

## 🛠️ Architecture Technique

### Backend (FastAPI + Python)
- **API REST** complète avec documentation Swagger
- **Base de données** PostgreSQL pour la persistance
- **Cache Redis** pour les performances
- **Authentification** et autorisation
- **Validation** des données avec Pydantic

### Frontend (React + TypeScript)
- **Interface moderne** avec Tailwind CSS
- **Gestion d'état** avec React Query
- **Formulaires** avec React Hook Form
- **Graphiques** avec Recharts
- **Animations** avec Framer Motion

### Infrastructure (Docker)
- **Conteneurisation** complète
- **Orchestration** avec Docker Compose
- **Reverse proxy** Nginx pour la production
- **Base de données** persistante

## 📋 Prérequis

- **Docker** et **Docker Compose**
- **Git** pour le clonage
- **4GB RAM** minimum
- **Ports disponibles** : 3000, 8000, 5432, 6379

## 🚀 Installation Rapide

### 1. Cloner le repository
```bash
git clone https://github.com/votre-username/lsu-system.git
cd lsu-system
```

### 2. Configuration des variables d'environnement
```bash
cp env.example .env
# Éditer .env avec vos paramètres
```

### 3. Démarrage du système
```bash
chmod +x start.sh
./start.sh
```

### 4. Vérification
```bash
./test_complet.sh
```

## 🔧 Configuration Détaillée

### Variables d'environnement (.env)
```env
# Base de données
POSTGRES_DB=lsu_db
POSTGRES_USER=lsu_user
POSTGRES_PASSWORD=lsu_password

# Backend
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
DEBUG=True

# Frontend
REACT_APP_API_URL=http://localhost:8000
REACT_APP_ENV=development

# Redis
REDIS_URL=redis://redis:6379

# Sécurité
SECRET_KEY=votre-clé-secrète-ici
```

### Structure des dossiers
```
lsu-system/
├── backend/                 # API FastAPI
│   ├── app/
│   │   ├── api/            # Routes API
│   │   │   ├── core/           # Configuration
│   │   │   ├── models/         # Modèles SQLAlchemy
│   │   │   └── schemas/        # Schémas Pydantic
│   │   ├── requirements.txt
│   │   └── main.py
│   ├── frontend/               # Application React
│   │   ├── src/
│   │   │   ├── components/     # Composants React
│   │   │   ├── pages/         # Pages de l'application
│   │   │   ├── hooks/         # Hooks personnalisés
│   │   │   └── utils/         # Utilitaires
│   │   ├── package.json
│   │   └── tailwind.config.js
│   ├── database/              # Scripts SQL
│   ├── docker/               # Configuration Docker
│   ├── docs/                 # Documentation
│   └── docker-compose.yml    # Orchestration
```

## 🧪 Tests et Vérification

### Test automatique complet
```bash
./test_complet.sh
```

### Test manuel des connexions
```bash
./test_connections.sh
```

### Vérification des services
```bash
# Statut des conteneurs
docker-compose ps

# Logs en temps réel
docker-compose logs -f

# Logs d'un service spécifique
docker-compose logs backend
```

## 🌐 Accès au Système

### Développement
- **Frontend React** : http://localhost:3000
- **Backend API** : http://localhost:8000
- **Documentation API** : http://localhost:8000/docs
- **Page d'accueil HTML** : http://localhost:3000/lsu_index.html
- **Générateur HTML** : http://localhost:3000/improved_lsu_generator.html
- **Profil élève HTML** : http://localhost:3000/student_profile_page.html

### Production
- **Application** : https://votre-domaine.com
- **API** : https://api.votre-domaine.com

## 📚 Documentation API

### Endpoints principaux
- `GET /api/v1/students/` - Liste des élèves
- `POST /api/v1/students/` - Créer un élève
- `GET /api/v1/students/{id}` - Détails d'un élève
- `PUT /api/v1/students/{id}` - Modifier un élève
- `DELETE /api/v1/students/{id}` - Supprimer un élève

### Authentification
```bash
# Exemple de requête authentifiée
curl -H "Authorization: Bearer votre-token" \
     http://localhost:8000/api/v1/students/
```

## 🔒 Sécurité

### Bonnes pratiques implémentées
- **Validation** des données d'entrée
- **Sanitisation** des requêtes SQL
- **CORS** configuré
- **Rate limiting** sur les API
- **Logs** de sécurité
- **Variables d'environnement** pour les secrets

### Recommandations de déploiement
- **HTTPS** obligatoire en production
- **Firewall** configuré
- **Backup** automatique de la base
- **Monitoring** des performances
- **Mise à jour** régulière des dépendances

## 🚀 Déploiement

### Développement local
```bash
# Démarrage rapide
./start.sh

# Ou étape par étape
docker-compose up -d
```

### Production
```bash
# Build de production
docker-compose -f docker-compose.prod.yml up -d

# Avec Nginx
docker-compose -f docker-compose.prod.yml up -d nginx
```

### Variables de production
```env
DEBUG=False
SECRET_KEY=clé-secrète-forte
DATABASE_URL=postgresql://user:pass@host:5432/db
REDIS_URL=redis://host:6379
```

## 🤝 Contribution

### Comment contribuer
1. **Fork** le projet
2. **Créer** une branche feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** vos changements (`git commit -m 'Add AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrir** une Pull Request

### Standards de code
- **Python** : PEP 8, type hints
- **JavaScript/TypeScript** : ESLint, Prettier
- **Tests** : pytest pour le backend, Jest pour le frontend
- **Documentation** : docstrings, README à jour

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Équipe

- **Développeur principal** : [Votre nom]
- **Design** : [Nom du designer]
- **Tests** : [Nom du testeur]

## 📞 Support

### Contact
- **Email** : support@lsu-system.com
- **Issues** : [GitHub Issues](https://github.com/votre-username/lsu-system/issues)
- **Documentation** : [Wiki](https://github.com/votre-username/lsu-system/wiki)

### FAQ
**Q: Comment ajouter un nouvel élève ?**
R: Utilisez l'interface web ou l'API POST /api/v1/students/

**Q: Comment générer un commentaire ?**
R: Accédez au générateur via l'interface ou utilisez l'API d'IA

**Q: Comment sauvegarder les données ?**
R: Les données sont automatiquement sauvegardées en base PostgreSQL

## 🎯 Roadmap

### Version 2.0 (Q2 2025)
- [ ] **Authentification** multi-utilisateurs
- [ ] **Notifications** en temps réel
- [ ] **Export** vers LSU officiel
- [ ] **Mobile app** native

### Version 2.1 (Q3 2025)
- [ ] **Analytics** avancées
- [ ] **Intégration** avec Pronote
- [ ] **API** publique
- [ ] **Plugins** système

---

**⭐ Si ce projet vous aide, n'oubliez pas de le star sur GitHub !** 