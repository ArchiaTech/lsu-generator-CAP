# 🎓 Guide de Lancement - Application LSU

## 🚀 **Méthodes de lancement disponibles**

### **1. Lancement simple (Recommandé)**
```bash
./lancer_lsu.sh
```
- ✅ Démarre un serveur Python local
- ✅ Ouvre automatiquement le navigateur
- ✅ Affiche "Page chargée avec succès"
- ✅ Rapide et simple

### **2. Lancement avec Docker (Complet)**
```bash
./launch_lsu.sh
```
- ✅ Démarre tous les services (Frontend, Backend, PostgreSQL, Redis)
- ✅ Construction complète des images Docker
- ✅ Plus lent mais fonctionnalités complètes

### **3. Lancement Python direct**
```bash
python3 launch_lsu.py
```
- ✅ Script Python avec vérifications
- ✅ Gestion d'erreurs avancée

### **4. Lancement rapide (Vérification)**
```bash
./quick_launch.sh
```
- ✅ Vérifie si les services sont déjà actifs
- ✅ Redémarre si nécessaire

## 🌐 **Accès à l'application**

### **URLs principales :**
- **Frontend** : http://localhost:3000
- **Backend API** : http://localhost:8000 (si Docker)
- **Documentation API** : http://localhost:8000/docs (si Docker)

### **Pages disponibles :**
- `index.html` - Page d'accueil
- `student_profile_page.html` - Profil élève
- `create_student.html` - Création d'élève
- `student_list.html` - Liste des élèves
- `photos_classe_pro.html` - Photos de classe
- `dashboard.html` - Tableau de bord

## 🛠️ **Commandes utiles**

### **Vérification des services :**
```bash
# Vérifier les ports
lsof -ti:3000
lsof -ti:8000

# Vérifier Docker
docker-compose ps

# Vérifier les logs
docker-compose logs -f
```

### **Arrêt des services :**
```bash
# Arrêter Docker
docker-compose down

# Arrêter le serveur Python
# Ctrl+C dans le terminal
```

### **Redémarrage :**
```bash
# Redémarrage rapide
docker-compose restart

# Redémarrage complet
./start.sh
```

## 📋 **Messages de succès attendus**

### **Lancement simple :**
```
🎓 Lancement Application LSU
============================
✅ Serveur démarré sur http://localhost:3000
✅ Navigateur ouvert automatiquement
✅ Page chargée avec succès
🎉 Application LSU prête !
```

### **Lancement Docker :**
```
🎓 Système de Gestion LSU
================================
[INFO] ✅ PostgreSQL est prêt
[INFO] ✅ Backend API est prêt
[INFO] ✅ Frontend est prêt
[INFO] 🎉 Système LSU démarré avec succès !
```

## 🔧 **Dépannage**

### **Port déjà utilisé :**
```bash
# Identifier le processus
lsof -ti:3000

# Arrêter le processus
kill -9 [PID]
```

### **Docker non démarré :**
```bash
# Démarrer Docker
open -a Docker

# Attendre et relancer
sleep 10 && ./lancer_lsu.sh
```

### **Erreur de permissions :**
```bash
# Rendre les scripts exécutables
chmod +x *.sh
```

## 📱 **Utilisation de l'application**

1. **Ouvrir** http://localhost:3000
2. **Naviguer** dans les différentes pages
3. **Tester** les fonctionnalités :
   - Création d'élèves
   - Gestion des photos
   - Import/Export de données
4. **Arrêter** avec Ctrl+C

## 🎯 **Scripts créés**

- `lancer_lsu.sh` - Lancement simple (recommandé)
- `launch_lsu.sh` - Lancement Docker complet
- `quick_launch.sh` - Lancement rapide avec vérification
- `launch_lsu.py` - Version Python
- `start.sh` - Script Docker original

---

**💡 Conseil :** Utilisez `./lancer_lsu.sh` pour un démarrage rapide et simple ! 