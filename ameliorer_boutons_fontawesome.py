#!/usr/bin/env python3
"""
Script pour améliorer les boutons en remplaçant les emojis par des icônes Font Awesome
Spécialement conçu pour les boutons mentionnés dans la demande utilisateur
"""

import os
import re
from pathlib import Path

def replace_emoji_with_fontawesome(html_content):
    """Remplace les emojis spécifiques par des icônes Font Awesome"""
    
    # Mapping des emojis vers Font Awesome (selon la demande utilisateur)
    emoji_mapping = {
        '🐣': 'fa-baby',           # Ajouter un élève
        '🐞': 'fa-download',       # Importer
        '📤': 'fa-upload',         # Exporter
        '➕': 'fa-plus',           # Ajouter (alternative)
        '📥': 'fa-download',       # Importer (alternative)
        '👁️': 'fa-eye',           # Voir
        '✏️': 'fa-edit',           # Modifier
        '🗑️': 'fa-trash',         # Supprimer
        '💾': 'fa-save',           # Sauvegarder
        '❌': 'fa-times',          # Fermer/Annuler
        '📸': 'fa-camera',         # Photo
        '👤': 'fa-user',           # Utilisateur
        '🔍': 'fa-search',         # Rechercher
        '📋': 'fa-list',           # Liste
        '📊': 'fa-chart-bar',      # Graphiques
        '💬': 'fa-comments',       # Commentaires
        '👨‍👩‍👧‍👦': 'fa-users',     # Famille
        '🏠': 'fa-home',           # Accueil
        '📝': 'fa-file-alt',       # Documents
        '🔧': 'fa-cog',            # Paramètres
        '🧭': 'fa-compass',        # Navigation
        '🎓': 'fa-graduation-cap', # École
        '✨': 'fa-magic',          # Générer
        '📁': 'fa-folder',         # Dossier
        '📄': 'fa-file',           # Fichier
        '📈': 'fa-chart-line',     # Progression
        '🌐': 'fa-globe',          # Web
        '✅': 'fa-check',          # Valider
        '⏳': 'fa-clock',          # En attente
        '⚠️': 'fa-exclamation-triangle', # Attention
        'ℹ️': 'fa-info-circle',    # Information
        '📞': 'fa-phone',          # Téléphone
        '🎯': 'fa-bullseye',       # Cible
        '📚': 'fa-book',           # Livre
        '🔄': 'fa-sync',           # Synchroniser
        '👥': 'fa-users',          # Groupe
        '👨‍🏫': 'fa-chalkboard-teacher' # Enseignant
    }
    
    # Remplacer les emojis dans les boutons avec la classe btn-with-icon
    for emoji, fa_class in emoji_mapping.items():
        # Pattern pour les boutons avec emojis
        button_pattern = rf'<button([^>]*class="[^"]*btn-with-icon[^"]*"[^>]*>)\s*{re.escape(emoji)}\s*([^<]*)</button>'
        
        def replace_button(match):
            button_attrs = match.group(1)
            button_text = match.group(2)
            
            # Créer le nouveau bouton avec icône Font Awesome
            new_button = f'<button{button_attrs}'
            new_button += f'<i class="fas {fa_class} icon-fa"></i>'
            new_button += f'{button_text}</button>'
            
            return new_button
        
        html_content = re.sub(button_pattern, replace_button, html_content)
        
        # Remplacer aussi les emojis dans les spans avec classe emoji-icon
        span_pattern = rf'<span class="emoji-icon">{re.escape(emoji)}</span>'
        span_replacement = f'<i class="fas {fa_class} icon-fa"></i>'
        html_content = re.sub(span_pattern, span_replacement, html_content)
    
    return html_content

def add_fontawesome_styles(html_content):
    """Ajoute les styles CSS pour les icônes Font Awesome"""
    
    fontawesome_styles = '''
        /* Styles pour les icônes Font Awesome */
        .icon-fa {
            font-size: 1.1em;
            width: 20px;
            text-align: center;
            margin-right: 8px;
        }

        /* Amélioration des boutons avec icônes */
        .btn-with-icon {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            font-weight: 500;
            transition: all 0.3s ease;
            cursor: pointer;
            text-decoration: none;
        }

        .btn-with-icon:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        /* Styles spécifiques pour les boutons d'action */
        .btn-with-icon.btn-success {
            background: linear-gradient(135deg, #28a745, #1e7e34);
            color: white;
        }

        .btn-with-icon.btn-info {
            background: linear-gradient(135deg, #17a2b8, #117a8b);
            color: white;
        }

        .btn-with-icon.btn-warning {
            background: linear-gradient(135deg, #ffc107, #e0a800);
            color: #212529;
        }

        .btn-with-icon.btn-primary {
            background: linear-gradient(135deg, #007bff, #0056b3);
            color: white;
        }

        .btn-with-icon.btn-danger {
            background: linear-gradient(135deg, #dc3545, #c82333);
            color: white;
        }

        .btn-with-icon.btn-secondary {
            background: linear-gradient(135deg, #6c757d, #545b62);
            color: white;
        }
'''
    
    # Ajouter les styles avant la fermeture de </style>
    if '</style>' in html_content:
        pattern = r'(</style>)'
        replacement = fontawesome_styles + r'\1'
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def ensure_fontawesome_included(html_content):
    """S'assure que Font Awesome est inclus dans le head"""
    
    fontawesome_link = '    <!-- Font Awesome CSS -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">\n    \n'
    
    # Vérifier si Font Awesome est déjà inclus
    if 'font-awesome' not in html_content.lower() and 'fontawesome' not in html_content.lower():
        # Insérer après Bootstrap si présent
        if 'bootstrap' in html_content.lower():
            pattern = r'(<link[^>]*bootstrap[^>]*>)'
            replacement = r'\1\n' + fontawesome_link
            html_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)
        else:
            # Insérer après la première balise <style> ou avant </head>
            if '<style>' in html_content:
                pattern = r'(<style>)'
                replacement = fontawesome_link + r'\1'
                html_content = re.sub(pattern, replacement, html_content)
            elif '</head>' in html_content:
                pattern = r'(</head>)'
                replacement = fontawesome_link + r'\1'
                html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def process_html_file(file_path):
    """Traite un fichier HTML pour améliorer les boutons"""
    print(f"Amélioration de {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Appliquer les améliorations
        content = ensure_fontawesome_included(content)
        content = add_fontawesome_styles(content)
        content = replace_emoji_with_fontawesome(content)
        
        # Sauvegarder le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} amélioré avec succès")
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {file_path}: {e}")

def main():
    """Fonction principale"""
    print("🎨 Amélioration des boutons avec Font Awesome")
    print("=" * 50)
    
    # Trouver tous les fichiers HTML
    html_files = list(Path('.').glob('*.html'))
    
    if not html_files:
        print("❌ Aucun fichier HTML trouvé dans le répertoire courant")
        return
    
    print(f"📁 {len(html_files)} fichiers HTML trouvés")
    
    # Traiter chaque fichier
    for html_file in html_files:
        process_html_file(html_file)
    
    print("\n🎉 Amélioration terminée !")
    print("\n📋 Résumé des améliorations apportées :")
    print("   ✅ Remplacement des emojis par des icônes Font Awesome")
    print("   ✅ Ajout de styles CSS améliorés pour les boutons")
    print("   ✅ Inclusion automatique de Font Awesome CSS")
    print("   ✅ Boutons avec animations et effets visuels")
    print("\n🎯 Boutons spécifiquement améliorés :")
    print("   🐣 → fa-baby (Ajouter un élève)")
    print("   🐞 → fa-download (Importer)")
    print("   📤 → fa-upload (Exporter)")
    print("\n🌐 Les boutons sont maintenant parfaitement compatibles avec GitHub Pages !")

if __name__ == "__main__":
    main() 