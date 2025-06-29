# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer au Système de Gestion LSU ! Ce document vous guidera dans le processus de contribution.

## 📋 Table des matières

- [Code de conduite](#code-de-conduite)
- [Comment contribuer](#comment-contribuer)
- [Configuration de l'environnement](#configuration-de-lenvironnement)
- [Standards de code](#standards-de-code)
- [Tests](#tests)
- [Pull Request](#pull-request)
- [Questions et support](#questions-et-support)

## 📜 Code de conduite

Ce projet et ses contributeurs s'engagent à maintenir un environnement respectueux et inclusif. En participant, vous acceptez de respecter notre code de conduite.

### Nos standards

- Utiliser un langage accueillant et inclusif
- Respecter les différents points de vue et expériences
- Accepter gracieusement les critiques constructives
- Se concentrer sur ce qui est le mieux pour la communauté
- Faire preuve d'empathie envers les autres membres

## 🚀 Comment contribuer

### Types de contributions

Nous accueillons différents types de contributions :

- **🐛 Rapports de bugs** : Signaler des problèmes
- **✨ Nouvelles fonctionnalités** : Proposer des améliorations
- **📚 Documentation** : Améliorer la documentation
- **🧪 Tests** : Ajouter ou améliorer les tests
- **🎨 Interface** : Améliorer l'expérience utilisateur
- **🔧 Optimisations** : Améliorer les performances

### Processus de contribution

1. **Vérifier les issues existantes**
   - Regardez les issues ouvertes et fermées
   - Évitez de dupliquer le travail existant

2. **Créer une issue** (si nécessaire)
   - Décrivez clairement le problème ou la fonctionnalité
   - Incluez des étapes de reproduction pour les bugs
   - Ajoutez des captures d'écran si pertinent

3. **Fork le repository**
   - Cliquez sur "Fork" en haut à droite
   - Clonez votre fork localement

4. **Créer une branche**
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   # ou
   git checkout -b fix/nom-du-bug
   ```

5. **Développer**
   - Suivez les standards de code
   - Ajoutez des tests si nécessaire
   - Mettez à jour la documentation

6. **Tester**
   ```bash
   # Tests backend
   cd backend && pytest
   
   # Tests frontend
   cd frontend && npm test
   
   # Tests complets
   ./test_complet.sh
   ```

7. **Commit et push**
   ```bash
   git add .
   git commit -m "feat: ajouter nouvelle fonctionnalité"
   git push origin feature/nom-de-la-fonctionnalite
   ```

8. **Créer une Pull Request**
   - Remplissez le template de PR
   - Décrivez clairement les changements
   - Référencez les issues concernées

## ⚙️ Configuration de l'environnement

### Prérequis

- **Docker** et **Docker Compose**
- **Git**
- **Node.js** 18+ (pour le développement frontend)
- **Python** 3.11+ (pour le développement backend)

### Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/lsu-system.git
   cd lsu-system
   ```

2. **Configuration des variables d'environnement**
   ```bash
   cp env.example .env
   # Éditer .env avec vos paramètres
   ```

3. **Démarrage de l'environnement**
   ```bash
   ./start.sh
   ```

4. **Vérification**
   ```bash
   ./test_complet.sh
   ```

### Développement local

#### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend (React)
```bash
cd frontend
npm install
npm start
```

## 📝 Standards de code

### Python (Backend)

- **PEP 8** : Respecter les conventions de style
- **Type hints** : Utiliser les annotations de type
- **Docstrings** : Documenter les fonctions et classes
- **Noms** : Utiliser des noms descriptifs

```python
from typing import List, Optional
from pydantic import BaseModel

class Student(BaseModel):
    """Modèle représentant un élève."""
    
    id: Optional[int] = None
    first_name: str
    last_name: str
    level: str
    
    def get_full_name(self) -> str:
        """Retourne le nom complet de l'élève."""
        return f"{self.first_name} {self.last_name}"
```

### TypeScript/JavaScript (Frontend)

- **ESLint** : Respecter les règles de linting
- **Prettier** : Formater le code automatiquement
- **TypeScript** : Utiliser les types strictement
- **Noms** : Utiliser des noms descriptifs

```typescript
interface Student {
  id?: number;
  firstName: string;
  lastName: string;
  level: string;
}

const getFullName = (student: Student): string => {
  return `${student.firstName} ${student.lastName}`;
};
```

### Git

- **Messages de commit** : Utiliser le format conventionnel
  - `feat:` nouvelle fonctionnalité
  - `fix:` correction de bug
  - `docs:` documentation
  - `style:` formatage
  - `refactor:` refactorisation
  - `test:` tests
  - `chore:` maintenance

```bash
git commit -m "feat: ajouter génération de commentaires IA"
git commit -m "fix: corriger bug d'affichage sur mobile"
git commit -m "docs: mettre à jour README"
```

## 🧪 Tests

### Backend (Python)

```bash
cd backend
pytest                    # Tous les tests
pytest -v                # Tests avec détails
pytest --cov=app         # Tests avec couverture
pytest tests/test_api.py # Tests spécifiques
```

### Frontend (React)

```bash
cd frontend
npm test                 # Tous les tests
npm test -- --coverage   # Tests avec couverture
npm test -- --watch      # Tests en mode watch
```

### Tests d'intégration

```bash
./test_complet.sh        # Tests complets du système
./test_connections.sh    # Tests des connexions
```

## 🔄 Pull Request

### Template de PR

```markdown
## Description
Brève description des changements apportés.

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Breaking change
- [ ] Documentation

## Tests
- [ ] Tests unitaires passent
- [ ] Tests d'intégration passent
- [ ] Tests manuels effectués

## Checklist
- [ ] Code respecte les standards
- [ ] Documentation mise à jour
- [ ] Tests ajoutés/modifiés
- [ ] Pas de régression introduite

## Screenshots (si applicable)
Ajoutez des captures d'écran pour les changements UI.

## Issues liées
Fixes #123
```

### Processus de review

1. **Automatique** : Les tests CI/CD s'exécutent
2. **Code review** : Au moins un maintainer doit approuver
3. **Tests** : Vérification que tous les tests passent
4. **Documentation** : Mise à jour si nécessaire
5. **Merge** : Une fois approuvé, la PR est mergée

## ❓ Questions et support

### Ressources

- **Documentation** : `/docs`
- **Issues** : [GitHub Issues](https://github.com/votre-username/lsu-system/issues)
- **Discussions** : [GitHub Discussions](https://github.com/votre-username/lsu-system/discussions)
- **Wiki** : [GitHub Wiki](https://github.com/votre-username/lsu-system/wiki)

### Contact

- **Email** : support@lsu-system.com
- **Discord** : [Serveur Discord](https://discord.gg/lsu-system)
- **Twitter** : [@LSU_System](https://twitter.com/LSU_System)

## 🎉 Reconnaissance

Tous les contributeurs sont listés dans le fichier [CONTRIBUTORS.md](CONTRIBUTORS.md).

### Badges

Les contributeurs actifs reçoivent des badges :

- 🥇 **Gold** : 50+ contributions
- 🥈 **Silver** : 20+ contributions  
- 🥉 **Bronze** : 5+ contributions

---

**Merci de contribuer au Système de Gestion LSU ! 🎓** 