#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour intégrer la barre de navigation latérale dans tous les fichiers HTML
de l'application ÉCOLE DU CAP.
"""

import os
import re
from pathlib import Path

def create_sidebar_content():
    """Crée le contenu HTML de la barre latérale."""
    return '''<!-- Barre de navigation latérale - ÉCOLE DU CAP -->
<div id="sidebar" class="fixed left-0 top-0 h-full w-64 bg-gradient-to-b from-indigo-500 to-blue-500 text-white shadow-xl z-50 transition-all duration-300 transform -translate-x-full sm:translate-x-0">
    
    <!-- Logo et nom de l'école -->
    <div class="p-6 border-b border-indigo-400/30">
        <div class="flex items-center space-x-3">
            <div class="text-3xl">🏫</div>
            <div>
                <h1 class="text-xl font-bold">ÉCOLE DU CAP</h1>
                <p class="text-xs text-indigo-100">Navigation principale</p>
            </div>
        </div>
    </div>

    <!-- Navigation -->
    <nav class="mt-6 px-4">
        <ul class="space-y-2">
            <!-- Accueil -->
            <li>
                <a href="index.html" id="nav-accueil" class="nav-link flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-200 hover:bg-white/10 hover:shadow-md group">
                    <span class="text-xl">🏠</span>
                    <span class="font-medium">Accueil</span>
                    <div class="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                        </svg>
                    </div>
                </a>
            </li>

            <!-- Générateur LSU -->
            <li>
                <a href="lsu_generator.html" id="nav-lsu" class="nav-link flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-200 hover:bg-white/10 hover:shadow-md group">
                    <span class="text-xl">🎓</span>
                    <span class="font-medium">Générateur LSU</span>
                    <div class="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                        </svg>
                    </div>
                </a>
            </li>

            <!-- Profils élèves -->
            <li>
                <a href="profils_eleves.html" id="nav-profils" class="nav-link flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-200 hover:bg-white/10 hover:shadow-md group">
                    <span class="text-xl">👨‍🎓</span>
                    <span class="font-medium">Profils élèves</span>
                    <div class="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                        </svg>
                    </div>
                </a>
            </li>

            <!-- Tableau de bord -->
            <li>
                <a href="dashboard.html" id="nav-dashboard" class="nav-link flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-200 hover:bg-white/10 hover:shadow-md group">
                    <span class="text-xl">📊</span>
                    <span class="font-medium">Tableau de bord</span>
                    <div class="ml-auto opacity-0 group-hover:opacity-100 transition-opacity">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                        </svg>
                    </div>
                </a>
            </li>
        </ul>
    </nav>

    <!-- Footer de la sidebar -->
    <div class="absolute bottom-0 left-0 right-0 p-4 border-t border-indigo-400/30">
        <div class="text-center text-xs text-indigo-100">
            <p>© 2025 ÉCOLE DU CAP</p>
            <p class="mt-1">Système de gestion éducative</p>
        </div>
    </div>
</div>

<!-- Bouton burger pour mobile -->
<div id="sidebar-toggle" class="fixed top-4 left-4 z-50 sm:hidden bg-indigo-500 text-white p-2 rounded-lg shadow-lg">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
    </svg>
</div>

<!-- Overlay pour mobile -->
<div id="sidebar-overlay" class="fixed inset-0 bg-black/50 z-40 sm:hidden hidden"></div>'''

def create_sidebar_styles():
    """Crée les styles CSS pour la barre latérale."""
    return '''<!-- Styles CSS pour la sidebar -->
<style>
    /* Animation d'entrée pour la sidebar */
    @keyframes slideIn {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }

    /* Highlight pour la page active */
    .nav-link.active {
        background: rgba(255, 255, 255, 0.15);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #fbbf24;
    }

    /* Animation de survol améliorée */
    .nav-link:hover {
        transform: translateX(4px);
    }

    /* Responsive design */
    @media (max-width: 640px) {
        #sidebar {
            transform: translateX(-100%);
        }
        
        #sidebar.open {
            transform: translateX(0);
        }
    }

    /* Ajustement du contenu principal pour la sidebar */
    .main-content {
        margin-left: 0;
        transition: margin-left 0.3s ease;
    }

    @media (min-width: 640px) {
        .main-content {
            margin-left: 256px; /* w-64 = 16rem = 256px */
        }
    }
</style>'''

def create_sidebar_script():
    """Crée le script JavaScript pour la barre latérale."""
    return '''<!-- Script JavaScript pour la sidebar -->
<script>
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebarOverlay = document.getElementById('sidebar-overlay');
    const navLinks = document.querySelectorAll('.nav-link');

    // Fonction pour marquer la page active
    function setActivePage() {
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === currentPage) {
                link.classList.add('active');
            }
        });
    }

    // Fonction pour basculer la sidebar sur mobile
    function toggleSidebar() {
        sidebar.classList.toggle('open');
        sidebarOverlay.classList.toggle('hidden');
    }

    // Événements pour mobile
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
    }
    
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', toggleSidebar);
    }

    // Fermer la sidebar en cliquant sur un lien (mobile)
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth < 640) {
                toggleSidebar();
            }
        });
    });

    // Marquer la page active au chargement
    setActivePage();

    // Gestion du redimensionnement de fenêtre
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 640) {
            sidebar.classList.remove('open');
            sidebarOverlay.classList.add('hidden');
        }
    });
});
</script>'''

def add_tailwind_css(html_content):
    """Ajoute Tailwind CSS si pas déjà présent."""
    if 'tailwindcss.com' not in html_content and 'tailwind' not in html_content.lower():
        # Ajouter Tailwind CSS CDN
        tailwind_link = '<script src="https://cdn.tailwindcss.com"></script>'
        
        # Insérer après la balise <head>
        if '<head>' in html_content:
            html_content = html_content.replace('<head>', f'<head>\n    {tailwind_link}')
        else:
            # Si pas de head, ajouter au début
            html_content = f'<head>\n    {tailwind_link}\n</head>\n{html_content}'
    
    return html_content

def integrate_sidebar_in_file(file_path):
    """Intègre la barre latérale dans un fichier HTML."""
    print(f"Traitement de {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Vérifier si la sidebar est déjà présente
        if 'id="sidebar"' in content:
            print(f"  ⚠️  Sidebar déjà présente dans {file_path}")
            return False
        
        # Ajouter Tailwind CSS si nécessaire
        content = add_tailwind_css(content)
        
        # Ajouter la classe main-content au body
        if '<body' in content:
            content = re.sub(r'<body([^>]*)>', r'<body\1 class="main-content">', content)
        else:
            content = content.replace('<html>', '<html>\n<body class="main-content">')
            content = content.replace('</html>', '</body>\n</html>')
        
        # Insérer la sidebar après l'ouverture du body
        sidebar_content = create_sidebar_content()
        if '<body' in content:
            body_match = re.search(r'<body[^>]*>', content)
            if body_match:
                insert_pos = body_match.end()
                content = content[:insert_pos] + '\n    ' + sidebar_content + '\n    ' + content[insert_pos:]
        
        # Ajouter les styles CSS dans le head
        sidebar_styles = create_sidebar_styles()
        if '</head>' in content:
            content = content.replace('</head>', f'    {sidebar_styles}\n</head>')
        
        # Ajouter le script JavaScript avant la fermeture du body
        sidebar_script = create_sidebar_script()
        if '</body>' in content:
            content = content.replace('</body>', f'    {sidebar_script}\n</body>')
        
        # Sauvegarder le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Sidebar intégrée avec succès dans {file_path}")
        return True
        
    except Exception as e:
        print(f"  ❌ Erreur lors du traitement de {file_path}: {e}")
        return False

def main():
    """Fonction principale."""
    print("🚀 Intégration de la barre de navigation latérale")
    print("=" * 50)
    
    # Fichiers HTML principaux à traiter
    main_files = [
        'index.html',
        'lsu_generator.html', 
        'profils_eleves.html',
        'dashboard.html'
    ]
    
    # Créer le fichier sidebar.html séparé
    sidebar_content = create_sidebar_content()
    sidebar_styles = create_sidebar_styles()
    sidebar_script = create_sidebar_script()
    
    sidebar_html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sidebar - ÉCOLE DU CAP</title>
    <script src="https://cdn.tailwindcss.com"></script>
    {sidebar_styles}
</head>
<body>
    {sidebar_content}
    {sidebar_script}
</body>
</html>'''
    
    with open('sidebar.html', 'w', encoding='utf-8') as f:
        f.write(sidebar_html)
    
    print("✅ Fichier sidebar.html créé")
    
    # Traiter chaque fichier principal
    success_count = 0
    for file_name in main_files:
        if os.path.exists(file_name):
            if integrate_sidebar_in_file(file_name):
                success_count += 1
        else:
            print(f"  ⚠️  Fichier {file_name} non trouvé")
    
    print("\n" + "=" * 50)
    print(f"🎉 Intégration terminée ! {success_count}/{len(main_files)} fichiers traités avec succès")
    print("\n📋 Instructions d'utilisation :")
    print("1. La barre latérale est maintenant visible sur toutes les pages")
    print("2. Sur mobile, utilisez le bouton burger (☰) pour ouvrir/ferrir la sidebar")
    print("3. Le contenu principal s'ajuste automatiquement avec un margin-left")
    print("4. La page active est automatiquement mise en surbrillance")
    
    return success_count

if __name__ == "__main__":
    main() 