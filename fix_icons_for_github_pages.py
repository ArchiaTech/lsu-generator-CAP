#!/usr/bin/env python3
"""
Script pour corriger les icônes manquantes sur GitHub Pages
Ajoute Font Awesome en fallback et améliore la compatibilité des emojis
"""

import os
import re
from pathlib import Path

def add_font_awesome_to_head(html_content):
    """Ajoute Font Awesome CSS dans le head si pas déjà présent"""
    if 'font-awesome' not in html_content.lower() and 'fontawesome' not in html_content.lower():
        # Chercher la balise </head> ou </style> pour insérer Font Awesome
        font_awesome_link = '    <!-- Font Awesome CSS (fallback pour les icônes) -->\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">\n    \n'
        
        # Insérer après Bootstrap si présent
        if 'bootstrap' in html_content.lower():
            pattern = r'(<link[^>]*bootstrap[^>]*>)'
            replacement = r'\1\n' + font_awesome_link
            html_content = re.sub(pattern, replacement, html_content, flags=re.IGNORECASE)
        else:
            # Insérer après la première balise <style> ou avant </head>
            if '<style>' in html_content:
                pattern = r'(<style>)'
                replacement = font_awesome_link + r'\1'
                html_content = re.sub(pattern, replacement, html_content)
            elif '</head>' in html_content:
                pattern = r'(</head>)'
                replacement = font_awesome_link + r'\1'
                html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def add_icon_fallback_styles(html_content):
    """Ajoute les styles CSS pour les icônes de fallback"""
    fallback_styles = '''
        /* Amélioration de la compatibilité des icônes */
        .icon-fallback {
            display: inline-block;
            width: 1em;
            height: 1em;
            text-align: center;
            line-height: 1;
        }

        /* Fallback pour les emojis qui ne s'affichent pas */
        .btn .emoji-icon {
            display: inline-block;
            margin-right: 5px;
        }

        /* Styles pour les icônes Font Awesome en fallback */
        .fa-fallback {
            display: none;
        }

        /* Amélioration de l'affichage des boutons avec icônes */
        .btn-with-icon {
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }

        /* Amélioration de l'affichage des emojis */
        .emoji-icon {
            font-size: 1.1em;
            vertical-align: middle;
        }
'''
    
    # Ajouter les styles avant la fermeture de </style>
    if '</style>' in html_content:
        pattern = r'(</style>)'
        replacement = fallback_styles + r'\1'
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def improve_button_icons(html_content):
    """Améliore les boutons avec des icônes de fallback"""
    
    # Mapping des emojis vers les icônes Font Awesome
    icon_mapping = {
        '👁️': 'fa-eye',
        '✏️': 'fa-edit',
        '🗑️': 'fa-trash',
        '➕': 'fa-plus',
        '📥': 'fa-download',
        '📤': 'fa-upload',
        '💾': 'fa-save',
        '❌': 'fa-times',
        '📸': 'fa-camera',
        '👤': 'fa-user',
        '🔍': 'fa-search',
        '📋': 'fa-list',
        '📊': 'fa-chart-bar',
        '💬': 'fa-comments',
        '👨‍👩‍👧‍👦': 'fa-users',
        '🏠': 'fa-home',
        '📝': 'fa-file-alt',
        '🔧': 'fa-cog',
        '🧭': 'fa-compass',
        '🎓': 'fa-graduation-cap',
        '✨': 'fa-magic',
        '📁': 'fa-folder',
        '📄': 'fa-file',
        '📈': 'fa-chart-line',
        '🌐': 'fa-globe',
        '✅': 'fa-check',
        '⏳': 'fa-clock',
        '⚠️': 'fa-exclamation-triangle',
        'ℹ️': 'fa-info-circle',
        '📞': 'fa-phone',
        '🎯': 'fa-bullseye',
        '📚': 'fa-book',
        '🔄': 'fa-sync',
        '👥': 'fa-users',
        '👨‍🏫': 'fa-chalkboard-teacher'
    }
    
    # Améliorer les boutons avec des icônes
    for emoji, fa_class in icon_mapping.items():
        # Pattern pour les boutons avec emojis
        button_pattern = rf'<button([^>]*>)\s*{re.escape(emoji)}\s*([^<]*)</button>'
        
        def replace_button(match):
            button_attrs = match.group(1)
            button_text = match.group(2)
            
            # Créer le nouveau bouton avec fallback
            new_button = f'<button{button_attrs} class="btn-with-icon">'
            new_button += f'<span class="emoji-icon">{emoji}</span>'
            new_button += f'<i class="fas {fa_class} fa-fallback"></i>'
            new_button += f'{button_text}</button>'
            
            return new_button
        
        html_content = re.sub(button_pattern, replace_button, html_content)
    
    return html_content

def improve_navigation_icons(html_content):
    """Améliore les icônes de navigation"""
    
    nav_icon_mapping = {
        '🎓': 'fa-graduation-cap',
        '🏠': 'fa-home',
        '📝': 'fa-file-alt',
        '👤': 'fa-user',
        '📸': 'fa-camera',
        '🔧': 'fa-cog',
        '🧭': 'fa-compass'
    }
    
    for emoji, fa_class in nav_icon_mapping.items():
        # Pattern pour les spans avec icônes de navigation
        nav_pattern = rf'<span class="(logo-icon|nav-icon)">{re.escape(emoji)}</span>'
        
        def replace_nav_icon(match):
            span_class = match.group(1)
            new_span = f'<span class="{span_class}">'
            new_span += f'<span class="emoji-icon">{emoji}</span>'
            new_span += f'<i class="fas {fa_class} fa-fallback"></i>'
            new_span += '</span>'
            return new_span
        
        html_content = re.sub(nav_pattern, replace_nav_icon, html_content)
    
    return html_content

def add_icon_detection_script(html_content):
    """Ajoute un script JavaScript pour détecter et corriger les icônes manquantes"""
    
    icon_script = '''
    <script>
    // Script de détection et correction des icônes manquantes
    document.addEventListener('DOMContentLoaded', function() {
        // Fonction pour détecter si un emoji s'affiche correctement
        function isEmojiSupported(emoji) {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            ctx.font = '16px Arial';
            ctx.fillText(emoji, 0, 16);
            const data = ctx.getImageData(0, 0, 16, 16).data;
            return data.some(pixel => pixel !== 0);
        }
        
        // Vérifier et corriger les icônes
        function fixMissingIcons() {
            const emojiElements = document.querySelectorAll('.emoji-icon');
            
            emojiElements.forEach(element => {
                const emoji = element.textContent;
                if (!isEmojiSupported(emoji)) {
                    // Masquer l'emoji et afficher l'icône Font Awesome
                    element.style.display = 'none';
                    const fallbackIcon = element.nextElementSibling;
                    if (fallbackIcon && fallbackIcon.classList.contains('fa-fallback')) {
                        fallbackIcon.style.display = 'inline-block';
                    }
                }
            });
        }
        
        // Exécuter après un délai pour laisser le temps au rendu
        setTimeout(fixMissingIcons, 100);
        
        // Réexécuter si nécessaire
        window.addEventListener('load', fixMissingIcons);
    });
    </script>
'''
    
    # Ajouter le script avant la fermeture de </body>
    if '</body>' in html_content:
        pattern = r'(</body>)'
        replacement = icon_script + r'\1'
        html_content = re.sub(pattern, replacement, html_content)
    
    return html_content

def process_html_file(file_path):
    """Traite un fichier HTML pour corriger les icônes"""
    print(f"Traitement de {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Appliquer les corrections
        content = add_font_awesome_to_head(content)
        content = add_icon_fallback_styles(content)
        content = improve_button_icons(content)
        content = improve_navigation_icons(content)
        content = add_icon_detection_script(content)
        
        # Sauvegarder le fichier modifié
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path} corrigé avec succès")
        
    except Exception as e:
        print(f"❌ Erreur lors du traitement de {file_path}: {e}")

def main():
    """Fonction principale"""
    print("🔧 Correction des icônes pour GitHub Pages")
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
    
    print("\n🎉 Correction terminée !")
    print("\n📋 Résumé des améliorations apportées :")
    print("   ✅ Ajout de Font Awesome CSS en fallback")
    print("   ✅ Styles CSS pour améliorer la compatibilité")
    print("   ✅ Boutons avec icônes de fallback")
    print("   ✅ Navigation avec icônes de fallback")
    print("   ✅ Script JavaScript de détection automatique")
    print("\n🌐 Les icônes devraient maintenant s'afficher correctement sur GitHub Pages !")

if __name__ == "__main__":
    main() 