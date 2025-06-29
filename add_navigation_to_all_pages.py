#!/usr/bin/env python3
"""
Script pour ajouter la barre de navigation cohérente à toutes les pages HTML du projet LSU
"""

import os
import re
from pathlib import Path

# Code de la barre de navigation
NAVIGATION_HTML = '''    <!-- Barre de Navigation LSU -->
    <nav class="nav-bar">
        <div class="nav-container">
            <div class="nav-logo">
                <a href="index.html" class="logo-link">
                    <span class="logo-icon">🎓</span>
                    <span class="logo-text">LSU Pro</span>
                </a>
            </div>
            
            <div class="nav-menu" id="navMenu">
                <a href="index.html" class="nav-link">
                    <span class="nav-icon">🏠</span>
                    Accueil
                </a>
                <a href="improved_lsu_generator.html" class="nav-link">
                    <span class="nav-icon">📝</span>
                    Générateur LSU
                </a>
                <a href="student_profile_page.html" class="nav-link">
                    <span class="nav-icon">👤</span>
                    Profils Élèves
                </a>
                <a href="photos_classe_pro.html" class="nav-link">
                    <span class="nav-icon">📸</span>
                    Photos Classe
                </a>
                <a href="lsu_connection_test.html" class="nav-link">
                    <span class="nav-icon">🔧</span>
                    Tests Connexion
                </a>
                <a href="test_navigation.html" class="nav-link">
                    <span class="nav-icon">🧭</span>
                    Navigation
                </a>
            </div>
            
            <div class="nav-toggle" id="navToggle">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>
'''

# Styles CSS de la barre de navigation
NAVIGATION_CSS = '''        /* Barre de Navigation LSU */
        .nav-bar {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 3px solid #3498db;
        }

        .nav-container {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 20px;
            height: 70px;
        }

        .nav-logo {
            display: flex;
            align-items: center;
        }

        .logo-link {
            display: flex;
            align-items: center;
            text-decoration: none;
            color: white;
            font-size: 1.5em;
            font-weight: bold;
            transition: all 0.3s;
        }

        .logo-link:hover {
            transform: scale(1.05);
            text-shadow: 0 0 10px rgba(52, 152, 219, 0.5);
        }

        .logo-icon {
            font-size: 1.8em;
            margin-right: 10px;
        }

        .logo-text {
            background: linear-gradient(45deg, #3498db, #2ecc71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-menu {
            display: flex;
            gap: 5px;
            align-items: center;
        }

        .nav-link {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 12px 16px;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.3s;
            font-weight: 500;
            position: relative;
            overflow: hidden;
        }

        .nav-link::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: left 0.5s;
        }

        .nav-link:hover::before {
            left: 100%;
        }

        .nav-link:hover {
            background: rgba(52, 152, 219, 0.2);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.3);
        }

        .nav-link.active {
            background: rgba(52, 152, 219, 0.3);
            box-shadow: 0 0 15px rgba(52, 152, 219, 0.5);
        }

        .nav-icon {
            font-size: 1.2em;
        }

        .nav-toggle {
            display: none;
            flex-direction: column;
            cursor: pointer;
            gap: 4px;
        }

        .nav-toggle span {
            width: 25px;
            height: 3px;
            background: white;
            border-radius: 2px;
            transition: all 0.3s;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .nav-menu {
                position: fixed;
                top: 70px;
                left: -100%;
                width: 100%;
                height: calc(100vh - 70px);
                background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                flex-direction: column;
                padding: 20px;
                transition: left 0.3s;
                gap: 10px;
            }

            .nav-menu.active {
                left: 0;
            }

            .nav-link {
                width: 100%;
                justify-content: center;
                padding: 15px;
                font-size: 1.1em;
            }

            .nav-toggle {
                display: flex;
            }

            .nav-toggle.active span:nth-child(1) {
                transform: rotate(45deg) translate(5px, 5px);
            }

            .nav-toggle.active span:nth-child(2) {
                opacity: 0;
            }

            .nav-toggle.active span:nth-child(3) {
                transform: rotate(-45deg) translate(7px, -6px);
            }
        }

        /* Animation d'entrée */
        @keyframes slideInDown {
            from {
                transform: translateY(-100%);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        .nav-bar {
            animation: slideInDown 0.5s ease-out;
        }
'''

# Script JavaScript de la navigation
NAVIGATION_JS = '''        // Script pour la navigation
        document.addEventListener('DOMContentLoaded', function() {
            const navToggle = document.getElementById('navToggle');
            const navMenu = document.getElementById('navMenu');
            const navLinks = document.querySelectorAll('.nav-link');
            
            // Toggle menu mobile
            navToggle.addEventListener('click', function() {
                navMenu.classList.toggle('active');
                navToggle.classList.toggle('active');
            });
            
            // Fermer le menu en cliquant sur un lien
            navLinks.forEach(link => {
                link.addEventListener('click', function() {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                });
            });
            
            // Marquer le lien actif
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            navLinks.forEach(link => {
                if (link.getAttribute('href') === currentPage) {
                    link.classList.add('active');
                }
            });
            
            // Fermer le menu en cliquant à l'extérieur
            document.addEventListener('click', function(event) {
                if (!event.target.closest('.nav-bar')) {
                    navMenu.classList.remove('active');
                    navToggle.classList.remove('active');
                }
            });
        });
'''

def add_navigation_to_file(file_path):
    """Ajoute la barre de navigation à un fichier HTML"""
    print(f"Traitement de {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si la navigation est déjà présente
        if 'nav-bar' in content:
            print(f"  ⚠️  Navigation déjà présente dans {file_path}")
            return False
        
        # Ajouter les styles CSS
        if '<style>' in content:
            # Insérer après la première balise <style>
            style_pattern = r'(<style>)'
            content = re.sub(style_pattern, r'\1\n' + NAVIGATION_CSS, content, count=1)
        else:
            # Ajouter une section style dans le head
            head_pattern = r'(</head>)'
            content = re.sub(head_pattern, f'    <style>\n{NAVIGATION_CSS}\n    </style>\n\\1', content, count=1)
        
        # Ajouter la structure HTML
        body_pattern = r'(<body>)'
        content = re.sub(body_pattern, r'\1\n' + NAVIGATION_HTML, content, count=1)
        
        # Ajouter le script JavaScript
        if '<script>' in content:
            # Insérer au début du premier script
            script_pattern = r'(<script>)'
            content = re.sub(script_pattern, r'\1\n' + NAVIGATION_JS, content, count=1)
        else:
            # Ajouter avant la fermeture du body
            body_close_pattern = r'(</body>)'
            content = re.sub(body_close_pattern, f'    <script>\n{NAVIGATION_JS}\n    </script>\n\\1', content, count=1)
        
        # Sauvegarder le fichier
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Navigation ajoutée avec succès à {file_path}")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale"""
    print("🎓 Ajout de la barre de navigation à toutes les pages HTML")
    print("=" * 60)
    
    # Liste des fichiers HTML à traiter
    html_files = [
        'improved_lsu_generator.html',
        'student_profile_page.html',
        'lsu_connection_test.html',
        'test_navigation.html'
    ]
    
    success_count = 0
    total_count = len(html_files)
    
    for html_file in html_files:
        if os.path.exists(html_file):
            if add_navigation_to_file(html_file):
                success_count += 1
        else:
            print(f"  ⚠️  Fichier {html_file} non trouvé")
    
    print("\n" + "=" * 60)
    print(f"📊 Résumé: {success_count}/{total_count} fichiers traités avec succès")
    
    if success_count == total_count:
        print("🎉 Toutes les pages ont maintenant une navigation cohérente !")
    else:
        print("⚠️  Certaines pages n'ont pas pu être traitées")

if __name__ == "__main__":
    main() 