# 🚀 Documentation des Routes API - Système LSU

## Vue d'ensemble

L'API REST du système de gestion LSU est organisée autour de 6 modules principaux :

- **Élèves** (`/api/v1/students`) - Gestion des profils d'élèves
- **Compétences** (`/api/v1/competences`) - Évaluation des compétences LSU
- **Commentaires** (`/api/v1/comments`) - Génération et gestion des commentaires
- **Évaluations** (`/api/v1/evaluations`) - Historique des évaluations
- **Utilisateurs** (`/api/v1/users`) - Gestion des enseignants
- **IA** (`/api/v1/ai`) - Services d'intelligence artificielle

## 🔐 Authentification

Toutes les routes (sauf `/health` et `/docs`) nécessitent une authentification JWT.

```bash
# Obtenir un token
POST /api/v1/auth/login
{
  "username": "teacher1",
  "password": "password"
}

# Utiliser le token
Authorization: Bearer <token>
```

## 📚 Routes par Module

### 🎓 Élèves (`/api/v1/students`)

#### `GET /api/v1/students/`
Récupérer la liste des élèves avec filtres et pagination.

**Paramètres de requête :**
- `skip` (int, défaut: 0) - Nombre d'éléments à ignorer
- `limit` (int, défaut: 100, max: 1000) - Nombre maximum d'éléments
- `level` (string, optionnel) - Filtrer par niveau (CP, CE1, CE2, CM1, CM2)
- `is_active` (boolean, optionnel) - Filtrer par statut actif
- `search` (string, optionnel) - Recherche par nom/prénom
- `class_name` (string, optionnel) - Filtrer par classe
- `school_year` (string, optionnel) - Filtrer par année scolaire

**Réponse :**
```json
[
  {
    "id": 1,
    "first_name": "Léa",
    "last_name": "Martin",
    "full_name": "Léa Martin",
    "level": "CM1",
    "class_name": "CM1-A",
    "school_year": "2024-2025",
    "is_active": true,
    "age": 9
  }
]
```

#### `GET /api/v1/students/{student_id}`
Récupérer un élève par son ID.

**Réponse :**
```json
{
  "id": 1,
  "first_name": "Léa",
  "last_name": "Martin",
  "full_name": "Léa Martin",
  "birth_date": "2015-03-15",
  "age": 9,
  "gender": "F",
  "level": "CM1",
  "class_name": "CM1-A",
  "school_year": "2024-2025",
  "teacher_id": 2,
  "address": "12 rue de la Paix, 75001 Paris",
  "phone": "01 23 45 67 89",
  "email": "lea.martin@email.com",
  "parent1_name": "Pierre Martin",
  "parent1_phone": "06 12 34 56 78",
  "parent1_email": "pierre.martin@email.com",
  "parent1_profession": "Ingénieur",
  "parent2_name": "Sophie Martin",
  "parent2_phone": "06 98 76 54 32",
  "parent2_email": "sophie.martin@email.com",
  "parent2_profession": "Professeure",
  "strengths": "Mathématiques, Arts plastiques",
  "difficulties": "Expression écrite",
  "objectives": "Améliorer la rédaction",
  "is_active": true,
  "notes": "Élève motivée et curieuse",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

#### `POST /api/v1/students/`
Créer un nouvel élève.

**Corps de la requête :**
```json
{
  "first_name": "Nouvel",
  "last_name": "Élève",
  "birth_date": "2015-06-15",
  "gender": "M",
  "level": "CM1",
  "class_name": "CM1-A",
  "school_year": "2024-2025",
  "address": "123 rue Example",
  "phone": "01 23 45 67 89",
  "email": "nouvel.eleve@email.com",
  "parent1_name": "Parent Un",
  "parent1_phone": "06 12 34 56 78",
  "parent1_email": "parent1@email.com",
  "parent1_profession": "Profession",
  "strengths": "Points forts",
  "difficulties": "Difficultés",
  "objectives": "Objectifs"
}
```

#### `PUT /api/v1/students/{student_id}`
Mettre à jour un élève.

**Corps de la requête :** (tous les champs optionnels)
```json
{
  "first_name": "Nouveau Prénom",
  "level": "CM2",
  "class_name": "CM2-B",
  "strengths": "Nouveaux points forts"
}
```

#### `DELETE /api/v1/students/{student_id}`
Supprimer un élève (soft delete).

#### `GET /api/v1/students/{student_id}/profile`
Récupérer le profil complet d'un élève avec toutes ses données.

### 🎯 Compétences (`/api/v1/competences`)

#### `GET /api/v1/competences/`
Récupérer les compétences avec filtres.

**Paramètres :**
- `student_id` (int, optionnel) - Filtrer par élève
- `domain` (string, optionnel) - Filtrer par domaine
- `level` (string, optionnel) - Filtrer par niveau
- `period` (string, optionnel) - Filtrer par période

#### `GET /api/v1/competences/{competence_id}`
Récupérer une compétence spécifique.

#### `POST /api/v1/competences/`
Créer une nouvelle évaluation de compétence.

**Corps de la requête :**
```json
{
  "student_id": 1,
  "domain": "francais_lecture",
  "subdomain": "Fluidité",
  "level": "satisfaisant",
  "score": 3,
  "comment": "Lit avec fluidité, bonne compréhension",
  "strengths": "Fluidité de lecture",
  "difficulties": "Compréhension des textes complexes",
  "evaluation_date": "2024-01-15T10:30:00Z",
  "period": "1er trimestre"
}
```

#### `PUT /api/v1/competences/{competence_id}`
Mettre à jour une compétence.

#### `DELETE /api/v1/competences/{competence_id}`
Supprimer une compétence.

### 💬 Commentaires (`/api/v1/comments`)

#### `GET /api/v1/comments/`
Récupérer les commentaires LSU.

**Paramètres :**
- `student_id` (int, optionnel) - Filtrer par élève
- `period` (string, optionnel) - Filtrer par période
- `school_year` (string, optionnel) - Filtrer par année scolaire
- `is_draft` (boolean, optionnel) - Filtrer par statut brouillon

#### `GET /api/v1/comments/{comment_id}`
Récupérer un commentaire spécifique.

#### `POST /api/v1/comments/`
Créer un nouveau commentaire.

**Corps de la requête :**
```json
{
  "student_id": 1,
  "period": "1er trimestre",
  "school_year": "2024-2025",
  "content": "Léa réalise un premier trimestre satisfaisant...",
  "is_draft": true
}
```

#### `PUT /api/v1/comments/{comment_id}`
Mettre à jour un commentaire.

#### `DELETE /api/v1/comments/{comment_id}`
Supprimer un commentaire.

#### `POST /api/v1/comments/{comment_id}/publish`
Publier un commentaire (changer le statut de brouillon à publié).

### 📊 Évaluations (`/api/v1/evaluations`)

#### `GET /api/v1/evaluations/`
Récupérer les évaluations.

**Paramètres :**
- `student_id` (int, optionnel) - Filtrer par élève
- `subject` (string, optionnel) - Filtrer par matière
- `period` (string, optionnel) - Filtrer par période

#### `GET /api/v1/evaluations/{evaluation_id}`
Récupérer une évaluation spécifique.

#### `POST /api/v1/evaluations/`
Créer une nouvelle évaluation.

**Corps de la requête :**
```json
{
  "student_id": 1,
  "title": "Évaluation Mathématiques - Géométrie",
  "description": "Évaluation sur les propriétés des triangles",
  "subject": "maths_geometrie",
  "evaluation_date": "2024-01-15T10:30:00Z",
  "period": "1er trimestre",
  "results": {
    "score": 15,
    "max_score": 20,
    "details": {
      "triangles": 8,
      "cercles": 7
    }
  },
  "notes": "Bonne compréhension des propriétés"
}
```

### 👥 Utilisateurs (`/api/v1/users`)

#### `GET /api/v1/users/`
Récupérer la liste des utilisateurs (enseignants).

#### `GET /api/v1/users/{user_id}`
Récupérer un utilisateur spécifique.

#### `POST /api/v1/users/`
Créer un nouvel utilisateur.

#### `PUT /api/v1/users/{user_id}`
Mettre à jour un utilisateur.

#### `DELETE /api/v1/users/{user_id}`
Supprimer un utilisateur.

### 🤖 IA (`/api/v1/ai`)

#### `POST /api/v1/ai/generate-comment`
Générer un commentaire LSU avec l'IA.

**Corps de la requête :**
```json
{
  "student_id": 1,
  "period": "1er trimestre",
  "level": "satisfaisant",
  "strengths": ["participation", "autonomie"],
  "specific_points": "Points spécifiques à mentionner",
  "competences_summary": {
    "francais_lecture": "satisfaisant",
    "maths_calcul": "excellent",
    "francais_ecriture": "fragile"
  }
}
```

**Réponse :**
```json
{
  "comment": "Léa réalise un premier trimestre satisfaisant...",
  "model_used": "gpt-4",
  "tokens_used": 150,
  "generation_time": 2.5
}
```

#### `POST /api/v1/ai/analyze-competences`
Analyser les compétences d'un élève.

#### `GET /api/v1/ai/models`
Récupérer la liste des modèles IA disponibles.

## 📈 Codes de Statut HTTP

- `200` - Succès
- `201` - Créé avec succès
- `204` - Supprimé avec succès
- `400` - Requête invalide
- `401` - Non authentifié
- `403` - Non autorisé
- `404` - Ressource non trouvée
- `422` - Erreur de validation
- `500` - Erreur interne du serveur

## 🔄 Pagination

Les listes utilisent une pagination basée sur `skip` et `limit` :

```json
{
  "data": [...],
  "pagination": {
    "skip": 0,
    "limit": 100,
    "total": 150,
    "has_more": true
  }
}
```

## 📝 Validation des Données

Toutes les données sont validées avec Pydantic :

- **Niveaux** : CP, CE1, CE2, CM1, CM2
- **Domaines de compétences** : francais_lecture, maths_calcul, etc.
- **Niveaux de compétence** : insuffisant, fragile, satisfaisant, excellent
- **Années scolaires** : format YYYY-YYYY
- **Emails** : format email valide
- **Téléphones** : format français

## 🚀 Exemples d'Utilisation

### Avec cURL

```bash
# Récupérer tous les élèves
curl -H "Authorization: Bearer <token>" \
     http://localhost:8000/api/v1/students/

# Créer un élève
curl -X POST -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{"first_name":"Nouvel","last_name":"Élève","level":"CM1","school_year":"2024-2025"}' \
     http://localhost:8000/api/v1/students/

# Générer un commentaire IA
curl -X POST -H "Authorization: Bearer <token>" \
     -H "Content-Type: application/json" \
     -d '{"student_id":1,"period":"1er trimestre","level":"satisfaisant"}' \
     http://localhost:8000/api/v1/ai/generate-comment
```

### Avec JavaScript/Fetch

```javascript
// Récupérer les élèves
const response = await fetch('/api/v1/students/', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  }
});

const students = await response.json();

// Créer un élève
const newStudent = await fetch('/api/v1/students/', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    first_name: 'Nouvel',
    last_name: 'Élève',
    level: 'CM1',
    school_year: '2024-2025'
  })
});
```

## 📚 Documentation Interactive

- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

## 🔧 Configuration

L'API peut être configurée via les variables d'environnement :

```env
DATABASE_URL=postgresql://user:pass@host:5432/db
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-key
ANTHROPIC_API_KEY=your-anthropic-key
``` 